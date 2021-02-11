
def decrypt(text1,s):
     result=''
     for i in range(len(text1)):
         char=text1[i]
         if(char.isupper()):
             result+=chr((ord(char)+ s-65)% 26+65)
         else:
               result+=chr((ord(char)+ s-97)% 26+97)  
     return result
text1 = input("the text is :")
"""print(text1)"""
s=-4
print("text1"+text1)
print("shift"+str(s))
print("cipher"+decrypt(text1,s))