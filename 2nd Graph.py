from collections import deque
import datetime

class GraphB:
    
    def __init__(self, adjacent_list):
        self.adjacent_list = adjacent_list

    def get_adjancency(self, v):
        return self.adjacent_list[v]

    def h(self, n):
        H = {
            'S': 14,
            'A': 7,
            'B': 10,
            'C': 4,
            'D': 2,
            'E': 4,
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

            for (m, weight) in self.get_adjancency(n):
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
    'S': [('A', 6), ('B', 5), ('C', 10)],    
    'A': [('D', 6)],
    'B': [('D', 6), ('E', 7)],
    'C': [('E', 6)],
    'D': [('C', 4), ('G', 4)],
    'E': [('A', 3), ('G', 6)]
}
t0=datetime.datetime.now()
graph1 = GraphB(adjacent_list)

graph1.algorithm_Astar('S', 'G')

t1 = datetime.datetime.now()
diff = t1-t0
print('The time difference is : ', diff.microseconds)
 
 

