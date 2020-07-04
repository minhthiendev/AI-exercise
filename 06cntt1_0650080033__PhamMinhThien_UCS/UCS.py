
import numpy as np

roadmap = np.loadtxt("map.txt", dtype=str, delimiter=' ')

start = {'city': 'Arad',
         'cost': 0
         }
end = 'Bucharest'


def solution(neighbors, start, end):

    for x in neighbors:
        if(start['city'] == x[0]['city'] and end == x[len(x)-1]['city']):
            return x


def get_best_cost(a):
    b = []
    for x in a:
        b.append(int(x['cost']))
    return min(b)


def get_best_city(fringe):
    for x in fringe:
        if x['cost'] == get_best_cost(fringe):
            return x


def expand(road, current, fringe, paths):
    neighbors = []
    for x in road:
        if x[0] == current['city']:
            temp = {'city': x[1],
                    'cost': current['cost']+int(x[2])
                    }
            fringe.append(temp)
            neighbors.append(temp)
    for y in paths:
        if y[len(y)-1]['city'] == current['city']:
            for neighbor in neighbors:
                z = y+[neighbor]
                paths.append(z)
            paths.remove(y)

    return paths


def UCS(start, end):
    fringe = []
    closed = []
    fringe.append(start)
    paths = [[start]]
    while(not fringe == []):
        current = get_best_city(fringe)
        fringe.remove(current)
        if current not in closed:
            closed.append(current['city'])
        if current['city'] == end:
            return solution(paths, start, end)
        else:
            expand(roadmap, current, fringe, paths)
    return "no solution"


print("----------------------------UCS solution ---------------------------/", UCS(start, end))
