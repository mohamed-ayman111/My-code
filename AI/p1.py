from collections import deque
grid =[
    ['s','0','0'],
    ['1','1','0'],
    ['0','0','G']
]
queue=deque()
visited=set()
#find start
for i in range(3):
    for j in range(3):
        if grid[i][j]=='S':
            queue.append((i,j))
            visited.add((i,j))
            #BFS
            while queue:
                x,y=queue.popleft()
                if grid[x][y]=='G':
                    print("Goal Found")
                    break
                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx,ny=x+dx,y+dy
                        if 0<= nx <3 and 0 <=ny <3:
                            if grid[nx][ny]!='1' and (nx,ny) not in visited:
                                queue.append((nx,ny))
                                visited.add((nx,ny))