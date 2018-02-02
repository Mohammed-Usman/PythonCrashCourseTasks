pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
count=0
while 'cat' in pets:
    count+=1
    pets.remove('cat')
print(count)
print(pets)