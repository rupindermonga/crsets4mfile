

f = open("numbers",'w')

for i in range(5):
    f.write('%d\n' %i)

f.close
f = open('numbers','r')
v = set(f)
print(v)
f.close