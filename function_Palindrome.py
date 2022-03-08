def Palindrome(string):
    return string==string[::-1]
string = "mom"
result = Palindrome(string)
if result:
    print("Yes")
else:
    print("No")