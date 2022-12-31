#  list is a data structure which holds an ordered collection of items
mixlist =[1,1.5,'spam']


#traversing the list
shoplist =['milk', 'cheese','butter']
for i in shoplist:
    print(i)
    
# updating a list 
shoplist[1]='tomato'
print(shoplist)
shoplist.insert(3,11)
print(shoplist)

# deleting elemets 
#1)by pop, pop removes just the last element if nothinh specified, O(1)
# print(shoplist.pop())
#2  by del , time complexity O(n)
# del shoplist[0:2]
# print(shoplist)

# remove , eeds to specify element
#shoplist.remove(1) ,time complexity O(n)
shoplist.remove(11)
print(shoplist)

# space complexity for all is O(n)
