# check duplicate in a list

# method 1: by using 2 for loops

def check(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i] ==arr[j]):
                
                print("yes duplicate")
                break
    print("no duplicate")
nums =[1,2,3,4,5,6,6]
check(nums)

#method 2, 
def check(arr):
    a=[]
    for i in arr:
        if i in a :
            print("duplicate for ",i,"is there")
            return False
            
        else:
            a.append(i)
    return True
      
nums =[1,2,3,4,5,6,6,7,8,2]

print(check(nums))
