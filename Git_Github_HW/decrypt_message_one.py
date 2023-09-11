cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

decipher2 = {}

for key, item in cipher.items():
    decipher2[item] = key


# Write code below
def decrypt(file):
    encrypted_file = open(file, 'r')

    encrypted_message = encrypted_file.readline()

    encrypted_file.close()
    message = ""
    for letter in encrypted_message:
        if letter in decipher2.keys():
            message += decipher2[letter]
    return message 

print(decrypt("./Git_Github_HW/encrypted_message_one.txt"))
