import codecs
f = codecs.open('out.txt', encoding='utf-8')

print(f.readline([0,0]))

# for line in f:
# 	print(line)
f.close()