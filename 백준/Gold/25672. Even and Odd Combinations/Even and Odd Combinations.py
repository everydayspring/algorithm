import sys

it=sys.stdin.read().splitlines()
t=int(it[0]);p=1
out=[]
for _ in range(t):
    n,k=map(int,it[p].split());p+=1
    line=it[p].strip() if p<len(it) else ""
    p+=1
    a=list(map(int,line.split())) if k>0 and line else []
    if 1 in a:
        a=[x for x in a if x!=1]
    else:
        a=[1]+a
    out.append(f"{n} {len(a)}")
    out.append(" ".join(map(str,a)))
sys.stdout.write("\n".join(out))
