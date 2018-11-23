import random
#A1
users = ["Bob","Tom","Ken"]
#A2
int_numbers = [1,2,3,4,5]
#A3
#kazuma_info = ["Kazuma","Takahashi",35]
#A4
members = ["Kazuma", "Makoto", "Ohira"]
#A6
odd_numbers = [1, 3, 5, 7, 9]
#A7
even_numbers = [2, 4, 6, 8]

#A8
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]
#A9
kazuma_info = {"first_name":"Kazuma","family_name":"Takahashi","age":35}

#A10
def dice():
    result = random.randint(1,6)
    print(result)


print("####################")
#A4
print(members[1])
print(members[0])
print("####################")
#A5
#print(f"Name:{kazuma_info[1]} {kazuma_info[0]},Age:{kazuma_info[2]}")

print("####################")
#A6
for odd_number in odd_numbers:
    print(odd_number)

print("####################")
#A7
for even_number in even_numbers:
    print(even_number * 2)

print("####################")
#A8
for user_info in users_info:
    print(f"Name: {user_info[0]}, Age:{user_info[1]}")

print("####################")
#A9
print(kazuma_info["first_name"])
print(kazuma_info["family_name"])
print(kazuma_info["age"])

print("####################")
#A10
dice()




