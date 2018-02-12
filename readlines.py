filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readline()
print(lines)

for i in range(0,len(lines)):
    print()
pi_string=''

for line in lines:
    pi_string += line.rstrip()
    print(len(pi_string))

print(pi_string)
