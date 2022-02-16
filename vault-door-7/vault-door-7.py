def get_flag(x):
    password = ""
    for i in x:
        c1 = i >> 24
        c2 = (i >> 16) & 0xff
        c3 = (i >> 8) & 0xff
        c4 = i & 0xff

        password += chr(c1) + chr(c2) + chr(c3) + chr(c4)
    
    return "picoctf{" + password + "}"


if __name__ == "__main__":
    x = [None] * 8
    x[0] = 1096770097
    x[1] = 1952395366
    x[2] = 1600270708
    x[3] = 1601398833
    x[4] = 1716808014
    x[5] = 1734293296
    x[6] = 842413104
    x[7] = 1684157793

    flag = get_flag(x)

    print(flag)