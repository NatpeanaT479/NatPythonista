# Write your in_range function here:
def in_range(num,lower,upper):
  if num >= lower and num <=upper:
    return True 
  return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

#since our if statement will return True and exit the function if the condition is true, 
# the last line will only be reached if the condition was false.



# Write your same_name function here:
def same_name(your_name,my_name):
  #if your_name == my_name:
   # return True
  #return False
  return True if your_name == my_name else False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

# Write your always_false function here. This is to create contradiction.
def always_false(num):
  if num > 0 and num < 0:
    return True
  else: 
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False


#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#Write your function here
def append_sum(lst):
  for i in lst:
    for k in range(3):
      lst.append(lst[-1] + lst[-2])
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


# use range to add to x 8 times
x=0
for x in range(8):
	x +=1
print(x)



def delete_starting_evens(lst):
  while(len(lst) > 0 and lst[0]%2 == 0):
    lst = lst[1:]
  return lst

#use a while loop to keep iterating as long as some provided conditions are true
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


#Find the indices in two equally sized lists where the numbers match
def same_values(lst1,lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#len(lst) is 5 so range(5) is 0,1,2,3,4. These numbers can use as index for given list. Remember this.

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#To test two lists to see if the second list is the reverse of the first list
def reversed_list(lst1,lst2):
    for index in range(len(lst1)):
      if lst1[index] != lst2[len(lst2)- 1-index]:
        return False
    return True
      
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


# To replicate len() function
def get_length(word):
  num_w = 0
  for w in word:
    num_w += 1
  return num_w

#The function should return a list of the indices where the values were equal in lst1 and lst2.
def same_values(lst1,lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

def contains(big_string,little_string):
  return little_string in big_string

 #To create a function called common_letters that takes two arguments, string_one and string_two
 # then returns a list with all of the letters they have in common.
#The letters in the returned list should be unique.

def common_letters(string_one,string_two):
  com_letter =[]
  for index in range(len(string_one)):
    if string_one[index] in string_two and not string_one[index] in com_letter:
      com_letter.append(string_one[index])
  return com_letter

# How to combine element of same indices from two lists:
for i in range(len(prices)):
  pizza_and_prices.append([prices[i], toppings[i]])


#the function to take the input user name and shift all of the letters by one to the right, 
# so the last letter of the username ends up as the first letter and so forth. 
# For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.

def password_generator(username):
  password =""
  for name in range(len(username)):
    password = username[-1] + username[:-1]
    return password