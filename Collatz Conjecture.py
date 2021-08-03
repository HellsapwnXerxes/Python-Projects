count = 0
num = int(input("Enter any numberf: "))

while(num!=1):
    if(num % 2 == 0):
        num /= 2
        print(num)
    else:
        num = num * 3 + 1
        print(num)
    count += 1

print("\nThe number of iterations to reach 1 are: ", count)