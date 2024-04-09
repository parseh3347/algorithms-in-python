def encrypt(string,key):
    alpha = "abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_-+=?><ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result

print(encrypt('amir_big',35))

def decrypt(string,key):
    key *=-1
    return encrypt(string,key)
    
print(decrypt('(D<Ic)<?',35))

def brute_force(string):
    alpha = "abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_-+=?><ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = 1
    result = ''
    brute_force_data = {}

    while key <= len(alpha):
        result = decrypt(string, key)
        brute_force_data[key]=result
        key += 1
        result = ''
    return brute_force_data


print(brute_force('(D<Ic)<?'))


