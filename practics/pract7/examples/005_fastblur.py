import pyopencl as cl
import numpy as np
import Image as im

def show_single_buffer(queue, n_pix, buffer):
	temp = np.empty(n_pix).astype(np.uint8)
	cl.enqueue_copy(queue, temp, buffer)
	test = im.new('L', cat.size)
	test.putdata(temp)
	test.show()

cat = im.open('data/cat.jpg').convert('RGBA').resize((640,480))
pix = np.array(list(cat.getdata())).astype(np.uint8)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

prg = cl.Program(ctx, """
    __kernel void sep_channels(__global uchar4 *a,
            __global uchar *r,
            __global uchar *g,
            __global uchar *b)
    {
      int gid = get_global_id(0);
      r[gid] = a[gid].x;
      g[gid] = a[gid].y;
      b[gid] = a[gid].z;
    }
    __kernel void mer_channels(__global uchar4 *a,
            __global uchar *r,
            __global uchar *g,
            __global uchar *b)
    {
      int gid = get_global_id(0);
      a[gid].x = r[gid];
      a[gid].y = g[gid];
      a[gid].z = b[gid];
      a[gid].w = 255;
    }
    __kernel void blur_channel(__global uchar *c,
            __global uchar *res,
            __local uchar *c_loc,
            uint w, uint h)
    {
      uint xg = get_global_id(0);
      uint yg = get_global_id(1);
      uint xl = get_local_id(0)+1;
      uint yl = get_local_id(1)+1;
      uint wm = get_local_size(0)+2;
      uint wl = get_local_size(0);
      uint hl = get_local_size(1);
      c_loc[xl+wm*yl] = c[xg+w*yg];
      uint left = clamp(xg-1, (uint)0, w);
      if(xl==1) c_loc[0+wm*yl] = c[left+w*yg];
      uint right = clamp(xg+1, (uint)0, w);
      if(xl==wl) c_loc[(wl+1)+wm*yl] = c[right+w*yg];
      uint top = clamp(yg-1, (uint)0, h);
      if(yl==1) c_loc[xl+wm*0] = c[xg+w*top];
      uint bot = clamp(yg+1, (uint)0, h);
      if(yl==hl) c_loc[xl+wm*(hl+1)] = c[xg+w*bot];
      barrier(CLK_LOCAL_MEM_FENCE);
      uchar blr = 0.2*c_loc[xl+wm*(yl-1)] +
                  0.2*c_loc[xl-1+wm*yl] +
                  0.2*c_loc[xl+wm*yl] +
                  0.2*c_loc[xl+1+wm*yl] +
                  0.2*c_loc[xl+wm*(yl+1)];
      res[xg+w*yg] = blr;
    }
    """).build()

n_pix = cat.size[0]*cat.size[1]
result = np.empty_like(pix)
mf = cl.mem_flags
pix_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=pix)
r_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
g_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
b_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
rb_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
gb_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
bb_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
pixb_buf = cl.Buffer(ctx, mf.WRITE_ONLY | mf.COPY_HOST_PTR, hostbuf=result)

n_workers = (cat.size[0]*cat.size[1],)
prg.sep_channels(queue, n_workers, None, pix_buf, r_buf, g_buf, b_buf)

wgs = cl.Kernel(prg, 'blur_channel').get_work_group_info(cl.kernel_work_group_info.WORK_GROUP_SIZE,
		ctx.get_info(cl.context_info.DEVICES)[0])
n_local = (16,12)
if n_local[0]*n_local[1] > wgs:
	print "Reduce the n_local variable size please!"

nn_buf = cl.LocalMemory((n_local[0]+2)*(n_local[1]+2))
n_workers = (cat.size[0], cat.size[1])

prg.blur_channel(queue, n_workers, n_local, r_buf, rb_buf, nn_buf, np.uint32(cat.size[0]), np.uint32(cat.size[1]))
prg.blur_channel(queue, n_workers, n_local, g_buf, gb_buf, nn_buf, np.uint32(cat.size[0]), np.uint32(cat.size[1]))
prg.blur_channel(queue, n_workers, n_local, b_buf, bb_buf, nn_buf, np.uint32(cat.size[0]), np.uint32(cat.size[1]))

#show_single_buffer(queue, n_pix, r_buf)
show_single_buffer(queue, n_pix, rb_buf)

n_workers = (cat.size[0]*cat.size[1],)
prg.mer_channels(queue, n_workers, None, pixb_buf, rb_buf, gb_buf, bb_buf)

cl.enqueue_copy(queue, result, pixb_buf)

im_data = [ (p[0], p[1], p[2], p[3]) for p in result ]
cat.putdata(im_data)
cat.show()