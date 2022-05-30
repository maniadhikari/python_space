#program to open file and  change the line to seperate strings and sort them
#assignment from py4e.com
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
    word= line.rstrip().split()    
    for element in word:           
        if element in lst:        
            continue               
        else :                     
            lst.append(element)       
lst.sort()                         
print lst       
