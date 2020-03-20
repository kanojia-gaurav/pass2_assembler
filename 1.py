"""
Created by Gaurav Kanojia
"""
with open("aa.txt","r") as file:
    line=file.readlines()
    file.close()
import re
list1=[]
count=0
r=[]
address=""
lc=[]
lc.append(0)
symbol=[]
sym=[]
for i in line:
    r=re.split("\s*",i)
    list1.append(r)

for i in range(0,len(list1)):
    if(list1[1][2] == "*"):
        address="R"
        operand=0
    else:
        address="A"

for i in range(0, len(list1)):
        if((list1[i][1] == "start") or (list1[i][1] == "using")):
            count=0
            lc.append(count)
        
        elif(list1[i][0] == "-"):
            if((list1[i][2].isdigit()) and (list1[i][3].isdigit()) ):
                count+=2
                lc.append(count)
            else:
                count+=4    
                lc.append(count)

        elif(list1[i][0] != "-"):
            if(list1[i][2] == "b" or list1[i][3] == "b"):
                count+=1
                lc.append(count)
            elif(list1[i][2] == "h" or list1[i][3] == "h"):
                count+=2
                lc.append(count)
            elif(list1[i][2] == "f" or list1[i][3] == "f"):
                count+=4
                lc.append(count)
            elif(list1[i][2] == "d" or list1[i][3] == "d"):
                count+=8
                lc.append(count)
                
        if(list1[i][0]!="-"):

             if(i==0):
                 symbol.append(list1[i][0])
                 symbol.append(str(lc[-2]))
                 symbol.append(str(1))
                 if(list1[1][2]=="*"):
                     symbol.append('R')
                 else:
                     symbol.append("A")
                 
             else:
                    symbol.append(list1[i][0])
                    symbol.append(str(lc[-2]))
                    symbol.append(str(lc[-1]-lc[-2]))
                    if(list1[1][2]=="*"):
                        symbol.append('R')
                    else:
                        symbol.append("A")
                    
                
file1=open("symboltable.txt","w+")
file1.write("********SYMBOL TABLE**********\n\n")
file1.write("S\t\tV\t\tL\t\tR/A\n")

final = [symbol[i * 4:(i + 1) * 4] for i in range((len(symbol) + 4 - 1) // 4 )] 

for i in final:
    file1.write(str(i))
    file1.write("\n")
file1.close()

file2=open("pass1.txt","w+")
file2.write("************PASS 1****************\n\n")


for i in range(0,len(list1)):
    file2.write(str(lc[i]))
    file2.write("\t\t")
    if(list1[i][1] == "dc"):
        file2.write(str(list1[i][3]))
        file2.write('\n')
    elif(list1[i][1] == "ds"):
        file2.write('\n')
    elif(list1[i][1] == "start" or list1[i][1] == "using"):
        file2.write('\n')
    elif(list1[i][3].isalpha()):
        file2.write(str(list1[i][1]))
        file2.write('\t\t')
        file2.write(str(list1[i][2]))
        file2.write('\n')
    elif(list1[i][1] == "end"):
        file2.write("\n")
    else:
        file2.write(str(list1[i][1]))
        file2.write('\n')

file3=open("pass2.txt","w+")
file3.write("************PASS 2*********************\n\n")
v=[]
string1=[]
final1=[]


for i in range(0,len(list1)):
        for j in range(0,len(final)):
            if(list1[i][0] == "-"):
                if(list1[i][3] == final[j][0]):
                    v.append(final[j][1])

j=0
for i in range(0,len(list1)):
    file3.write(str(lc[i]))
    file3.write("\t\t")
    if(list1[i][1] == "dc"):
        file3.write(bin(int(list1[i][3])))
        file3.write('\n')
    elif(list1[i][1] == "ds"):
        file3.write('\n')
    elif(list1[i][1] == "start" or list1[i][1] == "using"):
        file3.write('\n')
    elif(list1[i][3].isalpha()):
        file3.write(str(list1[i][1]))
        file3.write('\t\t')
        file3.write(str(list1[i][2]))
        file3.write('\t\t')
        file3.write(str(v[j]))
        file3.write("(")
        file3.write(str(operand))
        file3.write(",")
        file3.write(str(list1[1][3]))
        file3.write(")")
        file3.write('\n')
        j=j+1
    elif(list1[i][1] == "end"):
        file3.write("\n")
    else:
        file3.write(str(list1[i][1]))
        file3.write('\n')


