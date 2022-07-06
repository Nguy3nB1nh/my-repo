def stringcut(s):
    temps = []
    ret = []
    char = s[0]
    for i in s:
        if i == char:
            temps.append(i)
        else:
            ret.append(temps)
            temp = []
            temp.append(i)
            char = i
    return ret
print(stringcut("aaabbbccc"))
