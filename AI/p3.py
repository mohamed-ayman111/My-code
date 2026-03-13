from collections import deque
def water_jug_bfs():
jug1_capacity=4
jug2_capacity=3
goal=2
visited=set()
queue=deque()
queue.append((0,0))
visited.add((0,0))
while queue:
    jug1,jug2=queue.popleft()
    print(jug1,jug2)
    if jug1==goal or jug2==goal:
        print("Goal reached")
        return
    possible_states=[
            (jug1_capacity,jug2),  #fill jug1
            (jug1,jug2_capacity),  #fill jug2
            (0,jug2), #empty jug1
            (jug1,0), #empty jug2
            (min(jug1+jug2,jug1_capacity),
            jug1+jug2 - min(jug1+jug2,jug1_capacity)), #pour jug2 --> jug1
            (jug1+jug2-min(jug1+jug2,jug2_capacity),
            min(jug1+jug2,jug2_capacity))  #pour jug1 --> jug2
        ]
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    print("Goal not reachable")
water_jug_bfs()