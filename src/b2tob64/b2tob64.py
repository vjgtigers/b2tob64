b2tob64_B_A2 = {"000000":"_", "000001":"A", "000010":"B", "000011":"C", "000100":"D", "000101":"E", "000110":"F", "000111":"G", "001000":"H", "001001":"I", "001010":"J", "001011":"K", "001100":"L", "001101":"M", "001110":"N", "001111":"O", "010000":"P", "010001":"Q", "010010":"R", "010011":"S", "010100":"T", "010101":"U", "010110":"V", "010111":"W", "011000":"X", "011001":"Y", "011010":"Z", "011011":"a", "011100":"b", "011101":"c", "011110":"d", "011111":"e", "100000":"f", "100001":"g", "100010":"h", "100011":"i", "100100":"j", "100101":"k", "100110":"l", "100111":"m", "101000":"n", "101001":"o", "101010":"p", "101011":"q", "101100":"r", "101101":"s", "101110":"t", "101111":"u", "110000":"v", "110001":"w", "110010":"x", "110011":"y", "110100":"z", "110101":"0", "110110":"1", "110111":"2", "111000":"3", "111001":"4", "111010":"5", "111011":"6", "111100":"7", "111101":"8", "111110":"9", "111111":"-"}
b2tob64_A_B2 = {v: k for k, v in b2tob64_B_A2.items()}
b2tob64_short = {1:"_", 2:"A", 3:"B", 4:"C", 5:"D"}
b2tob64_short_flip = {v: k for k, v in b2tob64_short.items()}




def b2tob64(j):
    j_rem = len(j) % 6
    j_b = j[-j_rem:]
    str_list = []
    for i in range(int(len(j)/6)):
        str_list.append(b2tob64_B_A2[(j[i * 6:(i * 6) + 6])])
    match j_rem:
        case 1: str_list.append((b2tob64_B_A2["00000" + j_b] + "_"))
        case 2: str_list.append((b2tob64_B_A2["0000" + j_b] + "A"))
        case 3: str_list.append((b2tob64_B_A2["000" + j_b] + "B"))
        case 4: str_list.append((b2tob64_B_A2["00" + j_b] + "C"))
        case 5: str_list.append((b2tob64_B_A2["0" + j_b] + "D"))
        case 0: str_list.append("E")
    return ''.join(str_list)

def b64tob2(str1):
    str_list = []
    st_len = len(str1)
    if str1[-1:] == "E":
        for i in range(st_len - 1):
            str_list.append(b2tob64_A_B2[str1[i]])
    else:
        for i in range(st_len - 2):
            str_list.append(b2tob64_A_B2[str1[i]])
        str_list.append(b2tob64_A_B2[str1[st_len - 2]][-b2tob64_short_flip[str1[-1]]:])
    return ''.join(str_list)

