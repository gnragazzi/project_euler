import sys

f = open("13_aux.txt","r")
a = []

for line in f:
    a.append(int(line))

sum = 0

for n in a:
    sum += n

res = str(sum)[:int(sys.argv[1])]
print(res)
