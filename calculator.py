1.  #......First Program
my_list=[1,2,2,4,4.5,6.8,10,13,22,35,52,83]
print(my_list)
new_list=[i for i in my_list if i>=10]
print(new_list)
user_input=int(input("hey user enter a number\n"))
new_list1=[i for i in my_list if i>=user_input]
print(new_list1)


output:
[1, 2, 2, 4, 4.5, 6.8, 10, 13, 22, 35, 52, 83]
[10, 13, 22, 35, 52, 83]
hey user enter a number
3
[4, 4.5, 6.8, 10, 13, 22, 35, 52, 83]

2.#....Second program on dictionaries......
employee={"name":"tim","age":30,"birthday":"1990-03-10","job":"Devops Engineer"}
dict1={"job":"Software Engineer"}
employee.update(dict1)
del employee['age']

for k in employee:
   print(k,':' ,employee[k])
   
output:
name : tim
birthday : 1990-03-10
job : Software Engineer

3. 3..........using dictionaries....... 
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}
]
print(type(employees))
for k in range (len(employees)):
      print("name", ':' , employees[k]["name"])
      print("job", ':', employees[k]["job"])
      print("city", ':', employees[k]["address"]["city"])
print(employees[1]["address"]["country"])

output:

name : Tina
job : DevOps Engineer
city : New York
name : Tim
job : Developer
city : Sydney
Australia   



4.#.............calculator Program............

def calculation(input1,input2):

       addition_of_num=input1+input2
       print(f"Addition of {input1} and {input2} is {addition_of_num}")
       sub_of_num=input1-input2
       print(f"Substraction of {input1} and {input2} is {sub_of_num}")
       mul_of_num=input1*input2
       print(f"Multiplication of {input1} and {input2} is {mul_of_num}")
       if(input2!=0):
           div_of_num=input1/input2
           print(f"Division of {input1} and {input2} is {div_of_num}")

       else:
           print("Division by zero is ivalid,please enter a valid value")



def validate_and_execution():
    try:
        user_input_value1=int(user_input1)
        user_input_value2=int(user_input2)
        calculation(user_input_value1,user_input_value2)
    except ValueError:
            print("you entered an invalid numbers,please enter valid numbers")

user_inputs="true"
count=0

while user_inputs=="true":


     user_input = input("Do u wnt to run the program!:")
     if user_input=="yes":
        user_input1=input("enter first number:")
        user_input2=input("enter second number:")
        count=count+1
        validate_and_execution()
     else:
          break

print(f"{count} times you are performed the calculations")
print("Thank You")


output:
Do u wnt to run the program!:yes
  enter first number:3
  enter second number:4
  Addition of 3 and 4 is 7
  Substraction of 3 and 4 is -1
  Multiplication of 3 and 4 is 12
  Division of 3 and 4 is 0.75
Do u wnt to run the program!:yes
  enter first number:siri
  enter second number:vara
  you entered an invalid numbers,please enter valid numbers
Do u wnt to run the program!:yes
  enter first number:2
  enter second number:0
  Addition of 2 and 0 is 2
  Substraction of 2 and 0 is 2
  Multiplication of 2 and 0 is 0
  Division by zero is ivalid,please enter a valid value
  
Do u wnt to run the program!:no
3 times you are performed the calculations
Thank You

helper module:

3......Finding of youngest employee

def operations_on_dict(data):
    for k in range(len(data)):
        print("name", ':', data[k]["name"])
        print("age", ':', data[k]["age"])
    min_age = min(data, key=lambda x: x['age'])
    print("the youngest employee is")
    print(min_age["name"], ':', min_age["age"])

#......finding of number of lower and upper letters
def count_of_lower_upper(input):
    upper=0
    lower=0
    for x in input:
         if x.isupper():
             upper=upper+1
         elif x.islower():
             lower=lower+1
         else:
             pass
    print(f"no of upper case letters in {input} are {upper}")
    print(f"no of upper case letters in {input} are {lower}")

#.............finding of even numbers

def cal_of_evenno(input):
    even_no=[i for i in input if i%2==0]
    print(f"the even no are {even_no} ")

#........main module.........      
    
import helper

#.........user input declarations and functions calling from helper module

employees = [{ "name": "Tina",  "age": 30},{"name": "Tim","age": 35},{"name":"siri","age":20}]
helper.operations_on_dict(employees)

user_input=input("enter a string:")
helper.count_of_lower_upper(user_input)

input_list=[1,2,5,6,56,98,36]
helper.cal_of_evenno(input_list)


output:
name : Tina
age : 30
name : Tim
age : 35
name : siri
age : 20
the youngest employee is
siri : 20
enter a string:SireeSha
no of upper case letters in SireeSha are 2
no of upper case letters in SireeSha are 6
the even no are [2, 6, 56, 98, 36]

6.#.........guessing number game...........
import random
def guessing_num():
  list = random.randint(1, 9)
  ran_num=list
  return ran_num

def result_of_game(ran_value,user_input):

  if ran_value==user_input:
    return "YOU WON!"


  elif ran_value>user_input:
     return "you are guessing too low!"

  elif ran_value<user_input:
     return "you are guessing too high"


ran_values=guessing_num()
user_input="true"
count=0

while user_input=="true":

     guess_number=int(input("guess a number between 1 to 9 range:"))
     final_result=result_of_game(ran_values,guess_number)
     if final_result=="YOU WON!":
         break
     else:
         print(final_result)


print(final_result)


output:
guess a number between 1 to 9 range:8
you are guessing too high
guess a number between 1 to 9 range:2
you are guessing too low!
guess a number between 1 to 9 range:4
you are guessing too low!
guess a number between 1 to 9 range:6
you are guessing too high
guess a number between 1 to 9 range:5
YOU WON!





















