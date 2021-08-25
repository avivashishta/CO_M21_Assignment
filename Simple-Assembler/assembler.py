instructions ={
    "add" : {
        "type": "A",
        "opcode" : "00000",
    },
    "sub" : {
        "type": "A",
        "opcode" : "00001",
    },
    "mov" : {
        "type": "B",
        "opcode" : "00010",
    },
    # if performsmov register
    "move" : {
        "type": "C",
        "opcode" : "00011",
    },
    "ld" : {
        "type": "D",
        "opcode" : "00100",
    },
    "st" : {
        "type": "D",
        "opcode" : "00101",
    },
    "mul" : {
        "type": "A",
        "opcode" : "00110",
    },
    "div" : {
        "type": "A",
        "opcode" : "00111",
    },
    "rs" : {
        "type": "B",
        "opcode" : "01000",
    },
    "ls" : {
        "type": "B",
        "opcode" : "01001",
    },
    "xor" : {
        "type": "A",
        "opcode" : "01010",
    },
    "or" : {
        "type": "A",
        "opcode" : "01011",
    },
    "and" : {
        "type": "A",
        "opcode" : "01100",
    },
    "not" : {
        "type": "C",
        "opcode" : "01101",
    },
    "cmp" : {
        "type": "C",
        "opcode" : "01110"
    },
    "jmp" : {
        "type": "E",
        "opcode" : "01111",
    },
    "jlt" :{
        "type": "E",
        "opcode" : "10000"
    },
    "jgt" : {
        "type": "E",
        "opcode" : "10001"
    },
    "je" : {
        "type": "E",
        "opcode" : "10010"
    },
    "hlt":{
        "type": "F",
        "opcode" : "10011"
    }
}

register ={
    "R0" : "000",
    "R1" : "001",
    "R2" : "010",
    "R3" : "011",
    "R4" : "100",
    "R5" : "101",
    "R6" : "110",
    "FLAGS" : "111",
    
}
variables = dict()
labels = []

def assembler(line,count,tag,flag1,flag2):
    input_arr = line.split()
    if len(input_arr):

        if tag==1 and "hlt" not in input_arr:
            print("missing hlt instruction "+"at line "+str(count+1)+"\n")
        
        if input_arr[0] == "mov":
            if (not input_arr[2][0]=="$"):
                input_arr[0]="move"

        if input_arr[0]=="var" and len(input_arr) > 1:
            variables[input_arr[1]] = int(count) 

        if input_arr[0] not in instructions and input_arr[0][-1] == ":":
            if input_arr[0][:-1] in variables:
                print("Misuse of label as a variable "+"at line "+str(count)+"\n")
                
            else:
                label = input_arr[0][:-1]
                labels.append(label) 
                input_arr = input_arr[1:]
                

        if "FLAGS" in input_arr and input_arr[0] != "move":
            print("Illegal use of FLAGS Register "+"at line "+str(count)+"\n")
            
        if len(input_arr):
            if input_arr[0] == "var" and flag2 == True:
                print("Variables not declared at the beginning " + "at line "+ str(count)+"\n")
                
        if len(input_arr):
            if input_arr[0] in instructions:

                if flag1==False:
                    flag1 = True
                    flag2 = True

                if instructions[input_arr[0]]["type"] == "A":
                    if len(input_arr)!= 4:
                        print("Wrong Syntax for this type of instruction "+"at line "+str(count+1)+"\n")
                    else:   
                        if input_arr[1] not in register or input_arr[2] not in register or input_arr[3] not in register:
                            print("Typo in Register Name "+"at line"+str(count)+"\n")
                        print(instructions[input_arr[0]]["opcode"]+"00"+register[input_arr[1]]+register[input_arr[2]]+register[input_arr[3]]+"\n")
                
                elif instructions[input_arr[0]]["type"] == "B":
                    if len(input_arr)!=3:
                        print("Wrong Syntax for this type of instruction "+"at line "+str(count+1)+"\n")
                        

                    if input_arr[1] not in register:
                        print("Typo in Register Name " +"at line "+str(count+1)+"\n")
                        

                    if int(input_arr[2][1:])<0 or int(input_arr[2][1:])>255:
                        print("Illegal Immediate Value "+"at line "+str(count+1)+"\n")
                        

                    print(instructions[input_arr[0]]["opcode"]+register[input_arr[1]]+'{0:08b}'.format(int(input_arr[2][1:]))+"\n")
                
                elif instructions[input_arr[0]]["type"] == "C":
                    if len(input_arr)!=3:
                        print("Wrong Syntax for this type of instruction "+"at line "+str(count+1)+"\n")
                        
                    if input_arr[1] not in register or input_arr[2] not in register:
                        print("Typo in Register Name "+"at line"+str(count+1)+"\n")
                        

                    print(instructions[input_arr[0]]["opcode"]+"00000"+register[input_arr[1]]+register[input_arr[2]]+"\n")
                elif instructions[input_arr[0]]["type"] == "D":
                    if len(input_arr)!=3:
                        print("Wrong Syntax for this type of instruction "+ " at line "+ str(count+1)+"\n")
                    if input_arr[1] not in register:
                        print("Typo in Register Name "+" at line "+ str(count+1)+"\n")
                    if input_arr[2] not in variables:
                        print("Use of Undefined Variable " + " at line "+ str(count+1)+"\n")
                    else:
                        print(instructions[input_arr[0]]["opcode"]+register[input_arr[1]] + str('{0:08b}'.format(count)) + "\n")
                
                elif instructions[input_arr[0]]["type"] == "E":
                    if len(input_arr)!=2:
                        print("Wrong Syntax for this type of instruction "+"at line "+ str(count)+"\n")
                        
                    # if input_arr[1] not in labels:
                    #     print("Use of Undefined Label "+"at line "+ str(count)+"\n")
                    
                    else:
                        print(instructions[input_arr[0]]["opcode"]+"000"+ str('{0:08b}'.format(count-len(variables))) +"\n")

                elif instructions[input_arr[0]]["type"] == "F":
                    
                    if len(input_arr)!=1:
                        print("Wrong Syntax for this type of instruction "+"at line "+str(count)+"\n")
                        

                    if tag != 1:
                        print("hlt not being used as last instruction "+"at line "+str(count)+"\n")
                        

                    print(instructions[input_arr[0]]["opcode"]+"0"*11+"\n")
                    
                
                else:
                    print("Typos in Instruction name "+"at line "+str(count)+"\n")
                    
            
            
            if input_arr[0] not in instructions and input_arr[0] != "var" and input_arr[0] not in labels:
                print("General Syntax Error " + "at line "+str(count)+"\n")
                

                
            

# Assembler's function

# Code to read file from EOD Line wise.
def main():
    count = 0
    flag1= False
    flag2 = False
    tag = 0
    while tag == 0:
        line = input('')
        count += 1
        if not line:
            break
        if "hlt" in line.split():
            tag += 1
            assembler(line,count,tag,flag1,flag2)
        else:
            assembler(line,count,tag,flag1,flag2) # perform some operation(s) on given string

if __name__ == '__main__':
	main()




    