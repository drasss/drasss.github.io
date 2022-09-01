t,j=tuple(),tuple()
for i in range(1,10001):
      res=i
      while res!=1:
            if res%2==0:res=res/2
            else:res=3*res+1
      t+=tuple(str(int(res)))
      j+=(str(i),)
for i in range(len(j)):
      print(j[i]+" -> "+t[i])
