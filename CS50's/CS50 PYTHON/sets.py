# create an empty set

s = set()

#add element to set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)  #still print{1,2,3,4}
s.remove(2)
print(s)


#len

print("the set has {len(s)}elements")