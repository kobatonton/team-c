import re
import dic

def trans_word2(inputtext):
    #print('({})'.format('|'.join(map(re.escape, dic.replacements.keys()))))
    return re.sub('({})'.format('|'.join(map(re.escape, dic.replacements.keys()))), lambda m: dic.replacements[m.group()], inputtext)
               
text = input()
itext = text.lower()
intext = itext.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

print(trans_word2(intext))
