from collections import OrderedDict
od = OrderedDict()
for _ in range(int(input())):
    x = input()
    od[x]=od.get(x,0)+1
print (len(od))
print (" ".join(str(v) for k,v in od.items()))
