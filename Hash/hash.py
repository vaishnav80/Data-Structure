# class Hashtable:

#     def __init__(self,size):
#         self.size = size
#         self.table =[[]for _ in range(size)]

#     def hashfunction(self,k):
#         return (k%self.size)
    
#     def insert(self, key):
#         i = self.hashfunction(key)
#         self.table[i].append(key)

#     # def insert(self, key):
#     #     i = self.hashfunction(key)
#     #     # Check if the key already exists in the bucket (list at index i)
#     #     for pair in self.table[i]:
#     #         # print(pair,'dfkjdgf')
#     #         if pair[0] == key:
#     #             pair[1] += 1  # Increment the count if the key exists
#     #             return
#     #     # If the key doesn't exist, append it to the bucket with a count of 1
#     #     self.table[i].append([key, 1]) 
    
#     def display(self):
#         for i in self.table:
#             print(i,end="")

#     def search(self,key):
#         i = self.hashfunction(key)
#         if key in self.table[i]:
#             print()
#             print("the data is found",key)
#         else:
#             print("not found")

#     def delete(self,key):
#         i = self.hashfunction(key)
#         if key in self.table[i]:
#             self.table[i].remove(key)
    
#     # def find_duplicates(self):
#     #     duplicates = []
#     #     # Iterate through the entire table to find keys with count > 1
#     #     for bucket in self.table:
#     #         for pair in bucket:
#     #             if pair[1] > 1:  # If the count is greater than 1, it's a duplicate
#     #                 duplicates.append(pair[0])
#     #     return duplicates


# obj = Hashtable(10)
# lst = [1,20,5,6,6,18,8,9,4,2]
# for i in lst:
#     obj.insert(i)

# obj.display()

# obj.search(6)
# obj.delete(5)
# # obj.display()
# # print(obj.find_duplicates())



# class hash_table:
#     def __init__(self,size):
#         self.size = size
#         self.hash = [[] for _ in range(size)]

#     def hashfunction(self,key):
#         return (key%self.size)
    
#     def insert(self,key,data):
#         i = self.hashfunction(key)
#         self.hash[i] = data

#     def search(self,key):
#         i = self.hashfunction(key)
#         print(self.hash[i])

#     def delete(self,key):
#         i = self.hashfunction(key)
#         self.hash[i] = []
#         print(self.hash)

#     def display(self):
#         print(self.hash)

    # def insert(self, key):
    #     i = self.hashfunction(key)
    #     # Check if the key already exists in the bucket (list at index i)
    #     for pair in self.table[i]:
    #         # print(pair,'dfkjdgf')
    #         if pair[0] == key:
    #             pair[1] += 1  # Increment the count if the key exists
    #             return
    #     # If the key doesn't exist, append it to the bucket with a count of 1
    #     self.table[i].append([key, 1]) 

# obj = hash_table(10)
# obj.insert(5)
# obj.insert(3)
# obj.display()
# obj.search(5)
# obj.delete(5)


class Hash:
    def __init__(self,size):
        self.size = size
        self.hash = [[] for _ in range(size)]

    def hashfunction(self,key):
        return (key%self.size)
    
    def insert(self,key,data):
        index = self.hashfunction(key)
        self.hash[index].append(data)

    def display(self):
        for i in self.hash:
            print(i)

obj = Hash(5)
obj.insert(3,8)
obj.insert(3,5)
obj.insert(9,4)
obj.display()