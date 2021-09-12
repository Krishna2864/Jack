playing = input("do you want to play").lower()
print(playing)

if playing != "yes" :
          quit()
else :
    print("okay let's play")
    answer = input("what CPU stand for").lower()
    score = 0
    if answer == "central processing unit":
        print("Correct")
        score +=1
    else:
        print("incorrect")

    answer = input("what does GPU stand for").lower()
    if answer == "graphic processing unit":
        print("Correct")
        score +=1
    else:
        print("incorrect")

    answer = input("wtat does RAM stand for").lower()
    if answer.lower == "random access memeory":
        print("Correct")
        score +=1
    else:
        print("incorrect")

    answer = input("wtat does JSON stand for").lower()
    if answer.lower == "javascript object notation":
        print("Correct")
        score +=1
    else:
        print("incorrect")
    if score == 4:
        print("congrats  your score is 4")
    if score == 3:
        print("good game played your score is 3")
    if score == 2:
        print("welltried, your score is 2")
    if score == 1:
        print("sorry your score is 1")
    if score == 0:
       print("sorry your score is 0")
