def binarySearch(key,items):
    min=0
    max=len(items)
    found=False
    i=0
    while min<max:
        i+=1
        print(i)
        avarage=int((max+min)/2)

        if(items[avarage]==key):
            found=True
            break
        elif(items[avarage]<key):
            min=avarage+1
        elif(items[avarage]>key):
            max=avarage-1
    return found


print(binarySearch(29,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))

 