import random
ran = random.randint(1,9)
if ran == 1 :
    ques= "taylor swift"
    sol_1 ="boyfriend"
    sol_2 ="age"
    sol_3 ="net worth"
    sol_4 = "height"
    sol_5 ="birthday"
elif ran == 2:
    ques= "BGMI"
    sol_1 ="launch date in india"
    sol_2 ="apk"
    sol_3 ="apk download"
    sol_4 ="lite" 
    sol_5 ="redeem code"
elif ran == 3:
    ques= "Mousse"
    sol_1 ="foundation"
    sol_2 ="cake"
    sol_3 ="chocolate"
    sol_4 ="pronounciation" 
    sol_5 ="meaning"
elif ran == 4:
    ques= "The song of "
    sol_1 ="Achilles"
    sol_2 ="Ice and Fire"
    sol_3 ="Scorpians"
    sol_4 ="India written by" 
    sol_5 ="Glory"
elif ran == 5:
    ques= "height"
    sol_1 ="of taj mahal"
    sol_2 ="in feet"
    sol_3 ="kaise bhadaye"
    sol_4 ="of mount everest" 
    sol_5 ="in cm"
elif ran == 6:
    ques= "Most searched"
    sol_1 ="person on google"
    sol_2 ="topic on google"
    sol_3 ="topic on youtube"
    sol_4 ="things on google" 
    sol_5 ="on google today"
elif ran == 7:
    ques= "what is"
    sol_1 ="my ip"
    sol_2 ="computer"
    sol_3 ="internet"
    sol_4 ="cryptocurency" 
    sol_5 ="today"
elif ran == 8:
    ques= "how to resister "
    sol_1 ="for booster dose"
    sol_2 ="for vaccination"
    sol_3 ="for covid vaccine"
    sol_4 ="mobile number in SBI" 
    sol_5 ="for free laptop in UP"
else :
    ques = "When is" 
    sol_1 ="Diwali"
    sol_2 ="Pongal"
    sol_3 ="Makar Sankranti"
    sol_4 = "Halloween"
    sol_5 ="Holi"

ran2 = random.randint(1,9)

if ran2 == 1 :
    ques_2= "taylor swift"
    sol_2_1 ="boyfriend"
    sol_2_2 ="age"
    sol_2_3 ="net worth"
    sol_2_4 = "height"
    sol_2_5 ="birthday"
elif ran2 == 2:
    ques_2= "The song of "
    sol_2_1 ="Achilles"
    sol_2_2 ="Ice and Fire"
    sol_2_3 ="Scorpians"
    sol_2_4 ="India written by" 
    sol_2_5 ="Glory"
elif ran2 == 3:
    ques_2= "The song of "
    sol_2_1 ="Achilles"
    sol_2_2 ="Ice and Fire"
    sol_2_3 ="Scorpians"
    sol_2_4 ="India written by" 
    sol_2_5 ="Glory"    
elif ran2 == 4:
    ques_2= "The song of "
    sol_2_1 ="Achilles"
    sol_2_2 ="Ice and Fire"
    sol_2_3 ="Scorpians"
    sol_2_4 ="India written by" 
    sol_2_5 ="Glory"
elif ran2 == 5:
    ques_2= "The song of "
    sol_2_1 ="Achilles"
    sol_2_2 ="Ice and Fire"
    sol_2_3 ="Scorpians"
    sol_2_4 ="India written by" 
    sol_2_5 ="Glory"
elif ran2 == 6:
    ques_2= "The song of "
    sol_2_1 ="Achilles"
    sol_2_2 ="Ice and Fire"
    sol_2_3 ="Scorpians"
    sol_2_4 ="India written by" 
    sol_2_5 ="Glory"
elif ran2 == 7:
    ques_2= "The song of "
    sol_2_1 ="Achilles"
    sol_2_2 ="Ice and Fire"
    sol_2_3 ="Scorpians"
    sol_2_4 ="India written by" 
    sol_2_5 ="Glory"
elif ran2 == 8:
    ques_2= "The song of "
    sol_2_1 ="Achilles"
    sol_2_2 ="Ice and Fire"
    sol_2_3 ="Scorpians"
    sol_2_4 ="India written by" 
    sol_2_5 ="Glory"
else :
    ques_2 = "When is" 
    sol_2_1 ="Diwali"
    sol_2_2 ="Pongal"
    sol_2_3 ="Makar Sankranti"
    sol_2_4 = "Halloween"
    sol_2_5 ="Holi"

print()
print("Welcome to google fandom")
print()
player_1 = input("Enter player 1 name: ")
player_2 = input("Enter player 2 name: ")
print("Instructions are :")
print("1--> There will be 3 Rounds.")
print("2--> You will given some words of google search and some options.")
print("3--> Then you have to choose one option from one of them.")
print("4--> you will given points according to them.")
print("5--> In the end player who has more points will win the game")
print()
print("Round 1 is starting...")
print()
print(f"{player_1}'s turn")
print(f"Complete: {ques} ___")
print("options are --->")
print(f"option 1: {sol_3}")
print(f"option 2: {sol_1}")
print(f"option 3: {sol_5}")
print(f"option 4: {sol_2}")
print(f"option 5: {sol_4}")
print("Enter your answer 1/2/3/4/5 ")
input_2_1 = input()
input_2_1 = int(input_2_1)
if input_2_1 == 2:
    points_1 = 5
elif input_2_1 == 4:
    points_1 = 4
elif input_2_1 == 1:
    points_1 = 3
elif input_2_1 == 5:
    points_1 = 2
else:
    points_1 = 1
print(f"{player_1} round 1 points are {points_1}")
print()
print()
print(f"{player_2}'s turn")
print(f"Complete: {ques_2} ___")
print("options are --->")
print(f"option 1: {sol_2_4}")
print(f"option 2: {sol_2_3}")
print(f"option 3: {sol_2_1}")
print(f"option 4: {sol_2_5}")
print(f"option 5: {sol_2_2}")
print("Enter your answer 1/2/3/4/5 ")
input_1 = input()
input_1 = int(input_1)
if input_1 == 3:
    points_2_1 = 5
elif input_1 == 5:
    points_2_1 = 4
elif input_1 == 2:
    points_2_1 = 3
elif input_1 == 1:
    points_2_1 = 2
else:
    points_2_1 = 1
print(f"{player_2} round 1 points are {points_2_1}")
print()
print()
print("Round 2 begins...")
ran_2 = random.randint(1,9)
if ran != ran_2:
    if ran_2 == 1 :
          ques= "taylor swift"
    elif ran_2 == 2:
          ques= "BGMI"
          sol_1 ="launch date in india"
          sol_2 ="apk"
          sol_3 ="apk download"
          sol_4 ="lite" 
          sol_5 ="redeem code"
    elif ran_2 == 3:
          ques= "Mousse"
          sol_1 ="foundation"
          sol_2 ="cake"
          sol_3 ="chocolate"
          sol_4 ="pronounciation" 
          sol_5 ="meaning"
    elif ran_2 == 4:
        ques= "The song of "
        sol_1 ="Achilles"
        sol_2 ="Ice and Fire"
        sol_3 ="Scorpians"
        sol_4 ="India written by" 
        sol_5 ="Glory"
    elif ran_2 == 5:
        ques= "height"
        sol_1 ="of taj mahal"
        sol_2 ="in feet"
        sol_3 ="kaise bhadaye"
        sol_4 ="of mount everest" 
        sol_5 ="in cm"
    elif ran_2 == 7:
        ques= "what is"
        sol_1 ="my ip"
        sol_2 ="computer"
        sol_3 ="internet"
        sol_4 ="cryptocurency" 
        sol_5 ="today"
    elif ran_2 == 8:
        ques= "how to resister "
        sol_1 ="for booster dose"
        sol_2 ="for vaccination"
        sol_3 ="for covid vaccine"
        sol_4 ="mobile number in SBI" 
        sol_5 ="for free laptop in UP"
else :
    ques = "When is" 
    sol_1 ="Diwali"
    sol_2 ="Pongal"
    sol_3 ="Makar Sankranti"
    sol_4 = "Halloween"
    sol_5 ="Holi"

ran2_2 = random.randint(1,9)






print(f"{player_1}'s turn ")
print(f"Complete: {ques} ___")
print("options are --->")
print(f"option 1: {sol_5}")
print(f"option 2: {sol_2}")
print(f"option 3: {sol_4}")
print(f"option 4: {sol_1}")
print(f"option 5: {sol_3}")
print("Enter your answer 1/2/3/4/5 ")
input_2 = input()
input_2 = int(input_2)
if input_2 == 4:
    points_2 = 5
elif input_2 == 2:
    points_2 = 4
elif input_2 == 5:
    points_2 = 3
elif input_2 == 3:
    points_2 = 2
else:
    points_2 = 1

print(f"your round 2 points are {points_2}")
print()
print()
print("Round 3 begins...")
ran_3 = random.randint(1,9)
if ran != ran_3 :
    if ran_2 != ran_3 :
        if ran_3 == 1 :
            ques= "taylor swift"
            sol_1 ="boyfriend"
            sol_2 ="age"
            sol_3 ="net worth"
            sol_4 = "height"
            sol_5 ="birthday"
        elif ran_3 == 2:
            ques= "BGMI"
            sol_1 ="launch date in india"
            sol_2 ="apk"
            sol_3 ="apk download"
            sol_4 ="lite" 
            sol_5 ="redeem code"
        elif ran_3 == 3:
            ques= "Mousse"
            sol_1 ="foundation"
            sol_2 ="cake"
            sol_3 ="chocolate"
            sol_4 ="pronounciation" 
            sol_5 ="meaning"
        elif ran_3 == 4:
            ques= "The song of "
            sol_1 ="Achilles"
            sol_2 ="Ice and Fire"
            sol_3 ="Scorpians"
            sol_4 ="India written by" 
            sol_5 ="Glory"
        elif ran_3 == 5:
            ques= "height"
            sol_1 ="of taj mahal"
            sol_2 ="in feet"
            sol_3 ="kaise bhadaye"
            sol_4 ="of mount everest" 
            sol_5 ="in cm"
        elif ran_3 == 6:
            ques= "Most searched"
            sol_1 ="person on google"
            sol_2 ="topic on google"
            sol_3 ="topic on youtube"
            sol_4 ="things on google" 
            sol_5 ="on google today"
        elif ran_3 == 7:
            ques= "what is"
            sol_1 ="my ip"
            sol_2 ="computer"
            sol_3 ="internet"
            sol_4 ="cryptocurency" 
            sol_5 ="today"
        elif ran_3 == 8:
            ques= "how to resister "
            sol_1 ="for booster dose"
            sol_2 ="for vaccination"
            sol_3 ="for covid vaccine"
            sol_4 ="mobile number in SBI" 
            sol_5 ="for free laptop in UP"
else :
  ques = "When is" 
  sol_1 ="Diwali"
  sol_2 ="Pongal"
  sol_3 ="Makar Sankranti"
  sol_4 = "Halloween"
  sol_5 ="Holi"

print(f"Complete: {ques} ___")
print("options are --->")
print(f"option 1: {sol_2}")
print(f"option 2: {sol_5}")
print(f"option 3: {sol_3}")
print(f"option 4: {sol_1}")
print(f"option 5: {sol_4}")
print("Enter your answer 1/2/3/4/5 ")
input_3 = input()
input_3 = int(input_3)
if input_3 == 4:
    points_3 = 5
elif input_3 == 1:
    points_3 = 4
elif input_3 == 3:
    points_3 = 3
elif input_3 == 5:
    points_3 = 2
else:
    points_3 = 1
print(f"your round 3 points are {points_3}")
total_points = points_3 + points_1 + points_2
print()
print()
print(f"YOUR TOTAL POINTS ARE {total_points}")

