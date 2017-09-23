__author__ = 'Aabir'

a = [1,3,5,7,9,11,13, 15]
c = 0
for b in a: 
	c += 1 
#print(int(c))


middle = int(c/2) 
mid = a[middle]
#will go to the middle 
#element.
#print(mid) 

numin = int(input ('Enter a number:'))

if numin < mid and numin != mid: 
	newp = a[middle-1] 
	if numin < newp and numin != newp: 
		newp1 = a[newp-1]
		if numin < newp1 and numin != newp1:
			newp2 = a[new1-1]
			if numin < newp2 and numin != newp2:
				print ('Number not exists!')
				
elif numin > mid and numin != mid: 
	newp = a[middle+1] 
	if numin > newp and numin != newp: 
		newp1 = a[newp+1]
		if numin > newp1 and numin != newp1:
			newp2 = a[new1+1]
			if numin > newp2 and numin != newp2:
				print ('Number not exists')
else:
	print('The number exists!')	
