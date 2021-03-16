from collections import deque
import datetime

class GraphA:
    
    def __init__(self, adjacent_list):
        self.adjacent_list = adjacent_list

    def get_adjacency(self, v):
        return self.adjacent_list[v]

    def h(self, n):
        H = {
            'S': 6,
            'A': 4,
            'B': 3,
            'C': 3,
            'D': 1,
            'G': 0
        }

        return H[n]

    def algorithm_Astar(self, start_n, stop_n):

        open_list = set([start_n])
        close_list = set([])
        tpath = []

        g = {}

        g[start_n] = 0

        parents = {}
        parents[start_n] = start_n

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path is not initiated')
                return None

            if n == stop_n:
                print(n)
                
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_n)

                reconst_path.reverse()

                print('Path Initiate: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_adjacency(n):

                if m not in open_list and m not in close_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in close_list:
                            close_list.remove(m)
                            open_list.add(m)

            print(n)
            open_list.remove(n)
            close_list.add(n)

        print('Path is not initiated')
        return None


    
adjacent_list = {
    'S': [('A', 3), ('B', 2)],    
    'A': [('B', 1), ('D', 5)],
    'B': [('C', 2), ('D', 3)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 1)]
}


print(adjacent_list)

print(adjacent_list['S'])
t0 = datetime.datetime.now()

graph1 = GraphA(adjacent_list)
graph1.algorithm_Astar('S', 'G')

t1 = datetime.datetime.now()
diff = t1-t0
print('The time difference is: ', diff.microseconds)




