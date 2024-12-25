def chars(s,string,new = ''):
    if len(string) <=0 :
        return new
    if s != string[:1]:
        new += string[:1]
        print(f'chars{[s,string[1:],new]}')
        return chars(s,string[1:],new)
    else:
        return chars(s,string[1:],new)


print(chars('c','abcd'))