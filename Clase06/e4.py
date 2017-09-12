fil = open('t1.txt', 'r')
dd = fil.readline()

while (len(dd) !=0):
   print dd
   dd = fil.readline()

fil.close()

print dd
print type(dd)
print len(dd)




