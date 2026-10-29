sentence=input("sentence:")
a=len(sentence)
parts=sentence.split(" ")
r=len(parts)
x=0
m=0
p=0
b=0
i=0
t=0
vowel="aeiouAEIOU"
for ch in sentence:
    if ch in vowel:
        x+=1
    if ch.isalpha()==True and ch not in vowel:
        m+=1
    if ch.isdigit():
        p+=1
    if ch.isspace():
        b+=1
    if ch.isalpha():
        t+=1
    if ch not in vowel and ch.isalpha()==False and ch.isdigit()==False and ch.isspace()==False and ch.isalpha()==False:
        i+=1
per=(x/t)*100
print(f"Enter a sentence:{sentence}")
print("===========================================")
print("DOCUMENT ANALYSIS REPORT")
print("===========================================")
print(f"Sentence:{sentence}")
print(f"Total Character:{a}")
print("---Character Breakdown---")
print(f"Words:{r}")
print(f"Vowels:{x}")
print(f"Consonents:{m}")
print(f"Digits:{p}")
print(f"Spaces:{b}")
print(f"Special Characters:{i}")
print("---Summary----")
print(f"Total letter:{t}")
print(f"Vowel Percentage:{per}")
print("===================================")
print("Analysis Complete!")
print("===================================")