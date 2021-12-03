n = int(input("Enter the ending number: "))
sum = 5

for num in range(1, n + 1, 2):
     sum = (n*(n + 1))/2
print("The sum of the first", n, "numbers is: ", int(sum))
average = sum / n
print("The average of the first 8 numbers is: ", average)