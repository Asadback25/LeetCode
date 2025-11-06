# LettCode
# 3607. Power Grid Maintenance / Medium

class Solution:
    def processQueries(self, C: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)

        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

        power = collections.defaultdict(SortedList)
        poweron = [True] * C
        parent = [None] * C

        def bfs(start):
            q = collections.deque()

            parent[start - 1] = start
            q.append(start)
            power[start].add(start)

            while len(q) > 0:
                current = q.popleft()

                for v in adj_list[current]:
                    if parent[v - 1] is None:
                        parent[v - 1] = start
                        q.append(v)
                        power[start].add(v)

        for i in range(1, C + 1):
            if parent[i - 1] is None:
                bfs(i)

        ans = []
        for t, x in queries:
            if t == 1:
                if poweron[x - 1]:
                    ans.append(x)
                    continue

                if len(power[parent[x - 1]]) > 0:
                    ans.append(power[parent[x - 1]][0])
                    continue
                else:
                    ans.append(-1)
                    continue
            else:
                if poweron[x - 1]:
                    poweron[x - 1] = False
                    power[parent[x - 1]].remove(x)
        return ans