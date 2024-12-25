# def bubble(lst):
    
#     n= len(lst)
#     for i in range(n):
#         for j in range(n-i-1):
#             if lst[j] > lst[j+1]:
#                 lst[j],lst[j+1] = lst[j+1],lst[j] 

#     return lst

# lst = [6,2,5,4,3,8,7,4]
# print(bubble(lst))

# def bubble_sort_string(s):
#     # Convert string to a list of characters
#     char_list = list(s)
    
#     # Bubble sort algorithm
#     n = len(char_list)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             print(char_list[j],char_list[j+1])
#             if char_list[j] > char_list[j+1]:
#                 # Swap characters if they are in the wrong order
#                 char_list[j], char_list[j+1] = char_list[j+1], char_list[j]
    
#     # Convert the sorted list of characters back to a string
#     return ''.join(char_list)

# # Example usage
# s = "hello"
# sorted_string = bubble_sort_string(s)
# print("Sorted string:", sorted_string)












# def bubble(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(n-i-1):
#             if lst[j] > lst[j+1]:
#                 lst[j],lst[j+1] = lst[j+1],lst[j]

#     return lst














def bubble(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

    return lst

lst = [6,2,5,4,3,8,7,4]
print(bubble(lst))