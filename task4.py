#write a programto check input string is palindrome or not using while loop
str1="TENET"
palindrome=True
for i in range(len(str1)//2):
    if str1[i]!=str1[-(i+1)]:
        palindrome=False
        break
    if palindrome:
        print("string is palindrome")
    else:
        print("string is not a palindrome") 

#write a program to reverse a number without converting into string
num=1234567890
convrt=str(num) 
for x in convrt:
    print(x)              

