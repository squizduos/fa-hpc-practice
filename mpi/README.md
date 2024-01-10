## инсталляция

https://stackoverflow.com/questions/26920083/fatal-error-mpi-h-no-such-file-or-directory-include-mpi-h

sudo apt install libopenmpi-dev
## Запуск и компиляция

### Для cpp:
```
mpic++ send_recv.cpp -o send_recv
mpirun -np 4 send_recv
```
### Для c
```
mpicc send_recv.c -o send_recv
mpirun -np 4 send_recv
```

# Если не находит mpi.h

прописать путь к ней в С файле 
Для ubuntu 16:

    #include </usr/lib/openmpi/include/mpi.h>
    
Узнать где mpi.h;

    mpicc -showme 

