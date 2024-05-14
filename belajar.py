t1 = 'a','b','c','d','e'
print(type(t1))

t3 = tuple("dutawacana")
t3 = ("b",) +t3[0:]
print(type(t3))
print(t3)

t4 = (0, 1, 2) < (0, 3, 4)
t5 = (0, 1, 2000000) < (0, 3, 4)
print(t4)
print(t5)

kalimat = 'but soft what light in yonder window breaks'
dafkata = kalimat.split()
t = list()
for kata in dafkata:
    t.append((len(kata), kata))

t.sort(reverse=True)
# t.sort(reverse=False)

urutan = list()
for length, kata in t:
    urutan.append(kata)
print(urutan)

m = [ 'have', 'fun' ]
x, y = m
x = m[0]
print(x)
print(y)

email = 'yohanes.nevan@ti.ukdw.ac.id'
username, domain = email.split('@')

print(username)
print(domain)

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)

d = {'a':10, 'b':1, 'c':22}
for key, val in list(d.items()):
    print(val, key)

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items() :
    l.append( (val, key) )


d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)

import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            
# urutkan dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)
    
last = 'nevan'
first = 'yohanes'
number = '71230989'
directory = dict()
directory[last, first] = number
for last, first in directory:
    print(first, last, directory[last,first])
