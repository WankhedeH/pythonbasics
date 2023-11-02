#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Here I use for loop to itterate over a range, there I mentioneed the range in which I have to print
for i in range(1,11):
    #Here I use simply print function
    print(i)


# In[6]:


#Here I create a list
list1 = [1,4,5,43,67,8,3,2]
#Here I create a variable where I can store the value
sum_of_element = 0
#Here using for loop I itterate over a list
for i in list1:
    #Then I add all the element of list
    sum_of_element = sum_of_element+i
#Here I use simple print function    
print(sum_of_element)


# In[15]:


#Here I create a string
str1 = "Harshwardhan"
#Here I crate a empty variable
reversed_str = ""
#Here I use for loop in range to reversed the string
for i in range(len(str1) -1,-1,-1):
    #Here I concatenate the string and store it in a variable
    reversed_str = reversed_str + str1[i]
#Here I use simple print function    
print(reversed_str)


# In[39]:


#Here I defined a function called fact_num
def fact_num(num):
    #Here I gave if condion that if the number enter is 0 then return will be 1
    if num == 0 :
        return 1
    #If the 'If' condition is fail then else part will execute
    else:
        result = 1
        #Here I use for for to itterate over the range of number so that I can multiply them
        for i in range(1,num+1):
            #Here I multiply it and print the result
            result = result*i
        #Here I simply return the value    
        return result    


# In[43]:


#Here I call that function and I pass the value
fact_num(5)


# In[47]:


def multi_table(n1):
    for i in range(1,11):
        product=n1*i
        print(n1," ","*"," ",i," ","="," ",product)


# In[52]:


multi_table(10)


# In[69]:


#Here I declare 2 variable which will give me a count of even number and odd number
count = 0
count1 = 0
#Here I use for to itterate over a list
for i in list1:
    #Here I check the condition for even and increase the count by 1
    if i%2==0 :
        count += 1
    #If the number is not even then the number is odd
    else:
        count1 +=1
#Here I use print function to print the output        
print("Number of even number : ",count)    
print("Number of odd number : ",count1)


# In[74]:


#Here using for loop I itterate over a range from 1 to 5
for i in range(1,6):
    #Here I square the number
    square_of_num = i**2
    #Here I use simple print function
    print("The square of number ",i,":",square_of_num)


# In[82]:


#Here I create a empty variable
len_of_str = 0
#Here using for loop I itterate over a string
for i in str1:
    #Here I count the length of string
    len_of_str = len_of_str+1
#Here I use simple print function    
print("The length of string is",len_of_str)


# In[85]:


#Here I declared a variable called total
total = 0
#Here I use for loop to itterate over a list
for j in list1:
    #Here I calculate the total of a list
    total +=j
#Here I calculate the average of a list    
average_of_list = total/len(list1)
#Here I print the average of list numbers
print("the average of a list of numbers is ",average_of_list)


# In[90]:


#Here I defined a function for fibonacci series
def fibonacci(num2):
    #Here I create a variable
    x=0
    #Here I create another variable
    y=1
    #Here I print the first element of series
    print(x)
    #Here using for loop I itterate over range
    for i in range(1,num2):
        #Here I use print function to print the next element
        print(y)
        #Here I change the value everytime for next element
        x,y=y,y+x


# In[91]:


fibonacci(10)


# In[10]:


#Here I defined a function and pass a list
def duplicate(list2 = [2,3,4]):
    #Here I create a set stored it in a variable
    element_present = set()
    #Here using for loop I itterate over a list
    for k in list2:
        #Here I check the element and return 
        if k in element_present:
            return "List contain duplicate element"
        else:
            #Here I use add function to add elements in set, since set does not store duplicate
            element_present.add(k)
    return "List doesn't contain duplicate element"


# In[11]:


duplicate()


# In[33]:


#Here using for loop I itterate over a range
for num in range(1,11):
   # all prime numbers are greater than 1
   if num > 1:
        #Here using for loop I itterate over a range
       for i in range(2, num):
        #Here I check the condition for prime number
           if (num % i) == 0:
                #If yes the break the loop
               break
            #Else the else part will be executed
       else:
           print(num)


# In[4]:


#Here I created a string
str2 = "Harshwardhan"
#Here I declared a variable
count=0
#Here using for loop I itterate over a string
for k in str2:
    #Here I check if the string contain any vowels or not
    if k in "aeiouAEIOU":
        #Here I increment the value of count
        count +=1
#Here I use simple print function        
print(count)


# In[14]:


#Here I create a 2D list
list3 = [[1,2,3,4,5],[6,7,8,9,0]]
#Here I Initalize the maximum element in the list as a first element
max_element = list3[0][0]
#Here using for loop I itterate over a list as list contain 2 elements
for i in list3:
    #Here I itterate over the list in list and fetch the elemnts
    for j in i:
        #Here I check the element is greater than previous one
        if j > max_element:
            #Here I update everytime if the element is greater than previous one
            max_element = j
#Here I simply use print function            
print("The maxmimum element in the 2D list is ",max_element)


# In[5]:


#Here I create a list with some duplicate element
list4 = [32,53,6,7,7,8,9,7,5,6,5,4,2,3,4,5,6,7,8]
#Here I create a empty list
list5 = []
#Here I take the element to be removed
element_to_remove = 7
#Here using for loop I itterate over a list
for i in list4:
    #Here I gave a condition to if the element is not equal to the element then append it to a empty list
    if i!=element_to_remove:
        #Here I use simple append function
        list5.append(i)
#Here I use simple print function        
print(list5)        


# In[11]:


#Here I use nested for loop for creation of table
#Here in first for loop I itterate over a range that how many table I have to create
for i in range(1,6):
    #In second for loop I itterate over a range upto 10 so to create a table
    for j in range(1,11):
        #Here I use simple print function and printed the value of the table
        print(i, " " , "*" , " " , j , " ", "= ", i*j)


# In[15]:


#Here I create a list call fahrenheit and take the elements
fahrenheit = [32, 41, 50, 59, 68, 77, 86, 95]
#Here I create a empty list called celcius to store the elements 
celcius = []
#Here using for loop I itterate over a list of fahrenheit
for i in fahrenheit:
    #Here is the formula to convert the fahrenheit into celcius
    c = (i - 32) * 5 / 9
    #Here I append the elements which get converted
    celcius.append(c)
#Here I use simply print function    
print(celcius)


# In[18]:


#Here I create a list with some similar elements in another list
list6 = [2,3,4,5,6,7]
#Here I create a another list 
list7 = [5,6,7,8,9,0]
#Here I create a empty list
list8 = []
#Here using for loop I itterate over a list6
for i in list6:
    #Here I check if the same element is present in the list7
    if i in list7:
        #Here I append that element which is present in both the list
        list8.append(i)
#Here I use simple print function in list        
print(list8)        


# In[20]:


#Here I take number of rows for the triangle
n = 5
#Here I use for loop to iterate over the rows
for i in range(1, n+1):
    #Here I use simple print function to print the pattern
    print('*' * i)


# In[1]:


# Define a function to find the GCD of two numbers
def gcd(a, b):
  # Initialize the GCD variable to 1
  gcd = 1
  # Find the smaller of the two numbers
  smaller = min(a, b)
  # Loop from 1 to the smaller number
  for i in range(1, smaller + 1):
    # Check if both the numbers are divisible by i
    if a % i == 0 and b % i == 0:
      # Update the GCD variable with i
      gcd = i
  # Return the GCD value
  return gcd
# Test the function with some examples
print(gcd(12, 18))


# In[7]:


#Here I create a list of numbers
numbers = [345,6,76,7,86,9,96542,1,1,26,63,75]
#Here I defined a function that returns the sum of the digits of a number
def sum_digits(i):
    #Initialize the sum to zero
    s = 0
    #Loop through each digit of the number
    while i > 0:
        #Here I add the last digit to the sum
        s += i % 10
        #Here we have to remove the last digit from the number
        i //= 10
    #Here I simply return the sum
    return s
#Here using list comprehension to apply the function to each number in the list
sums = [sum_digits(i) for i in numbers]
#Here I use simple print function
print(sums)


# In[8]:


# Define a function to check if a number is prime
def is_prime(n):
    # Assume n is a positive integer
    if n == 1:
        return False # 1 is not prime
    if n == 2:
        return True # 2 is the only even prime
    if n % 2 == 0:
        return False # Even numbers are not prime
    # Check odd divisors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False # Found a divisor, not prime
    return True # No divisors found, prime
# Define a function to find the prime factors of a number
def prime_factors(n):
    # Assume n is a positive integer
    factors = [] # Initialize an empty list to store the factors
    # Check every number from 2 to n
    for i in range(2, n + 1):
        # If i is prime and divides n
        if is_prime(i) and n % i == 0:
            # Add i to the list of factors
            factors.append(i)
    return factors # Return the list of factors
# Use list comprehension to find the prime factors of numbers from 1 to 10
print([prime_factors(i) for i in range(1, 11)])


# In[3]:


#Here I create a list with some duplicate elements
my_list = [32,53,6,7,7,8,9,7,5,6,5,4,2,3,4,5,6,7,8]
#Here I Use a list comprehension to create a new list with only unique elements
#Set only store unique elements so I create a empty set
my_set = set()
#Here I use list comprehension
#Using for loop I itterate over a list then then check with set
new_list = [x for x in my_list if x not in my_set and not my_set.add(x)]
#Here I use simple Print function
print(new_list)


# In[6]:


#Here I take the limit
limit = 100
#Here I use list comprehension
#Using list comprehension I check if a number is equal to its reverse
palindromes = [n for n in range(1, limit + 1) if str(n) == str(n)[::-1]]
#Here I use Print function
print(palindromes)


# In[9]:


#Here I create a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
#Here I use list comprehension
#Here I flatten the nested list using list comprehension
flat_list = [element for i in nested_list for element in i]
#Here I use simple Print function
print(flat_list)


# In[ ]:




