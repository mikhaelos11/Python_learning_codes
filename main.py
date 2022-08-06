import random
from collections import defaultdict
lower_case = "abcdefghijklmnopqrtsuvwxyz"
upper_case = lower_case.upper()
numbers = "0123456789"
specials = "!@#$%^&*()"
i = 0
source = lower_case+upper_case+numbers+specials
passwd_length = int(input("Enter the wished length for your password: "))
x = int(input("Enter the wished number of choices"))
save = defaultdict(str)
f = open('passwords.txt', 'w')
while i < x:
    password = ''.join(random.sample(source, passwd_length))
    print("Your password is " + password)
    i += 1
    f.write(password)
    f.write("\n")
    save[i] = password
print(save)
f.close()
