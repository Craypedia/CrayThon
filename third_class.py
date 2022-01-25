from email.errors import CloseBoundaryNotFoundDefect


# color_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
# # print(color_list.index("Red"))
# print("welocme to the astroverse")
# choice = input("Enter your favourite color:\n>")
# color_list.append(choice)
# print(color_list)
# position = (input("enter the position:\n>"))
# color_list.insert(position, choice)
# color_list.insert
# print(color_list)

# cleaned_data = choice.split()
# print(cleaned_data)
# cleaned_data.extend(color_list)
# print(color_list)


# li = [0, 2, 9, 8]
# b = li.pop(1)
# print(li.remove(9))

# a = [1, 5, 7, 2]
# b = a 
# c = a.copy()
# a.remove(5)
# print(b)
# print(c)


###tuple

# my_tuple = 1,2,3,4,5,6
# print(my_tuple)


# a = {1,2,4,6}
# b = {2,4,1,5}

# c = a.difference(b)
# b.intersection_update(a)
# print(c)
# c = a.symmetric_difference(b)



# eng = {1,2,3,4,5,6,7,8,9}
# fren = {10,1,2,3,11,21,55,6,8}
# c = eng.symmetric_difference(fren)
# ans = len(c)
# print(ans)

# english = input("Enter roll number for English students\n>")
# french = input("Enter roll numbers for frech students:\n>")
# english_list = english.split()
# french_list = french.split()

# english_set = set (english_list)
# french_set = set (french_list)
# total = english_set.symmetric_difference(french_set)
# print(len(total))


eng = {1,2,3,4,5,6,7,8,9}
fren = {10,1,2,3,11,21,55,6,8}
c = eng.union(fren)
ans = len(c)
print(ans)