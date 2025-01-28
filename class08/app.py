# Default Parameter

def box(a, b=3):
    return a+b

sum = box(2)
print(sum)

def func(a,b):
    a+b

c = func(2,3)

print(c)

#STRING METHODS

name = "pakistan"

print(type(name))


print(name.capitalize())
print(name.count('a'))
print(name)
new_str = "my name is sami. my nationality is pakistani."

print(new_str.count('my'))
print(len(new_str))
print(new_str.find('my'))
print(new_str.index('my'))
print(new_str.replace("pakistani","american").upper())

#LIST METHODS
#append,reverse,sort,insert,remove,pop,extend

my_list = ["Aneeq","Sami","Sohaib","Aisha","Hifza"]


# # append :
my_list.append('Ameen Alam')
print(my_list)

# # insert :
my_list.insert(1,'Sir Zia')
print(my_list)


# reverse
my_list.reverse()
print(my_list)


# pop
print(my_list)
print(my_list.pop(2))

print(my_list)


# remove :
my_list.remove('Sohaib')
print(my_list)



# sort :
my_list.sort(reverse=True)
print(my_list)



# extend :
new_faculty = ['Abdullah','Ghous']
print("Old list ", my_list)
my_list.extend(new_faculty)

print("Updated list ", my_list)




# Dictionary :

my_dict = {
    "name" : "John",
    "age" : 25,
    "city" : "Karachi"
}


# #  dictionary Methods 


# # get() 
# # keys()
# # values()
# # item()
# # update()
# # clear()
# # pop()

# keys :
print(my_dict.keys())


# values : 
print(my_dict.values())


# items:
print(my_dict.items())




# get :
print(my_dict.get("name"))


# # update : 
new_dict = {"city" : "Islamabad"}
new_dict2={"country":"Pakistan"}
my_dict.update(new_dict)
my_dict.update(new_dict2)
print(my_dict)

# pop :
print(my_dict.pop('city'))
print(my_dict)


# clear :
my_dict.clear()
print(my_dict)


# next class homework :
#remaining methods of string,list and dictionary
# tuple methods 
