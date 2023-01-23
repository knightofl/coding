s1 = {'a','c','e','b','d','f',1}
s2 = {1,2,3,'b','d','f'}

s3 = set("BOYS, BE AMBITIOUS".lower())
print(s3)

print(s1 & s2 & s3)
print(s1 | s2 | s3)
print(s3 - s2 - s1)

s1.update('gh')
print(s1)

s2.update('A')
print(s2)
