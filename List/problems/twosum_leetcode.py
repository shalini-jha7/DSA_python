# to find integer pair whjich adds up to given target sum

def findsum(arr, target):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i] +arr[j] == target:
        print(arr[i],arr[j])
nums =[7,4,10,4,-1,5,6]
findsum(nums,8)
