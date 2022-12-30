def power(base, exp)
  if base == 0:
  assert int(exp) == exp
    return 0
   elif exp<0:
    return 1/base * power(base,exp+1)
  return base * power(base,exp-1)

  
