# Maze solver

def Display(visited):
    print('Solved maze path:')
    for i in visited:
        for j in i: 
            print(str(j)+' ',end='')
        print('')
def Find_path(Graph,Row):
    visited=[[0 for i in range(Row)] for i in range(Row)]
    if Maze_Path(Graph,0,0,visited,Row):
        Display(visited)
    else:
        print('Path not exist')

def Validate_path(Graph,x,y,visited,Row):
    if x>=0 and x<Row and y >=0 and y<Row and Graph[x][y]==1:
        return True
    else:
        return False

def Maze_Path(Graph,a,b,visited,Row):
    if a==Row-1 and b==Row-1:
        visited[a][b]=1
        return True
    if Validate_path(Graph,a,b,visited,Row):
        visited[a][b]=1
        if Maze_Path(Graph,a+1,b,visited,Row):
            return True
        if Maze_Path(Graph,a,b+1,visited,Row):
            return True

if __name__ == "__main__":
    Graph=[]
    Row=int(input('Enter number of rows\n'))
    for i in range(Row):
        print('Enter input for row :',i+1)
        row=list(map(int,input().split()))
        Graph.append(row)
    Find_path(Graph,Row)

