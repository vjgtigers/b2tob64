

b2tob64_N_B = {1:1,2:10,3:11,4:100,5:101,6:110,7:111,8:1000,9:1001,10:1010,11:1011,12:1100,13:1101,14:1110,15:1111,16:10000,17:10001,18:10010,19:10011,20:10100,21:10101,22:10110,23:10111,24:11000,25:11001,26:11010,27:11011,28:11100,29:11101,30:11110,31:11111,32:100000,33:100001,34:100010,35:100011,36:100100,37:100101,38:100110,39:100111,40:101000,41:101001,42:101010,43:101011,44:101100,45:101101,46:101110,47:101111,48:110000,49:110001,50:110010,51:110011,52:110100,53:110101,54:110110,55:110111,56:111000,57:111001,58:111010,59:111011,60:111100,61:111101,62:111110,63:111111, 0:0}
b2tob64_B_N = {v: k for k, v in b2tob64_N_B.items()}
b2tob64_N_A = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z",27:"a",28:"b",29:"c",30:"d",31:"e",32:"f",33:"g",34:"h",35:"i",36:"j",37:"k",38:"l",39:"m",40:"n",41:"o",42:"p",43:"q",44:"r",45:"s",46:"t",47:"u",48:"v",49:"w",50:"x",51:"y",52:"z",53:"0",54:"1",55:"2",56:"3",57:"4",58:"5",59:"6",60:"7",61:"8",62:"9",63:"-",0:"_"}
b2tob64_A_N = {v: k for k, v in b2tob64_N_A.items()}

b2tob64_A_S=  {1:"1",2:"10",3:"11",4:"100",5:"101",6:"110",7:"111",8:"1000",9:"1001",10:"1010",11:"1011",12:"1100",13:"1101",14:"1110",15:"1111",16:"10000",17:"10001",18:"10010",19:"10011",20:"10100",21:"10101",22:"10110",23:"10111",24:"11000",25:"11001",26:"11010",27:"11011",28:"11100",29:"11101",30:"11110",31:"11111",32:"100000",33:"100001",34:"100010",35:"100011",36:"100100",37:"100101",38:"100110",39:"100111",40:"101000",41:"101001",42:"101010",43:"101011",44:"101100",45:"101101",46:"101110",47:"101111",48:"110000",49:"110001",50:"110010",51:"110011",52:"110100",53:"110101",54:"110110",55:"110111",56:"111000",57:"111001",58:"111010",59:"111011",60:"111100",61:"111101",62:"111110",63:"111111"}

import random
def new_away_base(str22):
    back_to = []
    back_to[:0] = str22
    str33 = ""
    back_len = len(back_to)
    counter = 1
    for i in back_to:
        num = b2tob64_A_N[i]
        num2 = b2tob64_N_B[num]
        better = str(num2)
        print(better)
        e1 = "0"
        e2 = "00"
        e3 = "000"
        e4 = "0000"
        e5 = "00000"
        if counter == back_len:
            print("calling back")
            last_len = len(i)
            if len(better) == 5:
                better = e1 + better
                print("calling bak")
            elif len(better) == 4:
                better = e2 + better
                print("calling bck")
            elif len(better) == 3:
                better = e3 + better
                print("calli back")
            elif len(better) == 2:
                better = e4 + better
                print("caing back")
            elif len(better) == 1:
                better = e5 + better
                print(" back")
        else:
            if len(better) == 5:
                better = e1 + better
            elif len(better) == 4:
                better = e2 + better
            elif len(better) == 3:
                better = e3 + better
            elif len(better) == 2:
                better = e4 + better
            elif len(better) == 1:
                better = e5 + better
        str33 = str33 + better
        counter += 1
    return (str33)




def away_base(str22):
    back_to = []
    back_to[:0] = str22
    str33 = ""
    checker = 1
    for i in back_to:
        num = b2tob64_A_N[i]
        num2 = b2tob64_N_B[num]
        better = str(num2)
        e1 = "0"
        e2 = "00"
        e3 = "000"
        e4 = "0000"
        e5 = "00000"
        if checker == 17:
            if len(better) == 2:
                better = e2 + better
            elif len(better) == 1:
                better = e3 + better
            elif len(better) == 3:
                better = e1 + better
        elif len(better) != 6:
            if len(better) == 5:
                better = e1 + better
            elif len(better) == 4:
                better = e2 + better
            elif len(better) == 3:
                better = e3 + better
            elif len(better) == 2:
                better = e4 + better
            elif len(better) == 1:
                better = e5 + better
        checker += 1
        str33 = str33 + better
    return (str33)
    
def to_base(new_num):
    counter = 0
    arrayF = []
    arr = []
    val = 0
    for i in iter(new_num):
        if counter < 6:
            arr.append(i)
        counter += 1
        if counter == 6:
            arrayF.append(arr)
            arr = []
            counter = 0
        val +=1
        if val == 99:
            arrayF.append(arr)
    str22 = ""
    for i in arrayF:
        num = int(''.join(i))
        num2 = b2tob64_B_N[num]
        char = b2tob64_N_A[num2]
        str22 += char
    return str22


def new_to(new_num):
    counter = 0
    arrayF = []
    arr = []
    val = 0
    select_check = 1
    strlen = len(new_num)
    for i in iter(new_num):
        #print(i)
        if select_check == strlen:
            arr.append(i)
            arrayF.append(arr)
        else:
            if counter < 6:
                arr.append(i)
                counter += 1
            if counter == 6:
                arrayF.append(arr)
                arr = []
                counter = 0
            val +=1
        select_check += 1
    str22 = ''
    for i in arrayF:
        num = int(''.join(i))
        num2 = b2tob64_B_N[num]
        char = b2tob64_N_A[num2]
        str22 += char
    return str22
    
def new_new_to(new_num):
    counter = 0
    arrayF = []
    arr = []
    val = 0
    select_check = 1
    strlen = len(new_num)
    for i in iter(new_num):
        #print(i)
        if select_check == strlen:
            arr.append(i)
            arrayF.append(arr)
            arrayF.append(len(arr))
        else:
            if counter < 6:
                arr.append(i)
                counter += 1
            if counter == 6:
                arrayF.append(arr)
                arr = []
                counter = 0
            val +=1
        select_check += 1
    str22 = ''
    for i in arrayF:
        num = int(''.join(i))
        num2 = b2tob64_B_N[num]
        char = b2tob64_N_A[num2]
        str22 += char
    return str22
    




test1 = "101011000100101010101010010011010110001001010101010100100101010000101001010101101101011000100101010101010010010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101010110101001011001010000010001010101011010101010101011010100110100101010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101"
test2 = "101011000100101010101010010011010110001001010101010100100101010000101001010101101101011000100101010101010010010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101010110101001011001010000010001010101011010101010101011010100110100101010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010000010"
test3 = "101011000100101010101010010011010110001001010101010100100101010000101001010101101101011000100101010101010010010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101010110101001011001010000010001010101011010101010101011010100110100101010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010000101"

print(new_new_to(test1))


#e= (new_to(test1))
#test2 = new_away_base(e)
#print(test2)
#if test2 == test1: 
#    print("worked")
#else:
#    print("failed")
#print(new_to("1010110001001010101010100100110101100010010101010101001001010100001010010101011011010110001001010101"))
#print(to_base("1010110001001010101010100100110101100010010101010101001001010100001010010101011011010110001001010101"))

sest = False
eee = 0
while sest:
    str1 = ""
    for i in range(100):
        str1 = str1 + str(random.randint(0,1))
    e = to_base(str1)
    e2 = away_base(e)
    if e2 == str1:
        print(eee)
    else:
        exit()
    eee += 1