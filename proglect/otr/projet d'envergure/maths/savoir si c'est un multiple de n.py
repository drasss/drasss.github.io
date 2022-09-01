

pr=""
for n in range(2,20):
      test=n*19
      pr+="-------------"+str(n)+"----------------"+str(test)+"\n"
      cent=int(test/100)
      dix=int(test/10)-cent*10
      unit=test%10
      for i in range(10):
            for j in range(10):
                  for k in range(10):
                        som=i*cent+j*dix+k*unit
                        if som%n==0:
                              pr+=str(i)+" "+str(j)+" "+str(k)+"\n"
print(pr)
      
