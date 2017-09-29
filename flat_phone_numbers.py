__author__ = 'Aabir'



def flat_num():
	flats = ['A','B','C','D','E',]
	floors = ['1','2','3','4','5','6','7','8']
	total= []
	
	for floor in floors: 
		for flat in flats: 
			t = total.append(flat+floor)
	return total
		
def intercom(fnum):	
    interlist = []
    '''will create a list of all numbers'''
    for number in range(802, 842): 
        interlist.append(number)
	
    '''will create a dictionary of flat and numbers'''
    result = {}
    for i in range(40): 
        result.update({fnum[i] : interlist[i]})
    return result
         
    
			
			
def main():		
    flat_lebels = flat_num() 
    complete_list = intercom(flat_lebels)
    
    query = input('Enter flat number: ')
    print('The intercom number of your chosen flat is: {}'.format(complete_list[query]))
    
 
if __name__ == '__main__': 
	main()
