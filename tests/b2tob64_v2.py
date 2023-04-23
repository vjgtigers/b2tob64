import time

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
            eeeee = len(arr)
            arrayF.append(arr)
            arr = []
            arr.append(eeeee)
            arrayF.append(str(arr))
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
    lenarrF = len(arrayF)
    count = 0
    for i in arrayF:
        if count != (lenarrF - 2):
            num = int(''.join(i))
            num2 = b2tob64_B_N[num]
            char = b2tob64_N_A[num2]
            str22 += char
            count += 1
        else:
            str1 = (''.join(i))
            zeroes = (str1+'1').index('1')
            if "1" not in str1:
                print("no ones in string")
                zeroes = zeroes - 1
            str1 = int(str1)
            num2 = b2tob64_B_N[str1]
            char = b2tob64_N_A[num2]
            str22 += char
            zeroes = b2tob64_N_B[zeroes]
            num2 = b2tob64_B_N[zeroes]
            char = b2tob64_N_A[num2]
            str22 += char
            break
    return str22
    
def double_away_base(str22):
    back_to = []
    back_to[:0] = str22
    str33 = ""
    back_len = len(back_to)
    counter = 1
    for i in back_to:
        num = b2tob64_A_N[i]
        num2 = b2tob64_N_B[num]
        better = str(num2)
        #print(better)
        e1 = "0"
        e2 = "00"
        e3 = "000"
        e4 = "0000"
        e5 = "00000"
        if counter == back_len-1:
            last = str22[-1]
            #break
            if last == "_":
                str33 = str33 + better
                break
            if last == "A":
                better = e1 + better
                str33 = str33 + better
                break
            if last == "B":
                better = e2 + better
                str33 = str33 + better
                break
            if last == "C":
                better = e3 + better
                str33 = str33 + better
                break
            if last == "D":
                better = e4 + better
                str33 = str33 + better
                break
            if last == "E":
                better = e5 + better
                str33 = str33 + better
                break
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





test1 = "101011000100101010101010010011010110001001010101010100100101010000101001010101101101011000100101010101010010010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101010110101001011001010000010001010101011010101010101011010100110100101010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101"
test11 = "10101100010010101010101001001101011000100101010101010010010101000010100101010110110101100010010101010101001001010100001010010101011010101101010010110010100000100010101010110101010101010110101001101001010101011010100101100101000001000101010101101010101010101101010011010010101010100001010010101011010101101010010110010100000100010101010110101010101010110101001101001000000"
test2 = "101011000100101010101010010011010110001001010101010100100101010000101001010101101101011000100101010101010010010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101010110101001011001010000010001010101011010101010101011010100110100101010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010000010"
test3 = "101011000100101010101010010011010110001001010101010100100101010000101001010101101101011000100101010101010010010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010101010110101001011001010000010001010101011010101010101011010100110100101010101000010100101010110101011010100101100101000001000101010101101010101010101101010011010010000101"
test111 = "0010011000111001010110001011101010001101011010110111111010010111111000010010000101110011111011011011101011110101000001011001100000100001"
test112 = "101010000101100001101100101000001000001000000001"
nowe = time.time()
for i in range(1000000):
    e12 = (new_new_to(test112))
    #print(e12)
    e13 = double_away_base(e12)
nowe2 = time.time()
print(nowe2-nowe)
#print(e13)
#if test112 == e13:
#    print("equal")
#print(test112)
#print(e13)
#e= (new_to(test1))
#test2 = new_away_base(e)
#print(test2)
#if test2 == test1: 
#    print("worked")
#else:
#    print("failed")
#print(new_to("1010110001001010101010100100110101100010010101010101001001010100001010010101011011010110001001010101"))
#print(to_base("1010110001001010101010100100110101100010010101010101001001010100001010010101011011010110001001010101"))
new_test = False
eee = 0
while new_test:
    strlen2 = random.randint(1,66)
    str1 = ""
    for i in range(strlen2):
        str1 = str1 + str(random.randint(0,1))
    e = new_new_to(str1)
    e2 = double_away_base(e)
    if e2 == str1:
        print(eee)
        print("in1: " + str1)
        print("out: " + e2)
    else:
        print(str1)
        print(e2)
        print("not equal")
        exit()
    eee += 1


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