#in this file we'll merge names and surnames with zip function

#create name list
names = ["Jake","Oliver","Sasha","Melissa","Bethany","Ava"]

#create surname list
surnames = ["Joses","Davies","O'Ryan","Williams","Miller","Brown"]

for i,j in zip(names,surnames):
    print(i,j)