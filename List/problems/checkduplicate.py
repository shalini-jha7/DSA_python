# check duplicate in a list

def check(arr):
  for i,j in range(len(arr)):
    if arr[i] ==arr[j]:
      return True
    return False
  arr =[1,2,3,1]
  print(check)
