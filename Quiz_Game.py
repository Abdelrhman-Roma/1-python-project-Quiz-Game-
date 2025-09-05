def want_to_play():
    playing = input("Do you want to play?(yes/no)\n").lower()
    if playing == "no":
       print("good bye!!")
       quit()
    elif playing == "yes":
       print("Okay! let's play :)")    
    else:
       print("please enter yes or no only")
       want_to_play()
def quiz():
    count = 0
    questions = [
        ("What does 'CPU' stand for?", ["central processing unit"]),
        ("Which key is used to delete text from the right side of the cursor?", ["delete key", "delete"]),
        ("What is the brain of the computer called?", ["cpu"]),
        ("What does 'URL' stand for in internet terms?", ["uniform resource locator"]),
        ("Which device is used to input text into a computer?", ["keyboard"]),
        ("What is the full form of 'USB'?", ["universal serial bus"]),
        ("Which part of the computer is used to display output (text, images, videos)?", ["monitor"]),
        ("What is the storage device inside most computers called?", ["hdd", "ssd", "hard drive", "solid state drive"]),
        ("What does 'Wi-Fi' allow a computer to do?", ["connect to the internet wirelessly", "wireless internet"]),
        ("Which operating system is developed by Microsoft?", ["windows"])
    ]

    for question, right_answers in questions:
        answer = input(question + "\n").lower().strip()
        if answer in right_answers:
            print("Correct!")
            count += 1
        else:
            print("Incorrect!")
            print(f"The right answer is: {right_answers[0]}")
        print('-' * 50)

    return count
def grade(score):
   print("Now you finsh the Quiz".center(50))
   if score == 10:
      print(f"your grade is : {score}")
      print("very nice you are a Hero!!")
   elif score >5 and score < 10:
      print(f"your grade is : {score}")
      print("nice you can do more")
   elif score ==5:
      print(f"your grade is {score}")
      print("not bad but be carefully another time")
   else:
      print(f"your grade is {score}")
      print("very very bad please study will before the next exam")

print("Welcome to my computer Quiz!!")
want_to_play()
score = quiz()
grade(score)
