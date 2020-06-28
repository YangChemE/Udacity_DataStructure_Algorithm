### My own naive implementation of the A* algorithm for the final project###
import math

def shortest_path(M,start,goal):
    print("shortest path called")

    # Initialize a dictionary where the route (in a tuple) is the key and the corresponding f value be the value)
    f_values = {(start,):get_distance(M, start, goal)}
    
    while len(f_values) > 0:

        # get the explored route that has the smallest f value
        current_route = min(f_values, key=lambda k : f_values[k])
        
        # the last element in the route tuple is the current frontier node/intersection
        current = current_route[-1]
        
        # goal test
        if current == goal:
            break

        
        # checking all the neighbours    
        for node in M.roads[current]:
              
            # avoid going backwards
            if node in current_route:
                continue
               
            # calculating f value for this neighbour
            g = f_values[current_route] - get_distance(M, current, goal) + get_distance(M, current, node)
            h = get_distance(M, node, goal)
         
            f_value = g + h
            
            # update the f_value table for the newly added route
            new_route = list(current_route)
            new_route.append(node)
            new_route = tuple(new_route)
            f_values[new_route] = f_value
            
        # pop out the old route / updating frontier    
        f_values.pop(current_route)    
        
    # get the shortest route and change it from tuple to list 
    route = list(min(f_values, key=lambda k : f_values[k]))
    
    return route


def get_distance(M, A, B):
    dist = math.sqrt((M.intersections[A][0] - M.intersections[B][0])**2 + (M.intersections[A][1] - M.intersections[B][1])**2)
    return dist
