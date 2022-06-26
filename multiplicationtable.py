# In this file we're create a multiplication table.

for i in range(1,11):
    print("_______________")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))