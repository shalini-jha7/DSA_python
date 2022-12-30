def deftobi(n):
  assert int(n) ==n
  if n ==0:
    return 0
  return n%2 + 10 *(deftobi(int(n/2)))

print(deftobi(5))
