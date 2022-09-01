



                   #LIS MOI !!! Et si tu faisais une partie ou ca detecte les notions du language et une autre ou ca répond en fonction des balises ? la partie languageavec le for et le reste en if
a="d"
print("Bonjour, comment allez vous ? ")
position="début"
grave=False

while a!=('a','u','r','e','v','o','i','r'):
    a = input(":")
    a=tuple(a)
    a=a+(' ',)
    #identification de concepts
    negation=False
    morale=False
    savoir=False
    for i in range(len(a)):
        if (a[i-1]==" " and (a[i]=="s" or a[i]=="S") and a[i+1]=="u"):
            if (a[i+2]==" "):
                savoir=True
        if (a[i-1]==" " and (a[i]=="s" or a[i]=="S") and a[i+1]=="a"):
            if (a[i+2]=="i"):
                if(a[i+3]=="s" or a[i+3]=="t"):
                    if (a[i+4]==" "):
                        savoir=True
            if (a[i+2]=="v"):
                if (a[i+3]=="e"):
                    if (a[i+4]=="n" and a[i+5]=="t"):
                        if (a[i+6]==" "):
                            savoir=True
                    if (a[i+4]=="z"):
                        if (a[i+5]==" "):
                            savoir=True
            if (a[i+2]=="c" and a[i+5]=="h" and a[i+5]=="e" ):
                if (a[i+6]==" "):
                    savoir=True
            if a[i+2]=="u" and a[i+3]=="r":
                if(a[i+6]=="e" or a[i+7]=="z"):
                    if (a[i+8]==" "):
                        savoir=True
                if (a[i+4]=="i"):
                    if(a[i+5]=="e" or a[i+6]=="z"):
                            if (a[i+7]==" "):
                                savoir=True
                    if (a[i+5]=="o" and a[i+6]=="n" and a[i+7]=="t"):
                        if (a[i+8]==" "):
                            savoir=True
                if (a[i+4]=="a"):
                    if (a[i+5]==" "):
                        savoir=True
                    if (a[i+5]=="i"):
                        if (a[i+6]=="e" and a[i+7]=="n" and a[i+8]=="t"):
                            if (a[i+9]==" "):
                                savoir=True
                        if (a[i+6]==" "):
                                savoir=True
                        if(a[i+6]=="s" or a[i+7]=="t"):
                            if (a[i+8]==" "):
                                savoir=True
                        
                if (a[i+4]=="o" and a[i+5]=="n" and a[i+6]=="t"):
                    if (a[i+7]==" "):
                        savoir=True
    print(a)
    print(savoir)
                
                    
                
            

                
                
        
            
    
