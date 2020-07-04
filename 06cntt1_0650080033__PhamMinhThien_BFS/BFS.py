
import numpy as np
import queue

roadmap = np.loadtxt("map.txt", dtype=str, delimiter=' ')

start = 'Arad'
end = 'Bucharest'


def solution(neighbors, start, end):
    for x in neighbors:
        if(start == x[0] and end == x[len(x)-1]):
            return x


def expand(road, current, fringe, closed, paths):
    neighbors = []
    for x in road:
        if x[0] == current:
            if x[1] not in list(closed.queue):
                fringe.put(x[1])
                neighbors.append(x[1])
    for y in paths:
        if y[len(y)-1] == current:
            for neighbor in neighbors:
                z = y+[neighbor]
                paths.append(z)
            paths.remove(y)

    return paths


def BFS(start, end):
    fringe = queue.Queue()
    closed = queue.Queue()
    fringe.put(start)

    paths = [[start]]
    while(fringe.empty() == False):
        current = fringe.get()
        if current not in list(closed.queue):
            closed.put(current)
        if current == end:
            return solution(paths, start, end)
        else:
            expand(roadmap, current, fringe, closed, paths)

        print("-----fringe-------", list(fringe.queue))

    return "no solution"


print("/-----------------------------BFS solution ---------------------------/", BFS(start, end))
