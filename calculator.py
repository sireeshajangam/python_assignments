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
        if((user_input_value1>=0)and(user_input_value2>=0)):
           calculation(user_input_value1,user_input_value2)
        elif((user_input_value1<=0)and(user_input_value2<=0)):
           calculation(user_input_value1, user_input_value2)
        elif((user_input_value1<=0)and(user_input_value2>=0)):
           calculation(user_input_value1, user_input_value2)
        else:
           calculation(user_input_value1, user_input_value2)
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

def operations_on_dict(data):
    for k in range(len(data)):
        print("name", ':', data[k]["name"])
        print("age", ':', data[k]["age"])
    min_age = min(data, key=lambda x: x['age'])
    print("the youngest employee is")
    print(min_age["name"], ':', min_age["age"])


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

def cal_of_evenno(input):
    even_no=[i for i in input if i%2==0]
    print(f"the even no are {even_no} ")

3........main module.........      
    
import helper

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















