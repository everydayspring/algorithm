import sys
x1,y1=map(int,sys.stdin.readline().split())
x2,y2=map(int,sys.stdin.readline().split())
x3,y3=map(int,sys.stdin.readline().split())
v=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
print(1 if v>0 else -1 if v<0 else 0)
