import matplotlib.pyplot as plt

opcode = {
    "00000" : 
    {
        "inst":"add",
        "type":"A"
    },
    "00001" :  
    {
        "inst":"sub",
        "type":"A"
    },
    "00010" :  
    {
        "inst":"mov",
        "type":"B"
    },
    "00011" :  
    {
        "inst":"move",
        "type":"C"
    },
    "00100" :  
    {
        "inst":"ld",
        "type":"D"
    },
    "00101" :  
    {
        "inst":"st",
        "type":"D"
    },
    "00110" :  
    {
        "inst":"mul",
        "type":"A"
    },
    "00111" :  
    {
        "inst":"div",
        "type":"A"
    },
    "01000" :  
    {
        "inst":"rs",
        "type":"B"
    },
    "01001" :  
    {
        "inst":"ls",
        "type":"B"
    },
    "01010" :  
    {
        "inst":"xor",
        "type":"A"
    },
    "01011" :  
    {
        "inst":"or",
        "type":"A"
    },
    "01100" :  
    {
        "inst":"and",
        "type":"A"
    },
    "01101" :  
    {
        "inst":"not",
        "type":"C"
    },
    "01110" :  
    {
        "inst":"cmp",
        "type":"C"
    },
    "01111" :  
    {
        "inst":"jmp",
        "type":"E"
    },
    "10000" :   
    {
        "inst":"jlt",
        "type":"E"
    },
    "10001" :   
    {
        "inst":"jgt",
        "type":"E"
    },
    "10010" :   
    {
        "inst":"je",
        "type":"E"
    },
    "10011" :   
    {
        "inst":"hlt",
        "type":"F"
    },
}

register = {
    "R0" : "000",
    "R1" : "001",
    "R2" : "010",
    "R3" : "011",
    "R4" : "100",
    "R5" : "101",
    "R6" : "110",
    "FLAGS" : "111",
}

def cmp(a, b):
    if a == b:
        return 1
    else:
        return 0


def main():
    reg_values={
        "000":"0"*16,
        "001":"0"*16,
        "010":"0"*16,
        "011":"0"*16,
        "100":"0"*16,
        "101":"0"*16,
        "110":"0"*16,
        "111":"0"*16, 
    }
    pc = -1
    tag = 0
    mem_heap = []
    line_heap = []
    pc_heap = []
    while tag == 0:
        line = input('')
        pc += 1
        pc_heap.append(pc)
        if not line:
            break
        elif line[0:5] == "10011":
            tag += 1
            simulator(line,pc,reg_values,mem_heap,line_heap)
            
        else:
            simulator(line,pc,reg_values,mem_heap,line_heap)
    memory(mem_heap,line_heap)
    plot(pc_heap,line_heap)

def memory(mem_heap,line_heap):
    for j in line_heap:
        print(j)
    for mem in mem_heap:
        print(str('{0:016b}'.format(int(mem,2))))
    for i in range(0,256 -len(mem_heap) - len(line_heap)):
        print("0"*16)

def simulator(line,pc,reg_values,mem_heap,line_heap):
    line_heap.append(line)
    execute(line,reg_values,mem_heap)
    print("\n")
    print('{0:08b}'.format(int(pc))+" "+str(reg_values["000"])+" "+str(reg_values["001"])+" "+str(reg_values["010"])+" "+str(reg_values["011"])+" "+str(reg_values["100"])+" "+str(reg_values["101"])+" "+str(reg_values["110"])+" "+str(reg_values["111"]))

def execute(line,reg_values,mem_heap):
    op = line[0:5]
    if op in opcode:
        if opcode[str(op)]["inst"] =="add":
            reg_values[str(line[7:10])] = str ('{0:016b}'.format ( int (reg_values[str(line[10:13])],2) + int(reg_values[str(line[13:])],2)))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="sub":
            reg_values[str(line[7:10])] = str ('{0:016b}'.format ( int (reg_values[str(line[10:13])],2) - int(reg_values[str(line[13:])],2)))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="mul":
            reg_values[str(line[7:10])] = str( '{0:016b}'.format ( int (reg_values[str(line[10:13])],2) * int(reg_values[str(line[13:])],2)))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="div":
            reg_values["000"] = str ('{0:016b}'.format ( int (reg_values[str(line[10:13])],2) / int(reg_values[str(line[13:])],2)))
            reg_values["001"] = str ('{0:016b}'.format ( int (reg_values[str(line[10:13])],2) % int(reg_values[str(line[13:])],2)))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="xor":
            reg_values[str(line[7:10])] = str ('{0:016b}'.format ( int (reg_values[str(line[10:13])],2) ^ int(reg_values[str(line[13:])],2))) 
            reg_values['111']="0"*16
 
        elif opcode[str(op)]["inst"] =="or":
            reg_values[str(line[7:10])] = str ('{0:016b}'.format ( int (reg_values[str(line[10:13])],2) | int(reg_values[str(line[13:])],2))) 
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="and":
            reg_values[str(line[7:10])] = str ('{0:016b}'.format ( int (reg_values[str(line[10:13])],2) & int(reg_values[str(line[13:])],2))) 
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="not":
            reg_values[str(line[10:13])] = str ('{0:016b}'.format (~ int(reg_values[str(line[13:])],2))) 
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="move":
            reg_values[str(line[10:13])] = str ('{0:016b}'.format (int(reg_values[str(line[13:])],2))) 
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="cmp":
            reg_values["111"] = str ('{0:016b}'.format (cmp(int(reg_values[str(line[10:13])],2),int(reg_values[str(line[13:])],2))))
        
        elif opcode[str(op)]["inst"] =="mov": 
            reg_values[str(line[5:8])] = str ('{0:016b}'.format (int(str(line[8:]),2)))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] == "rs":
            reg_values[str(line[5:8])] = str ('{0:016b}'.format (int(str(line[8:]),2)>>1))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] == "ls":
            reg_values[str(line[5:8])] = str ('{0:016b}'.format (int(str(line[8:]),2)<<1))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="ld":
            reg_values[str(line[5:8])] = str ('{0:016b}'.format (int(str(line[8:]),2)))
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="st":
            mem_heap.append(reg_values[str(line[5:8])])
            reg_values['111']="0"*16

        elif opcode[str(op)]["inst"] =="jlt" or opcode[str(op)]["inst"] == "je":
            reg_values["111"] = str('{0:016b}'.format(int(1)))
        
        elif opcode[str(op)]["inst"] == "hlt" or opcode[str(op)]["inst"] == "jgt":
            reg_values['111']="0"*16
    else:
        exit()
            

def plot(x,y):
    plt.scatter(x,y)
    plt.show()



if __name__ == '__main__':
	main()
      