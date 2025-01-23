#  data types
# 1. String
# 2. Integer
# 3. Boolean
# 4. list
# 5. tuple
# 6. Dictionary


# students = ["Ali", "Abdullah", "Amir"] 
# student = ["Name","01","Age", 20,"Class","Sunday 7-10"]
# student = {
#     "Name": "Ali",
#     "Age": 20,
#     "Class": "Sunday 7-10",
# }
# print("Before",student)
# student["RollNo"] = 9897

# print("After",student)


# def charger():
#     print("Charge Mobile")

# charger()

# def ramo_kaka(): 

#     print("hi")

#     return "Biryani Bangayi"




# plate = ramo_kaka()
# print(plate)

a = 1
b = 4

# Static Function

# def add():
#     return a+b
# sum = add()
# print(sum)

#Dynamic Function

#        parameter
# def greet(name,age,RollNo):

#     print("Assalam o Alekum Sir",name,"Your age is ",age,"roll no",RollNo, )

# #     argument
# greet("bilal",20,1234)


# version 1 Static Functions
# num1:int =10
# num2:int = 10
# def addition():
#     print(num1 + num2)


# addition()


# version 2 Dynamic Functions
#  Parameters 
# def addition(num1:int, num2: int): 
#     print(num1+num2)

# #       arguments
# addition(10,10)


# version 2 Dynamic Functions with return
def addition(num1: int, num2: int):
    return num1 + num2

# print(addition(10,10))  
# result  = 20 
result = addition(10,10) 
print(result)
# final_result = 20 + 20
final_result = result / 20
print(final_result)


