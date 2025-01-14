# range function/method

numbers =  [1,2,3,4,5,6,7,8,9]
x = range(1,10)  # 1,2,3,4,5
# 1.starting point
# 2.condition
# 3.increment
# print(numbers)
# print(list(x))

#  aam zindagi
# num: int = 2 
# print("2 x 1 =", num * 1  )
# print("2 x 2 =", num * 2  )
# print("2 x 3 =", num * 3  )
# print("2 x 4 =", num * 4  )
# print("2 x 5 =", num * 5  )
# print("2 x 6 =", num * 6  )
# print("2 x 7 =", num * 7  )
# print("2 x 8 =", num * 8  )
# print("2 x 9 =", num * 9  )
# print("2 x 10 =", num * 10 )


# mintos zindagi
# for num in range(1,11): # 1,2,3,4,... ,10
#     print("2 x",num , "=", 2 * num)          # indentation
#     print(f"2 x {num} = {2 * num}") # fstring

#loops
# 1. for loop
# 2. while loop 


# num = 1
# num = num + 1
# print("num first time", num)
# num = num + 1
# print("num second time", num)
# print(num < 10)
# while num < 10:
#     print("number before increment", num)
#     # num = num + 1
#     print("number after increment", num)

# password: str = "python123"
# user_input: str = ""

# print("user_input != password is",user_input != password)
# while user_input != password: # user input wo baraber na ho password k 
#     print("incorrect password!")
#     user_input = input("Type your answer please!")


# string
# integer
# boolean
# list
# tuple

numbers = [1,2,3,4,5]
#         0   ,   1   ,  2    ,  3
names1 = ["Ali","Bilal","Hamza","Okasha"]  # list  mutable
#         0   ,   1   ,  2    ,  3
names2 = ("Ali", "Bilal", "Hamza", "Okasha") # tuple immutable
name: str  = "Ali"
name  = "Bilal"



#  list
# print("names1 before over write", names1)
# #  Bilal    =  "Abdullah"
# names1[1] = "Abdullah"
# print("names1 after over write", names1)


#  tuple
# print("names1 before over write", names2)
# #  Bilal    =  "Abdullah"
# names2[1] = "Abdullah"
# print("names1 after over write", names2)


# print("list first name is", names1[0])
# print("tuple first name is", names2[0])