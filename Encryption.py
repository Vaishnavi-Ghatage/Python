import random
import string
str=input("Enter a sentence:")
if len(str)<=3:
    str=str[::-1]
    print(str)
else:
    l=list(str)
    l.append(l[0])
    l.remove(l[0])
    length = 3
    random_chars1 = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    random_chars2 = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    l=''.join(l)
    print("Encrypted String:")
    res=f"{random_chars1}{l}{random_chars2}"
    print(res)



res=res[3:-3]

a=res[-1]
res=res[:-1]
res=a+res
print("Decrypted string:")
print(res)


