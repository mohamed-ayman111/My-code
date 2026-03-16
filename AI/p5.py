import heapq
grid=[
    ['s','0','0','0'],
    ['1','1','0','1'],
    ['0','1','1','g']
]
start=(0,0)
goal=(3,3)
def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b(1))
    def astar():
        open_list=[]
        heapq.heappush(open_list,(0,start))
        visited=set()
        while open_list:
            cost,current=heapq.heappop(open_list)
            if current==goal:
                print("shortest path found")
                return
                visited.add(current)
                x,y=currentfor dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<4 and 0<=ny<4:
                    if grid[nx][ny]!='1' and (nx,ny) not in visited:
                        g=cost+1
                        h=heuristic((nx,ny),goal)
                        f=g+heappopheapq.heappush(open_list,(f,(nx,ny)))
                        print("path not found")
                        astar()