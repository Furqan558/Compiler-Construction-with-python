lis = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Expected Output : ['Green', 'White', 'Black']

for i in range(len(lis)):
    if i == 0 or i == 4 or i == 5:
        lis.pop()
print(lis)
