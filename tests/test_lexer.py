import os, re

files = os.listdir('lexer')

for f in files:
    if (re.search(r'^.+\.in$', f)):
        n = re.sub(r'\..*$', '.out', f)
        os.system ('D:/Homework/Compiler/compiler/Debug/compiler.exe D:/Homework/Compiler/tests/lexer/' + f + ' 1 > D:/Homework/Compiler/tests/lexer/' + n)

files1 = os.listdir('lexer')

i = 0
j = 0
for f in files1:
    if re.search(r'^.+\.out$', f):
        with open('lexer/' + f, 'r') as s1:
            n = re.sub(r'\..*$', '.sample', f)
            with open('lexer/' + n, 'r') as s2:
                i += 1
                if (s1.readlines() != s2.readlines()):
                    j += 1
                    print ('Check file ' + f)

print (str(i - j) + ' / ' + str(i) + ' tests passed')

input ('Press a key to continue\n')
