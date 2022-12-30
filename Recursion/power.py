def power(base, exp):
  if exp == 0:
    return 1
  elif exp<0:
    return 1/base * power(base,exp+1)
  elif exp ==1:
    return(base)
  return base * power(base,exp-1)
  
print(power(8,-1))
  
