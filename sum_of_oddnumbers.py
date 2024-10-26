#Create a program that prompts the user to enter a number n and then calculates and displays the sum of all odd numbers up to that number n.
x=int(input("please enter integer number"))
i=1
sum=0
while i<=x:
    sum+=i
    i+=2
print(sum)
