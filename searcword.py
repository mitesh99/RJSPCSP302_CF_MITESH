def searchword(filename,word):
    c=0
    with open (filename,'r') as read_obj:
        for line in read_obj:   
            c+=1
            if word in line:
                return "found the word at line "+str(c)



print(searchword('test.txt','Hello'))
