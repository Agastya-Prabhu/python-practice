# #Linear Search
# nums = [1,2,3,4,5]

# x = int(input("#: "))


# y = True
# for n in nums:
#     if x == n:
#         print("Number Found")
#         y = False
#         break
# if y:
#     print("Not Found")


# #Binary Search

# nums = [11,35,67,41,24,50,71]

# x = int(input("#: "))

# nums.sort()

# #1,2,3,4,5,6,7

# start_index = 0
# end_index = len(nums)-1
# mid_index = (start_index + end_index)//2
# flag = True

# while True:
#     mid_index = (start_index + end_index)//2
#     if x > nums[mid_index]:
#         print("Number lies in the 2nd half.")
#         start_index = mid_index + 1
#     if x < nums[mid_index]:
#         print("Number lies in the 1st half.")
#         end_index = mid_index - 1
#     if x == nums[mid_index]:
#         flag = False
#         print("Found.")
#         break
#     if x > nums[end_index] or x < nums[start_index]:
#         flag = True
#         break
        
# if flag:
#     print("Not found.")


#Sorting Algorithims

#1st Algorithim: Bubble Sort

# list = [5,4,3,5,2,1]

# for y in range(0,len(list) - 1,1):
#     for n in range(0,len(list) - 1,1):
#         x = n + 1
#         if list[n] > list[x]:
#             list[n],list[x] = list[x],list[n]

# print(list)

# 2nd Algorithim: Selection Sort

# L = [29,30,10,14,5,12,13,17,33,40]

# for n in range(0,len(L),1):

#     min_index = n

#     for x in range(min_index,len(L),1):
#         if L[min_index] > L[x]:
#             min_index = x

#     L[n],L[min_index] = L[min_index],L[n]

# print(L)

# L = [29,30,10,14,5,12,13,17,33,40]

# min_num = L[0]
# min_index = 0

# for n in range(0, len(L), 1):

#     if min_num > L[n]:
#         min_num = L[n]
#         min_index = n
# print(min_index)


# 3rd Algorithim: Insertion Sort

# L = [29,30,10,14,5,12,13,17,33,40]

# for n in range(len(L)):
#     x = n + 1
#     if x > (len(L) - 1):
#         break
#     y = x - 1
#     while True:
#         if y >= 0:
#             if L[x] > L[y]:
#                 break
#             else:
#                 z = L.pop(x)
#                 L.insert(y,z)
#                 print(L)
#         else:
#             break
    
# print(L)

# 3rd Algorithim: Insertion Sort

# L = [29,30,10,14,5,12,13,17,33,40]

# for n in range(1,len(L),1):
#     key = L[n]
#     prev = n - 1
#     while key < L[prev] and prev >= 0: #this while loop is used to shift all the numbers greater than the current element one position foreward. 
#         L[prev + 1] = L[prev]
#         prev -= 1
#     L[prev + 1] = key
# print(L)

# x = int(input("Give me a number: "))

# product = 1
# for n in range(x,0,-1):
#     product = product * n
# print(product)

#Recursion

# def factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * factorial(num-1)
# x = factorial(5)
# print(x)
    
# def quart_to_dolla(quarts):
#     dollars = quarts/4
#     return dollars

# x = quart_to_dolla(8)
# y = quart_to_dolla(12)

# print(x + y)

# def sum_to_floor(num):
#     if num == 1:
#         return num
#     else:
#         return num + sum_to_floor(num - 1)

# x = sum_to_floor(100)
# print(x)
