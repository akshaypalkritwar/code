lis = [7, 845, 69, 60]
p = []

for i in lis:
	x = list(str(i))
	p.extend(x)
p.sort()
p = "".join(p)
print(int(p))
