# Write a Python program that takes an integer `n` from the user and:

# - Use a **loop** to print all numbers from `1` to `n`.
# - Use **conditional statements** to identify whether each number is **even or odd**.
# - Use operators to calculate and display:
#     - Sum of all numbers
#     - Sum of even numbers
#     - Sum of odd numbers
# - At the end, display whether the total sum is **even or odd**.

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input("Enter the value of N : "))
sum = 0
sumOfEven = 0
sumOfOdd = 0

for i in range(1, n+1):
    sum = sum + i
    if isEven(i):
        sumOfEven = sumOfEven + i
    if not isEven(i):
            sumOfOdd = sumOfOdd + i
    print(i)

print(f"Sum of all numbers:{sum}")
print(f"Sum of even numbers:{sumOfEven}")
print(f"Sum of odd numbers:{sumOfOdd}")

if isEven(sum):
    print("Sum is even")
if not isEven(sum):
    print("Sum is odd")