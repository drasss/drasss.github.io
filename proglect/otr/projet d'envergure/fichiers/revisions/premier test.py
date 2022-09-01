fichw=open("alla.txt","w")
k=""
for i in range(10):
      k=k+"----------------------(x-"+str(i)+")----------------------\n"
      for j in range(10):
            k=k+"(x-"+str(i)+")(x-"+str(j)+") = x² "+str(-i-j)+"x + "+str(i*j)+"\n"
fichw.write(k)
fichw.close()
