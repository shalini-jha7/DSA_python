#accessing element using index.
mytup =('a','b','c','d')
print(mytup[0])
# access using slicing
print(mytup[:3]) ## give elements from 0 index to 2
print(mytup[:]) ## give all elements

print(mytup[1:2])


# tuples are immutable 
List =[1,2,3]
Tuple =(1,2,3)

List[0]=4
print(List)
Tuple[0]=4 
# will throw TypeError: 'tuple' object does not support item assignment
Print(Tuple)
