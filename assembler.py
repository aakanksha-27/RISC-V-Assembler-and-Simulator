#dictionary - instruction: (funct7,funct3,opcode)
RType = {
    "add":("0000000","000","0110011"),
    "sub":("0100000","000","0110011"),
    "sll":("0000000","001","0110011"),
    "slt":("0000000","010","0110011"),
    "sltu":("0000000","011","0110011"),
    "xor":("0000000","100","0110011"),
    "srl":("0000000","101","0110011"),
    "or":("0000000","110","0110011"),
    "and":("0000000","111","0110011")
}

#dictionary - instruction: (funct3,opcode)
IType = {
    "lw":("010","0000011"),
    "addi":("000","0010011"),
    "sltiu":("011","0010011"),
    "jalr":("000","1100111")
}

#dictionary - instruction: (funct3,opcode)
SType = {
    "sw":("010","0100011")
}

#dictionary - instruction: (funct3,opcode)
BType = {
    "beq":("000","1100011"),
    "bne":("001","1100011"),
    "blt":("100","1100011"),
    "bge":("101","1100011"),
    "bltu":("110","1100011"),
    "bgeu":("111","1100011")
}

#dictionary - instruction: (opcode)
UType = {
    "lui":("0110111"),
    "auipc":("0010111")
}

#dictionary - instruction: (opcode)
JType = {
    "jal":("1101111")
}

RegisterEncoding = {
    "zero": "00000",    #hard wired zero
    "ra": "00001",      #return address
    "sp": "00010",      #stack pointer
    "gp": "00011",      #global pointer
    "tp": "00100",      #thread pointer
    "t0": "00101",      #temporary register

    "t1": "00110",      #temporaries
    "t2": "00111",

    "s0": "01000",      #saved register/ frame pointer
    "fp": "01000",      
    "s1": "01001",      #saved register

    "a0": "01010",      #function arguments/ return values
    "a1": "01011",

    "a2": "01100",      #function arguments
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",

    "s2": "10010",      #saved registers
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",

    "t3": "11100",      #temporatries
    "t4": "11101",
    "t5": "11110",
    "t6": "11111"
}

labels = {
    "start":0,
    "end":1
}

program_memory = []