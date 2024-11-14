
quiz=input("Are you interested to join this Quiz :")
if quiz.lower() != 'yes':
    quit()
name=input("Enter Your full name :")
print('Full marks 10. Each question carries 1 mark.')
print("""

        ========= Quiz =========
""")
score=0
answer=input("What is the full form of 'www' ? ")
if answer.lower()=='world wide web':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer .......  Correct Answer is 'world wide web'" )

answer=input("CPU stands for __________________ ")
if answer.lower() =='central processing unit':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'central processing unit'")

answer=input("What is the full form of 'HTML' ? ")
if answer.lower() =='hyper text markup language':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer Wrong Answer ......... Correct Answer is 'hyper text markup language'")
answer=input(" 'Mouse is an input device' - True or False ? ")
if answer.lower() =='true':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'true'")
answer=input(" GPU stands for _____________________")
if answer.lower()=='graphics processing unit':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'graphics processing unit'")
answer=input("What is the full form of 'HTTPS' ")
if answer.lower()=='hyper text transfer protocol':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'hyper text transfer protocol'")
answer=input("'ISP' Stands for______________________")
if answer.lower()=='internet service provider':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'internet service provider'")
answer=input(" 'Webcam is an output device' - True or False ?")
if answer.lower()=='false':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'False'")

answer=input("'RAM' Stands for______________________")
if answer.lower()=='ramdom access memory':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'Random access memory'")

answer=input(" 'ATM' full form _____________")
if answer.lower()=='automatted tellor machine':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer ......... Correct Answer is 'Automatted tellor machine'")


print('Dear',name,'You obtained '+ str(score) +' Marks out of 10')
n=(score/10)*100
if(n<40):
    print("You are Fail ")
elif(n>=40 and n<50):
    print("Your grade is Third Division")
elif(n>=50 and n<60):
    print("Your grade is Second Division")
elif(n>=60 and n<75):
    print("Your grade is First Division")
elif(n>=75 and n<80):
    print("Congratulation!! Star Mark")
elif(n>=80 and n<90):
    print("Congratulation!!  Letter")
elif(n>=90 and n<=100):
    print("Congratulation!!  utstanding")
else:
    print("Invalid Input")




