  def main():
    num,a,rev=0,0,0
    n=input("enter n")
    num=n
    while (num > 0):
        a=num%10
        rev=rev*10+a
        num=num/10
    if(n==rev):
        print"palindome"
    else:
        print"not palindrome"
