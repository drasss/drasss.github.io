
mode=input("1)on traduit en eschaton ? ou 2) en francais ? ")
txt=input("texte a déchiffrer: ")
txt=tuple(txt)+(" ",)
no=""
if mode=="1":
    for i in range(len(txt)):
        if txt[i]=='a' or txt[i]=='A':
            no=no+"ae"
        if txt[i]=='b' or txt[i]=='B':
            no=no+"v"
        if txt[i]=='c' or txt[i]=='C':
            no=no+"k"
        if (txt[i]=='d' or txt[i]=='D'):
            if txt[i+1]==" ":
                no=no+"ct"
            else:
                no=no+"ct\'"
        if txt[i]=='e' or txt[i]=='E':
            no=no+"eh"
        if txt[i]=='f' or txt[i]=='F':
            no=no+"fh"
        if txt[i]=='g' or txt[i]=='G':
            no=no+"gl"
        if txt[i]=='h' or txt[i]=='H':
            if txt[i+1]==" ":
                no=no+"ht"
            else:
                no=no+"ht\'"
        if txt[i]=='i' or txt[i]=='I':
            no=no+"y"
        if txt[i]=='j' or txt[i]=='J':
            if txt[i+1]==" ":
                no=no+"cg"
            else:
                no=no+"cg\'"
        if txt[i]=='k' or txt[i]=='K':
            no=no+"c"
        if txt[i]=='l' or txt[i]=='L':
            if txt[i+1]==" ":
                no=no+"lw"
            else:
                no=no+"lw\'"
        if txt[i]=='m' or txt[i]=='M':
            if txt[i+1]==" ":
                no=no+"mg"
            else:
                no=no+"mg\'"
        if txt[i]=='n' or txt[i]=='N':
            if txt[i+1]==" ":
                no=no+"ng"
            else:
                no=no+"ng\'"
        if txt[i]=='o' or txt[i]=='O':
            no=no+"li"
        if txt[i]=='p' or txt[i]=='P':
            if txt[i+1]==" ":
                no=no+"ph"
            else:
                no=no+"ph\'"
        if txt[i]=='q' or txt[i]=='Q':
            no=no+"q"
        if txt[i]=='r' or txt[i]=='R':
            no=no+"r\'l"
        if txt[i]=='s' or txt[i]=='S':
            no=no+"sh"
        if txt[i]=='t' or txt[i]=='T':
            no=no+"tag"
        if txt[i]=='u' or txt[i]=='U':
            no=no+"ui"
        if txt[i]=='v' or txt[i]=='V':
            no=no+"w"
        if txt[i]=='w' or txt[i]=='W':
            no=no+"wg"
        if txt[i]=='x' or txt[i]=='X':
            if txt[i+1]==" ":
                no=no+"xa"
            else:
                no=no+"xa\'"
        if txt[i]=='y' or txt[i]=='Y':
            no=no+"yeh"
        if txt[i]=='z' or txt[i]=='Z':
            if txt[i+1]==" ":
                no=no+"ts"
            else:
                no=no+"ts\'"
        if txt[i]==' ':
            no=no+" "
print(no)
        
