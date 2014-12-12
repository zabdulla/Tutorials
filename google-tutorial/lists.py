colors=['red','blue','green']
b=colors
print "an = on lists does not make a copy!"
print colors
print b
b[2]='brown'
print colors
print b

for index,color in enumerate(colors):
  print index,color
