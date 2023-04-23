b2tob64_N_B = {1:1,2:10,3:11,4:100,5:101,6:110,7:111,8:1000,9:1001,10:1010,11:1011,12:1100,13:1101,14:1110,15:1111,16:10000,17:10001,18:10010,19:10011,20:10100,21:10101,22:10110,23:10111,24:11000,25:11001,26:11010,27:11011,28:11100,29:11101,30:11110,31:11111,32:100000,33:100001,34:100010,35:100011,36:100100,37:100101,38:100110,39:100111,40:101000,41:101001,42:101010,43:101011,44:101100,45:101101,46:101110,47:101111,48:110000,49:110001,50:110010,51:110011,52:110100,53:110101,54:110110,55:110111,56:111000,57:111001,58:111010,59:111011,60:111100,61:111101,62:111110,63:111111, 0:0}
b2tob64_B_N = {v: k for k, v in b2tob64_N_B.items()}
b2tob64_N_A = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z",27:"a",28:"b",29:"c",30:"d",31:"e",32:"f",33:"g",34:"h",35:"i",36:"j",37:"k",38:"l",39:"m",40:"n",41:"o",42:"p",43:"q",44:"r",45:"s",46:"t",47:"u",48:"v",49:"w",50:"x",51:"y",52:"z",53:"0",54:"1",55:"2",56:"3",57:"4",58:"5",59:"6",60:"7",61:"8",62:"9",63:"-",0:"_"}
b2tob64_A_N = {v: k for k, v in b2tob64_N_A.items()}

b2tob64_A_S=  {1:"1",2:"10",3:"11",4:"100",5:"101",6:"110",7:"111",8:"1000",9:"1001",10:"1010",11:"1011",12:"1100",13:"1101",14:"1110",15:"1111",16:"10000",17:"10001",18:"10010",19:"10011",20:"10100",21:"10101",22:"10110",23:"10111",24:"11000",25:"11001",26:"11010",27:"11011",28:"11100",29:"11101",30:"11110",31:"11111",32:"100000",33:"100001",34:"100010",35:"100011",36:"100100",37:"100101",38:"100110",39:"100111",40:"101000",41:"101001",42:"101010",43:"101011",44:"101100",45:"101101",46:"101110",47:"101111",48:"110000",49:"110001",50:"110010",51:"110011",52:"110100",53:"110101",54:"110110",55:"110111",56:"111000",57:"111001",58:"111010",59:"111011",60:"111100",61:"111101",62:"111110",63:"111111"}

def b2tob64(new_num):
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
    
def b64tob2(str22):
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




#nowe = time.time()
#for i in range(1000000):
#    e12 = (new_new_to(test112))
#    #print(e12)
#    e13 = double_away_base(e12)
#nowe2 = time.time()
#print(nowe2-nowe)
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