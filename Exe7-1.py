l=[6,12,5,8,12,19,55,7]
if 5 in l:
	print('Yes')
else:
	print('No')
del l[0]
del l[-1]
l.sort()
print(l)