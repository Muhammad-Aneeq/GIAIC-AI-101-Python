# # # string method : 
# # # name = "pakistan"
# # # capatalize
# # # count
# # # index
# # # length
# # # find
# # # replace
# # # print(name.capitalize())
# # # name = "pakistan"

# # # print(name.count('a'))
# # # newName = 'my name is Aneeq and my nationality is pakistan'
# # # print(newName.find('is'))


# # # length  
# # # newName = 'my     name is Aneeq and my nationality is pakistan'
# # # name_count = len(newName)    # snake_case 
# # # print(name_count)



# # # replace :
# # new_name:str = 'my name is Aneeq and my nationality is pakistan'
# # # print(new_name.replace('pakistan','America'))

# # # index
# # # print(new_name.index('america'))
# # print(new_name.find('america'))

# # LIST 
# # my_list = ['Ali','Abdullah','Aamir']
# # append :
# # my_list.append('Asif')
# # print(my_list)


# # insert :
# # my_list.insert(-1,"Sabir")
# # print(my_list)
# # print(my_list[-1])

# # reverse
# # my_list.reverse()
# # print(my_list)

# # pop 
# # my_list.pop()
# # my_list.pop(0)
# # print(my_list)

# # extend 
# my_list = ['Asif','Ali','Aamir']
# new_list = ['Ali','Aneeq','Abdullah']
# my_list.extend(new_list)

# my_list.remove('Ali')
# print

# # sort :
# # num_list = [5,2,9,1,7]
# # num_list.reverse()
# # print(f"reverse list {num_list}")
# # num_list.sort(reverse=True)
# # print(f"sort list {num_list}")



student = {
    "name": "hasnain",
    "age": 22,
    "course": "agentic ai"
}

# print(student["salary"])
# print(student.get("salary", "value not found"))

# print(student.keys())

# for key in student.keys(): 
#   print(key)

# print(student.values())

# print(student.items())

# for item in student.items():
#     print(item)

#   destructuing
# for key,value in student.items():
#     print(f"key {key} and value {value}")


# student.update({"age": 24})

# print(student)

# student.clear()

# print(student)


# try except

num: int = 10
num2: int = 0


user_input = input("ENter your number")
# result = num / num2
# print(result)

# try:
#     result = num / num2
#     print(result)
# except Exception as e:
#     print(e)


#  Zero divison error
#  key error 
# index error
# value error
# import error

list = ["ali", "abdullah"]
try:
    result =  list[3]
    print(result)
except IndexError:
    print("this is error with index")      
except ZeroDivisionError:
    print("this is error for zero value")
  


# try:
#     result =  num / num2
#     print(result)
# except IndexError:
#     print("this is error with index")      
# except ZeroDivisionError:
#     print("this is error for zero value")