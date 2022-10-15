

import pyttsx3
import gtts
from playsound import playsound




question_list=["1. How many continents are there?","2. What is the capital of India?", 
"3. NG mei kaun se course padhaye jate hai?","4. Who is the current odi captain of team india?",
"5. Who is richest men in the world?", "6. Who is miss universe of 2022",
"7. How many gold medals india won in 2022 CWG?", "8. Who is vice president of india?"]

option_list=[["1. four", "2. nine", "3. seven", "4. eight", "5. lifeline"],["1. Chandigharh", "2. Bhopal", "4. Chennai", "5. Delhi", "6. lifeline"],["1. software engineering", "2. counseling", "3. tourism", "4. agriculture", "5. lifeline"],["1. m.s.dhoni", "2. rohit sharma", "3. virat kholi", "4. rishabh pant", "5. lifeline"],["1. jeff bejos", "2. bill gates","3. gautam adani", "4. elon musk", "5. lifeline"],["1. harnaj sindhu", "2. harshika thakur", "3. karoline", "4. shree sashi", "5. lifeline"],["1. 23", "2. 18", "3. 26", "4. 22", "5. lifeline"],["1. sudesh dhankar", "3. draupadi murmu", "4. nikhat", "5. lifeline"]]
helpline_50_50=[["1. nine", "2. seven"],["1. chennai","2. Delhi"],["1. software engineering", "2. counsiling"],["1. rohit sharma","2. virat kholi"],["1. gautam adani", "2. elon musk"],["1. harnaj sindhu", "2. harshika thakur"],["1. 23", "2. 22"],["1, jagdeep dhankar", "2. draupadi murmu",]]

solution_list = [3,4,1,2,4,2,4,2]
helpline_sol = [2,2,1,1,2,2,2,1]
phone_sol = [3,4,1,2,4,2,4,2]

lifeline = ["1. phone a friend","2. 50-50","3. audience poll", "4. skip the question"]

color_list = ["\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m"]
price_c = 1
price = [1000,2000,3000,4000,5000,6000,7000,8000]

for x in range(len(question_list)):
    print(f"Aapka sawal hai\n{color_list[0]}\n{question_list[x]}\n{price[price_c]}$ ke liye\a")
    t1 = gtts.gTTS(f"Aapka sawal hai,{question_list[x]}\n{price[price_c]}$ ke liye\naapke option")
    t1.save("welcome.mp3")
    playsound("welcome.mp3")
    for j in option_list[x]:
        print(f'{color_list[3]} {j}')
        t1 = gtts.gTTS(j)
        t1.save("welcome.mp3")
        playsound("welcome.mp3")
    ans = int(input(f"{color_list[4]} enter your option.."))    
    if ans==5:
        for hp_li in lifeline:
            print(hp_li)
            t1 = gtts.gTTS(hp_li)
            t1.save("welcome.mp3")
            playsound("welcome.mp3")
        ans1=int(input(f"{color_list[4]} enter your option.."))
        if ans1==1:
            lifeline.pop(0)
        elif ans1==2:
            lifeline.pop(1)
        elif ans1==3:
            lifeline.pop(2)
        else:
            lifeline.pop(3)
        if ans1==1:
            print("you chose phone a friend")
            t1 =gtts.gTTS("you chose phone a friend")
            t1.save("welcome.mp3")
            playsound("welcome.mp3")
            ans=int(input( f"{color_list[4]} enter your answer.."))
            if ans==phone_sol[x]:
                print(color_list[2],"correct answer\n ",price[x])
                t1 = gtts.gTTS("sahi jawab")
                t1.save("welcome.mp3")
                playsound("welcome.mp3") 
                price_c+=1
                continue
            else:
                print(color_list[2],"wrong answer")
                t1 =gtts.gTTS("galat jawab")
                t1.save("welcome.mp3")
                playsound("welcome.mp3")
                break
        elif ans1==2:
            print("you chose 50-50","\nyour option are",helpline_50_50[x])
            t1 =gtts.gTTS("you chose 50-50","\nyour option are",helpline_50_50[x])
            t1.save("welcome.mp3")
            playsound("welcome.mp3")
            ans=int(input("enter your number.."))
            if ans==helpline_sol[x]:
                print(color_list[2],"correct answer\n ",price[x])
                t1 = gtts.gTTS("sahi jawab","aap jeet gaye h", price[x])
                t1.save("welcome.mp3")
                playsound("welcome.mp3")
                price_c+=1
                continue
            else:
                print(color_list[2],"wrong answer")
                t1 =gtts.gTTS("galat jawab")
                t1.save("welcome.mp3")
                playsound("welcome.mp3")
                break
        elif ans1==4:
            price_c+=0
            continue
        
    elif ans == solution_list[x]:
        print(color_list[2], "correct answer")
        t1 = gtts.gTTS("sahi jawab","aap jeet gaye h", price[x])
        t1.save("welcome.mp3")
        playsound("welcome.mp3")
        price_c+=1
    else:
        print(color_list[2],"wrong answer")
        t1 = gtts.gTTS("galat jawab")
        t1.save("welcome.mp3")
        playsound("welcome.mp3")