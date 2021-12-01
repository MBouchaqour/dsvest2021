import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#Improving code using set:
# set_result=set(names_1).intersection(set(names_2))
# duplicates=list(set_result)


#improing code using list
duplicates=[name for name in names_1 if name in names_2]



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
# Answer:
# What is the runtime complexity of this code?
#First runtime: 13.449148416519165 seconds
#Improving runtime: runtime: 0.012962579727172852 seconds
#
#Using list:
#Code improved abd we have now: runtime: 2.571621894836426 seconds

