def ecode(str='amir_'):
    return [ord(i)+522 for i in str]
print(ecode())

def decode(l:list):
    l=ecode()
    print(l)
    return ''.join(chr(i-522) for i in l)
print(decode)
