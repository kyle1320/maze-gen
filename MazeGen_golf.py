from random import *
r,l,o,w,h=choice,list,(0,0),25,25
a=lambda(i,j):{(x,y)for x,y in[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]if(0<=x<w)&(0<=y<h)};v,e,p={o},a(o),{0}
while e:
 c=r(l(e));n=a(c);b,n=r(l(v&n)),n-v;e|=n
 while 1:
  p|={(b[0]+c[0],b[1]+c[1])};e^={c};v|={c};n=a(c)-v
  if not n or.05>random():break
  b,c=c,r(l(n));e|=n
print"\n@ ".join(["@ "*(w*2+1)]+["".join([("@ ","  ")[x%2+y%2<1 or{(x,y)}<p and y<h*2-1]for x in range(w*2)])for y in range(h*2)])
