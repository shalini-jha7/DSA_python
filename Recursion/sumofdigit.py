def sumofdig(n):
    assert int(n)==n
    if n==0:
        return 0
    return int(n%10) + sumofdig(int(n/10))
print(sumofdig(11))
