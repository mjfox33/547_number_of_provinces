import numpy
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        
        islands_found = 0
        all_nodes = [i for i in range(m)]
        explored = []
        queue = []
        
        def work_to_do():
            return list(set(all_nodes) - set(explored))

        work = work_to_do()
        while work:
            explored.append(work[0])
            queue.append(work[0])
            islands_found += 1
            while queue:
                current_node = queue.pop(0)
                for node in range(m):
                    if node in explored:
                        continue
                    if isConnected[current_node][node] == 1:
                        queue.append(node)
                        explored.append(node)
            work = work_to_do()
            

        return islands_found