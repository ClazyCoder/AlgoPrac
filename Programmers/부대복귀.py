import heapq
INF = 999999999


def daijkstra(graph, start):
    Q = []
    dist = [INF] * len(graph)
    dist[start-1] = 0
    heapq.heappush(Q, start)
    while Q:
        u = heapq.heappop(Q)
        for v in graph[u]:
            if dist[u-1] + 1 < dist[v-1]:
                dist[v-1] = dist[u-1] + 1
                heapq.heappush(Q, v)
    return dist


def solution(n, roads, sources, destination):
    answer = []
    Q = []
    graph = {}
    for i in range(1, n+1):
        graph[i] = set()
    for road in roads:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])
    dist = daijkstra(graph, destination)
    for s in sources:
        if dist[s-1] == INF:
            answer.append(-1)
        else:
            answer.append(dist[s-1])
    return answer
