import random
import string
print("total no of parking spaces")
N = int(input())
print("total no of cars in parking lot")
M = int(input())
list1 = ["white","Blue","Black","Red"]
list2 = []
list4 = []
list3 = random.sample(range(1,N),M)
for I in range(M):
    list4.append(random.choice(list1))
    randomletter1 = random.choice(string.ascii_letters)
    randomletter2 = random.choice(string.ascii_letters)
    randomletter3 = random.choice(string.ascii_letters)
    randomletter4 = random.choice(string.ascii_letters)
    randomnum1 = random.randint(0,9)
    randomnum1 = str(randomnum1)
    randomnum2 = random.randint(0,9)
    randomnum2 = str(randomnum2)
    randomnum3 = random.randint(0,9)
    randomnum3 = str(randomnum3)
    randomnum4 = random.randint(0,9)
    randomnum4 = str(randomnum4)
    randomnum5 = random.randint(0,9)
    randomnum5 = str(randomnum5)
    randomnum6 = random.randint(0,9)
    randomnum6 = str(randomnum6)
    list2.append(randomletter1 + randomletter2 + "-" + randomnum1 + randomnum2 +"-"+ randomletter3 + randomletter4 +"-" + randomnum3 + randomnum4 + randomnum5+ randomnum6)
length =len(list2)
print('serialnumber | ' + 'registrationnumber | ' + "slotnumber")
for M in range(length):
    print(M,"          |",list2[M]," | ",list4[M]," | ",list3[M])
print("enter the slot no to veiw car details (or) to remove cardetails")
Slot = int(input())
A = list3.index(Slot)
print(list2[A])
print("enter the incoming car details in this format  hD-85-Ww-1765  |  Black ")
Details = input().split("|")
del list2[A]
del list3[A]
del list4[A]
for S in range(1,N+1):
    if S not in list3:
        list3.append(S)
        list2.append(Details[0].strip())
        list4.append(Details[1].strip())
        break
print('serialnumber | ' + 'registrationnumber | ' + "slotnumber")
for M in range(length):
    print(M,"          |",list2[M]," | ",list4[M]," | ",list3[M])
print("enter colour ")
color = input()
for J in range(len(list4)):
    if list4[J] == color:
        print(J,"          |",list2[J]," | ",list4[J]," | ",list3[J])
print("enter the slot number")
in1 = int(input())
A = list3.index(in1)
print("enter the car registeratoion number")
in2 = input()
if in2 == list2[A]:
    print("car is registerd at given slot")
else:
    print("car not registered at given slot")        
