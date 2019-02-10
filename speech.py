import speech_recognition as sr
import random
print('''

A VERY BASIC SPEECH RECOGNITION GAME BASED ON ADDITION

''')
x=10
count=0
flag=0
r = sr.Recognizer()

with sr.Microphone() as source:
    
    while(1):
            
        try:            
            a = int(random.random()*x)
            b = int(random.random()*x)
            print(a,"+",b)
            r.adjust_for_ambient_noise(source)        
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if(int(text)==a+b):
                count+=1
            print("i heard this",text,"correct answer is = ",a+b)    
            print("your score is = ",count)
            if(count%5==0):
                x*=10
        except:
            print("could not detect correct answer is = ",a+b)
            print("your score is = ",count)
        
