def assemble(inFileName,outFileName):
    lines=[]
    with open(inFileName) as fIn:
        for l in fIn:
            if l[0]=='#' or l[0]=='\n':
                continue
            if l[-1]=='\n':
                l=l[:-1]
            lines.append(l)
    intList=[]
    for line in lines:
        handle=handleLine(line)
        for a in handle:
            intList.append(a)
    
        
    with open(outFileName,'w',encoding = 'utf-8') as fOut:
        for a in intList:
            element =str(a)+','
            fOut.write(element)

def handleLine(l):
    tokens=l.split()
    immflags=['0','0','0']#c,b,a
    addresses=[]
    opcodes=['ADD','MUL','INP','OUT','JNZ','JPZ','LES','EQU','REL']
    if len(tokens)==1:
        return [99]
    else:
        for i in range(1,len(tokens)):
            if tokens[i][0] == 'P':
                immflags[i-1]='0'
            elif tokens[i][0] == 'I':
                immflags[i-1]='1'
            elif tokens[i][0] == 'I':
                immflags[i-1]='2'
            addresses.append(int(tokens[i][1:]))
    out=[int(immflags[2]+immflags[1]+immflags[0]+str(opcodes.index(tokens[0])))]
    for a in addresses:
        out.append(a)
    
    return out
            
print("please enter input file")
inFileName=input()+'.txt'
print("please enter output file")
outFileName=input()+'.txt'        
assemble(inFileName,outFileName)
