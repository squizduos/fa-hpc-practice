import multiprocessing
from collections import defaultdict, deque

def build_graph(assignments):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for left, rights in assignments:
        for right in rights:
            graph[right].append(left)
            in_degree[left] += 1
    
    return graph, in_degree

def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(order) == len(in_degree):
        return order
    else:
        return None 

def check_assignments_order(assignments, K):
    graph, in_degree = build_graph(assignments)
    order = topological_sort(graph, in_degree)
    
    if order is None:
        return False
    
    left_positions = {left: idx for idx, (left, _) in enumerate(assignments)}
    conflicts = 0
    
    for idx, (left, rights) in enumerate(assignments):
        for right in rights:
            if left_positions.get(right, -1) > idx:
                conflicts += 1
                if conflicts > K:
                    return False
    
    return True

def worker(assignments, K, result, idx):
    result[idx] = check_assignments_order(assignments, K)

def parallel_check(assignments_list, K):
    manager = multiprocessing.Manager()
    result = manager.list([None] * len(assignments_list))
    jobs = []
    
    for idx, assignments in enumerate(assignments_list):
        p = multiprocessing.Process(target=worker, args=(assignments, K, result, idx))
        jobs.append(p)
        p.start()
    
    for p in jobs:
        p.join()
    
    return result

if __name__ == "__main__":
    assignments_list = [
        [("a", ["b", "c"]), ("b", ["c"]), ("c", ["a"])],
        [("a", ["b"]), ("b", ["c"]), ("c", ["d"]), ("d", ["e"])],
        [("a", ["b"]), ("b", ["a", "c"]), ("c", ["d"]), ("d", ["e"])],
        [("a", ["b", "c"]), ("b", ["a", "d"]), ("c", ["e"]), ("d", ["e"]), ("e", ["f"])],
        [("a", ["b"]), ("b", ["c"]), ("c", ["d"]), ("d", ["e"]), ("e", ["a"])],
        [("a", ["b"]), ("b", ["c"]), ("c", ["a"]), ("d", ["e"]), ("e", ["f"])],
        [("a", ["b", "c"]), ("b", ["d"]), ("c", ["e"]), ("d", ["f"]), ("e", ["g"]), ("f", ["h"]), ("g", ["i"]), ("h", ["j"]), ("i", ["k"]), ("j", ["l"])],
        [("a", ["b", "c"]), ("b", ["c", "d"]), ("c", ["d", "e"]), ("d", ["e", "f"]), ("e", ["f", "g"]), ("f", ["g", "h"]), ("g", ["h", "i"]), ("h", ["i", "j"]), ("i", ["j", "k"]), ("j", ["k", "l"])], 
        [("a", ["b"]), ("b", ["c"]), ("c", ["d"]), ("d", ["e"]), ("e", ["f"]), ("f", ["a"])], 
        [("a", ["b"]), ("b", ["c"]), ("c", ["d"]), ("d", ["e"]), ("e", ["f"]), ("f", ["g"]), ("g", ["h"]), ("h", ["i"]), ("i", ["j"]), ("j", ["k"])] 
    ]
    K = 1 
    
    results = parallel_check(assignments_list, K)
    for idx, res in enumerate(results):
        print(f"Assignments list {idx} can be ordered with at most {K} conflicts: {res}")
