t = int(input())

def palindrome(x):
  rev = ''.join(reversed(x))
  if (s == rev):
    return True
  return False
 
# main function

while(t>0):
  s = input("enterthe :")
  ans = palindrome(s)
   
  if (ans):
      print("It is a palindrome")
  else:
      print("No")
  t-=1