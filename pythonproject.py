
# ===========================================================
# SECTION 1: PRACTICAL QUESTIONS ON DATA TYPES
# ===========================================================

print("\n" + "="*60)
print("SECTION 1: DATA TYPES")
print("="*60)

# -----------------------------------------------------------
# Q1. Store 5 student names in a list and display them one by one
# -----------------------------------------------------------
print("\n--- Q1: Student Names ---")
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
for name in students:
    print(name)

# -----------------------------------------------------------
# Q2. Accept 10 numbers and store only unique values
# -----------------------------------------------------------
print("\n--- Q2: Unique Numbers ---")
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"  Number {i+1}: "))
    numbers.append(num)
unique_numbers = list(set(numbers))
print("Unique values:", unique_numbers)

# -----------------------------------------------------------
# Q3. Tuple of 5 colors; display each using a loop
# -----------------------------------------------------------
print("\n--- Q3: Colors Tuple ---")
colors = ("Red", "Green", "Blue", "Yellow", "Purple")
for color in colors:
    print(color)

# -----------------------------------------------------------
# Q4. Count how many times a given element appears in a list
# -----------------------------------------------------------
print("\n--- Q4: Count Element in List ---")
data = [1, 2, 3, 2, 4, 2, 5, 2]
element = int(input("Enter element to count: "))
count = data.count(element)
print(f"'{element}' appears {count} time(s) in {data}")

# -----------------------------------------------------------
# Q5. Find the largest and smallest numbers in a list
# -----------------------------------------------------------
print("\n--- Q5: Largest and Smallest ---")
nums = [34, 7, 23, 32, 5, 62]
print("List:", nums)
print("Largest:", max(nums))
print("Smallest:", min(nums))

# -----------------------------------------------------------
# Q6. Remove all duplicate elements from a list
# -----------------------------------------------------------
print("\n--- Q6: Remove Duplicates ---")
lst = [1, 2, 2, 3, 4, 4, 5]
print("Original:", lst)
no_duplicates = list(dict.fromkeys(lst))
print("Without duplicates:", no_duplicates)

# -----------------------------------------------------------
# Q7. Merge two lists and display the result
# -----------------------------------------------------------
print("\n--- Q7: Merge Two Lists ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("List 1:", list1)
print("List 2:", list2)
print("Merged:", merged)

# -----------------------------------------------------------
# Q8. Reverse a string without using slicing
# -----------------------------------------------------------
print("\n--- Q8: Reverse a String (No Slicing) ---")
text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed:", reversed_text)

# -----------------------------------------------------------
# Q9. Count vowels, consonants, digits, and spaces in a string
# -----------------------------------------------------------
print("\n--- Q9: Count Characters ---")
sentence = input("Enter a string: ")
vowels = consonants = digits = spaces = 0
for ch in sentence.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Spaces: {spaces}")

# -----------------------------------------------------------
# Q10. Find the second largest number in a list
# -----------------------------------------------------------
print("\n--- Q10: Second Largest ---")
nums = [10, 20, 4, 45, 99, 99]
unique_sorted = sorted(set(nums), reverse=True)
if len(unique_sorted) >= 2:
    print("Second Largest:", unique_sorted[1])
else:
    print("Not enough unique elements.")


# ===========================================================
# SECTION 2: PRACTICAL QUESTIONS ON OPERATORS
# ===========================================================

print("\n" + "="*60)
print("SECTION 2: OPERATORS")
print("="*60)

# -----------------------------------------------------------
# Q1. Calculate total bill amount after adding GST
# -----------------------------------------------------------
print("\n--- Q1: GST Calculator ---")
amount = float(input("Enter bill amount: "))
gst_rate = float(input("Enter GST rate (%): "))
gst = (gst_rate / 100) * amount
total = amount + gst
print(f"GST Amount: ₹{gst:.2f}")
print(f"Total Bill: ₹{total:.2f}")

# -----------------------------------------------------------
# Q2. Check whether a number is even or odd
# -----------------------------------------------------------
print("\n--- Q2: Even or Odd ---")
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")

# -----------------------------------------------------------
# Q3. Find the greatest among three numbers using comparison operators
# -----------------------------------------------------------
print("\n--- Q3: Greatest of Three ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
greatest = a if (a >= b and a >= c) else (b if b >= c else c)
print(f"Greatest: {greatest}")

# -----------------------------------------------------------
# Q4. Swap two numbers without using a third variable
# -----------------------------------------------------------
print("\n--- Q4: Swap Without Third Variable ---")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

# -----------------------------------------------------------
# Q5. Check whether a number is divisible by both 3 and 5
# -----------------------------------------------------------
print("\n--- Q5: Divisible by 3 and 5 ---")
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is NOT divisible by both 3 and 5")

# -----------------------------------------------------------
# Q6. Calculate percentage of marks obtained in 5 subjects
# -----------------------------------------------------------
print("\n--- Q6: Percentage Calculator ---")
marks = []
for i in range(5):
    m = float(input(f"  Enter marks for subject {i+1} (out of 100): "))
    marks.append(m)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")

# -----------------------------------------------------------
# Q7. Check whether two variables refer to the same object
# -----------------------------------------------------------
print("\n--- Q7: Same Object Check ---")
p = [1, 2, 3]
q = p        # same object
r = [1, 2, 3]  # different object, same value
print(f"p is q: {p is q}")
print(f"p is r: {p is r}")
print(f"p == r: {p == r}")

# -----------------------------------------------------------
# Q8. Determine whether a character exists in a given string
# -----------------------------------------------------------
print("\n--- Q8: Character in String ---")
string = input("Enter a string: ")
char = input("Enter a character to search: ")
if char in string:
    print(f"'{char}' exists in the string.")
else:
    print(f"'{char}' does NOT exist in the string.")

# -----------------------------------------------------------
# Q9. Calculate simple interest
# -----------------------------------------------------------
print("\n--- Q9: Simple Interest ---")
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest (%): "))
time = float(input("Enter Time (years): "))
si = (principal * rate * time) / 100
print(f"Simple Interest: ₹{si:.2f}")
print(f"Total Amount: ₹{principal + si:.2f}")

# -----------------------------------------------------------
# Q10. Unit converter: kilometers and meters
# -----------------------------------------------------------
print("\n--- Q10: Unit Converter (km <-> m) ---")
choice = input("Convert (1) km to m  or  (2) m to km? Enter 1 or 2: ")
if choice == "1":
    km = float(input("Enter kilometers: "))
    print(f"{km} km = {km * 1000} meters")
else:
    m = float(input("Enter meters: "))
    print(f"{m} m = {m / 1000} kilometers")


# ===========================================================
# SECTION 3: PRACTICAL QUESTIONS ON CONDITIONAL STATEMENTS
# ===========================================================

print("\n" + "="*60)
print("SECTION 3: CONDITIONAL STATEMENTS")
print("="*60)

# -----------------------------------------------------------
# Q1. Login system with username and password validation
# -----------------------------------------------------------
print("\n--- Q1: Login System ---")
correct_user = "admin"
correct_pass = "password123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_user and password == correct_pass:
    print("Login successful! Welcome.")
else:
    print("Invalid username or password.")

# -----------------------------------------------------------
# Q2. Check whether a person is eligible to vote
# -----------------------------------------------------------
print("\n--- Q2: Voter Eligibility ---")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")

# -----------------------------------------------------------
# Q3. Find the greatest among three numbers
# -----------------------------------------------------------
print("\n--- Q3: Greatest of Three Numbers ---")
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
if a >= b and a >= c:
    print(f"Greatest: {a}")
elif b >= c:
    print(f"Greatest: {b}")
else:
    print(f"Greatest: {c}")

# -----------------------------------------------------------
# Q4. Grade calculator based on marks
# -----------------------------------------------------------
print("\n--- Q4: Grade Calculator ---")
marks = float(input("Enter your marks (out of 100): "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")

# -----------------------------------------------------------
# Q5. Check whether a year is a leap year
# -----------------------------------------------------------
print("\n--- Q5: Leap Year Check ---")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")

# -----------------------------------------------------------
# Q6. Determine whether a number is positive, negative, or zero
# -----------------------------------------------------------
print("\n--- Q6: Positive, Negative, or Zero ---")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# -----------------------------------------------------------
# Q7. Menu-driven calculator
# -----------------------------------------------------------
print("\n--- Q7: Menu-Driven Calculator ---")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Choose operation (1-4): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
if choice == "1":
    print(f"Result: {x + y}")
elif choice == "2":
    print(f"Result: {x - y}")
elif choice == "3":
    print(f"Result: {x * y}")
elif choice == "4":
    if y != 0:
        print(f"Result: {x / y:.4f}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid choice.")

# -----------------------------------------------------------
# Q8. Check whether a character is a vowel or consonant
# -----------------------------------------------------------
print("\n--- Q8: Vowel or Consonant ---")
ch = input("Enter a character: ").lower()
if ch.isalpha() and len(ch) == 1:
    if ch in "aeiou":
        print(f"'{ch}' is a Vowel.")
    else:
        print(f"'{ch}' is a Consonant.")
else:
    print("Please enter a single alphabet.")

# -----------------------------------------------------------
# Q9. Calculate electricity bill based on usage slabs
# -----------------------------------------------------------
print("\n--- Q9: Electricity Bill ---")
units = float(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = 100 * 1.5 + (units - 100) * 3.0
else:
    bill = 100 * 1.5 + 200 * 3.0 + (units - 300) * 5.0
print(f"Units Consumed: {units}")
print(f"Electricity Bill: ₹{bill:.2f}")

# -----------------------------------------------------------
# Q10. Determine the season based on the entered month number
# -----------------------------------------------------------
print("\n--- Q10: Season Finder ---")
month = int(input("Enter month number (1-12): "))
if month in [12, 1, 2]:
    print("Season: Winter")
elif month in [3, 4, 5]:
    print("Season: Spring")
elif month in [6, 7, 8]:
    print("Season: Summer")
elif month in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number.")

# -----------------------------------------------------------
# Q11. Check whether a person is eligible for a driving license
# -----------------------------------------------------------
print("\n--- Q11: Driving License Eligibility ---")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are NOT eligible. Minimum age is 18.")

# -----------------------------------------------------------
# Q12. Determine the type of triangle based on entered sides
# -----------------------------------------------------------
print("\n--- Q12: Triangle Type ---")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
# Check valid triangle
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle.")


# ===========================================================
# SECTION 4: PRACTICAL QUESTIONS ON FOR LOOPS
# ===========================================================

print("\n" + "="*60)
print("SECTION 4: FOR LOOPS")
print("="*60)

# -----------------------------------------------------------
# Q1. Print all even numbers between 1 and 100
# -----------------------------------------------------------
print("\n--- Q1: Even Numbers (1–100) ---")
print([n for n in range(2, 101, 2)])

# -----------------------------------------------------------
# Q2. Print the multiplication table of a given number
# -----------------------------------------------------------
print("\n--- Q2: Multiplication Table ---")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"  {n} x {i} = {n * i}")

# -----------------------------------------------------------
# Q3. Find the factorial of a number
# -----------------------------------------------------------
print("\n--- Q3: Factorial ---")
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} = {fact}")

# -----------------------------------------------------------
# Q4. Find the sum of numbers from 1 to N
# -----------------------------------------------------------
print("\n--- Q4: Sum 1 to N ---")
N = int(input("Enter N: "))
total = sum(range(1, N + 1))
print(f"Sum from 1 to {N} = {total}")

# -----------------------------------------------------------
# Q5. Count the number of digits in a number
# -----------------------------------------------------------
print("\n--- Q5: Count Digits ---")
num = int(input("Enter a number: "))
count = len(str(abs(num)))
print(f"Number of digits: {count}")

# -----------------------------------------------------------
# Q6. Reverse a number using a loop
# -----------------------------------------------------------
print("\n--- Q6: Reverse a Number ---")
num = int(input("Enter a number: "))
reversed_num = 0
temp = abs(num)
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if num < 0:
    reversed_num = -reversed_num
print(f"Reversed: {reversed_num}")

# -----------------------------------------------------------
# Q7. Find the sum of digits of a number
# -----------------------------------------------------------
print("\n--- Q7: Sum of Digits ---")
num = int(input("Enter a number: "))
digit_sum = sum(int(d) for d in str(abs(num)))
print(f"Sum of digits: {digit_sum}")

# -----------------------------------------------------------
# Q8. Print the Fibonacci series up to N terms
# -----------------------------------------------------------
print("\n--- Q8: Fibonacci Series ---")
N = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
print()

# -----------------------------------------------------------
# Q9. Find all prime numbers between 1 and 100
# -----------------------------------------------------------
print("\n--- Q9: Prime Numbers (1–100) ---")
primes = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(primes)

# -----------------------------------------------------------
# Q10. Count the number of even and odd elements in a list
# -----------------------------------------------------------
print("\n--- Q10: Even and Odd Count ---")
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = sum(1 for x in lst if x % 2 == 0)
odd_count = len(lst) - even_count
print(f"List: {lst}")
print(f"Even count: {even_count}, Odd count: {odd_count}")

# -----------------------------------------------------------
# Q11. Find the largest element in a list using a loop
# -----------------------------------------------------------
print("\n--- Q11: Largest Element ---")
lst = [3, 41, 12, 9, 74, 15]
largest = lst[0]
for item in lst:
    if item > largest:
        largest = item
print(f"List: {lst}")
print(f"Largest: {largest}")

# -----------------------------------------------------------
# Q12. Find the frequency of each element in a list
# -----------------------------------------------------------
print("\n--- Q12: Frequency of Elements ---")
lst = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
print(f"List: {lst}")
for key, val in freq.items():
    print(f"  {key} -> {val} time(s)")

# -----------------------------------------------------------
# Q13. Print a right-angled star pattern
# -----------------------------------------------------------
print("\n--- Q13: Right-Angled Star Pattern ---")
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("* " * i)

# -----------------------------------------------------------
# Q14. Print an inverted star pattern
# -----------------------------------------------------------
print("\n--- Q14: Inverted Star Pattern ---")
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("* " * i)

# -----------------------------------------------------------
# Q15. Print a pyramid pattern
# -----------------------------------------------------------
print("\n--- Q15: Pyramid Pattern ---")
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)


# ===========================================================
# SECTION 5: PRACTICAL QUESTIONS ON FUNCTIONS
# ===========================================================

print("\n" + "="*60)
print("SECTION 5: FUNCTIONS")
print("="*60)

# -----------------------------------------------------------
# Q1. Function to calculate area of a rectangle
# -----------------------------------------------------------
def area_rectangle(length, breadth):
    return length * breadth

print("\n--- Q1: Area of Rectangle ---")
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print(f"Area = {area_rectangle(l, b)}")

# -----------------------------------------------------------
# Q2. Function to calculate area of a circle
# -----------------------------------------------------------
import math
def area_circle(radius):
    return math.pi * radius ** 2

print("\n--- Q2: Area of Circle ---")
r = float(input("Enter radius: "))
print(f"Area = {area_circle(r):.4f}")

# -----------------------------------------------------------
# Q3. Function that returns the largest among three numbers
# -----------------------------------------------------------
def largest_of_three(a, b, c):
    return max(a, b, c)

print("\n--- Q3: Largest of Three ---")
a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))
print(f"Largest: {largest_of_three(a, b, c)}")

# -----------------------------------------------------------
# Q4. Function to check whether a number is prime
# -----------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\n--- Q4: Prime Check ---")
num = int(input("Enter a number: "))
print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}")

# -----------------------------------------------------------
# Q5. Function to find the factorial of a number
# -----------------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\n--- Q5: Factorial ---")
num = int(input("Enter a number: "))
print(f"Factorial of {num} = {factorial(num)}")

# -----------------------------------------------------------
# Q6. Function that counts vowels in a string
# -----------------------------------------------------------
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

print("\n--- Q6: Count Vowels ---")
text = input("Enter a string: ")
print(f"Vowel count: {count_vowels(text)}")

# -----------------------------------------------------------
# Q7. Function that reverses a string
# -----------------------------------------------------------
def reverse_string(s):
    return s[::-1]

print("\n--- Q7: Reverse String ---")
text = input("Enter a string: ")
print(f"Reversed: {reverse_string(text)}")

# -----------------------------------------------------------
# Q8. Function that checks whether a string is a palindrome
# -----------------------------------------------------------
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print("\n--- Q8: Palindrome Check ---")
text = input("Enter a string: ")
print(f"'{text}' is {'a Palindrome' if is_palindrome(text) else 'NOT a Palindrome'}")

# -----------------------------------------------------------
# Q9. Function that removes duplicate elements from a list
# -----------------------------------------------------------
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print("\n--- Q9: Remove Duplicates ---")
lst = [1, 2, 2, 3, 4, 4, 5]
print("Original:", lst)
print("Without duplicates:", remove_duplicates(lst))

# -----------------------------------------------------------
# Q10. Function that returns the second largest element in a list
# -----------------------------------------------------------
def second_largest(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) >= 2 else None

print("\n--- Q10: Second Largest ---")
lst = [10, 20, 4, 45, 99]
print("List:", lst)
print("Second Largest:", second_largest(lst))

# -----------------------------------------------------------
# Q11. Function that finds all prime numbers in a given range
# -----------------------------------------------------------
def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

print("\n--- Q11: Primes in Range ---")
start = int(input("Enter start: "))
end = int(input("Enter end: "))
print("Primes:", primes_in_range(start, end))

# -----------------------------------------------------------
# Q12. Function that returns the longest word in a sentence
# -----------------------------------------------------------
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

print("\n--- Q12: Longest Word ---")
sentence = input("Enter a sentence: ")
print(f"Longest word: '{longest_word(sentence)}'")

# -----------------------------------------------------------
# Q13. Function that calculates a student's grade
# -----------------------------------------------------------
def student_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    else: return "F"

print("\n--- Q13: Student Grade ---")
marks = float(input("Enter marks (out of 100): "))
print(f"Grade: {student_grade(marks)}")

# -----------------------------------------------------------
# Q14. Function that counts the frequency of characters in a string
# -----------------------------------------------------------
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print("\n--- Q14: Character Frequency ---")
text = input("Enter a string: ")
freq = char_frequency(text)
for ch, count in freq.items():
    print(f"  '{ch}': {count}")

# -----------------------------------------------------------
# Q15. Function that calculates the total bill amount including tax
# -----------------------------------------------------------
def total_bill(amount, tax_percent):
    tax = (tax_percent / 100) * amount
    return amount + tax

print("\n--- Q15: Total Bill with Tax ---")
amount = float(input("Enter bill amount: "))
tax = float(input("Enter tax percentage: "))
print(f"Total Bill: ₹{total_bill(amount, tax):.2f}")


# ===========================================================
# SECTION 6: COMBINED INTERVIEW-LEVEL PRACTICAL QUESTIONS
# ===========================================================

print("\n" + "="*60)
print("SECTION 6: COMBINED / INTERVIEW-LEVEL SYSTEMS")
print("="*60)

# ===========================================================
# Q1. Student Management System
# ===========================================================
print("\n--- Q1: Student Management System ---")

students_db = {}

def sms_add():
    roll = input("  Roll Number: ")
    name = input("  Name: ")
    marks = float(input("  Marks: "))
    students_db[roll] = {"name": name, "marks": marks}
    print("  Student added successfully.")

def sms_view():
    if not students_db:
        print("  No students found.")
    for roll, info in students_db.items():
        print(f"  Roll: {roll} | Name: {info['name']} | Marks: {info['marks']}")

def sms_search():
    roll = input("  Enter roll number to search: ")
    if roll in students_db:
        info = students_db[roll]
        print(f"  Found -> Name: {info['name']}, Marks: {info['marks']}")
    else:
        print("  Student not found.")

def sms_delete():
    roll = input("  Enter roll number to delete: ")
    if roll in students_db:
        del students_db[roll]
        print("  Student deleted.")
    else:
        print("  Student not found.")

while True:
    print("  1.Add  2.View  3.Search  4.Delete  5.Exit")
    ch = input("  Choice: ")
    if ch == "1": sms_add()
    elif ch == "2": sms_view()
    elif ch == "3": sms_search()
    elif ch == "4": sms_delete()
    elif ch == "5": break
    else: print("  Invalid choice.")

# ===========================================================
# Q2. Contact Book
# ===========================================================
print("\n--- Q2: Contact Book ---")

contacts = {}

while True:
    print("  1.Add  2.View  3.Search  4.Delete  5.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        name = input("  Name: ")
        phone = input("  Phone: ")
        contacts[name] = phone
        print("  Contact added.")
    elif ch == "2":
        if contacts:
            for n, p in contacts.items():
                print(f"  {n}: {p}")
        else:
            print("  No contacts.")
    elif ch == "3":
        name = input("  Enter name to search: ")
        print(f"  {name}: {contacts.get(name, 'Not found')}")
    elif ch == "4":
        name = input("  Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("  Deleted.")
        else:
            print("  Not found.")
    elif ch == "5":
        break

# ===========================================================
# Q3. Quiz Application
# ===========================================================
print("\n--- Q3: Quiz Application ---")

quiz = [
    {"q": "Capital of India?", "options": ["A.Mumbai", "B.Delhi", "C.Chennai", "D.Kolkata"], "ans": "B"},
    {"q": "2 + 2 = ?", "options": ["A.3", "B.4", "C.5", "D.6"], "ans": "B"},
    {"q": "Python is: ", "options": ["A.Compiled", "B.Interpreted", "C.Both", "D.Neither"], "ans": "B"},
]
score = 0
for i, q in enumerate(quiz):
    print(f"  Q{i+1}: {q['q']}")
    for opt in q['options']:
        print(f"       {opt}")
    ans = input("  Your answer (A/B/C/D): ").upper()
    if ans == q['ans']:
        print("  Correct!")
        score += 1
    else:
        print(f"  Wrong! Answer: {q['ans']}")
print(f"  Final Score: {score}/{len(quiz)}")

# ===========================================================
# Q4. Banking System
# ===========================================================
print("\n--- Q4: Banking System ---")

balance = 0.0
while True:
    print("  1.Deposit  2.Withdraw  3.Balance  4.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        amt = float(input("  Enter deposit amount: "))
        if amt > 0:
            balance += amt
            print(f"  Deposited ₹{amt:.2f}. Balance: ₹{balance:.2f}")
    elif ch == "2":
        amt = float(input("  Enter withdrawal amount: "))
        if amt > balance:
            print("  Insufficient balance.")
        else:
            balance -= amt
            print(f"  Withdrew ₹{amt:.2f}. Balance: ₹{balance:.2f}")
    elif ch == "3":
        print(f"  Current Balance: ₹{balance:.2f}")
    elif ch == "4":
        break

# ===========================================================
# Q5. ATM Simulation
# ===========================================================
print("\n--- Q5: ATM Simulation ---")

atm_pin = "1234"
atm_balance = 10000.0
entered_pin = input("  Enter PIN: ")
if entered_pin != atm_pin:
    print("  Incorrect PIN. Access denied.")
else:
    print("  Welcome!")
    while True:
        print("  1.Check Balance  2.Withdraw  3.Deposit  4.Exit")
        ch = input("  Choice: ")
        if ch == "1":
            print(f"  Balance: ₹{atm_balance:.2f}")
        elif ch == "2":
            amt = float(input("  Enter amount: "))
            if amt > atm_balance:
                print("  Insufficient funds.")
            else:
                atm_balance -= amt
                print(f"  Dispensing ₹{amt:.2f}. Remaining: ₹{atm_balance:.2f}")
        elif ch == "3":
            amt = float(input("  Enter deposit amount: "))
            atm_balance += amt
            print(f"  Deposited ₹{amt:.2f}. Balance: ₹{atm_balance:.2f}")
        elif ch == "4":
            print("  Thank you. Goodbye!")
            break

# ===========================================================
# Q6. Library Management System
# ===========================================================
print("\n--- Q6: Library Management System ---")

library = {}

while True:
    print("  1.Add Book  2.View Books  3.Issue Book  4.Return Book  5.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        isbn = input("  ISBN: ")
        title = input("  Title: ")
        library[isbn] = {"title": title, "issued": False}
        print("  Book added.")
    elif ch == "2":
        for isbn, info in library.items():
            status = "Issued" if info['issued'] else "Available"
            print(f"  [{isbn}] {info['title']} - {status}")
    elif ch == "3":
        isbn = input("  Enter ISBN to issue: ")
        if isbn in library and not library[isbn]['issued']:
            library[isbn]['issued'] = True
            print("  Book issued.")
        elif isbn in library:
            print("  Book already issued.")
        else:
            print("  Book not found.")
    elif ch == "4":
        isbn = input("  Enter ISBN to return: ")
        if isbn in library and library[isbn]['issued']:
            library[isbn]['issued'] = False
            print("  Book returned.")
        else:
            print("  Invalid return.")
    elif ch == "5":
        break

# ===========================================================
# Q7. Restaurant Billing System
# ===========================================================
print("\n--- Q7: Restaurant Billing System ---")

menu = {"Dosa": 40, "Idli": 30, "Biryani": 120, "Tea": 15, "Coffee": 25}
order = {}
print("  Menu:")
for item, price in menu.items():
    print(f"    {item}: ₹{price}")

while True:
    item = input("  Enter item (or 'done' to finish): ").title()
    if item == "Done":
        break
    if item in menu:
        qty = int(input(f"  Quantity of {item}: "))
        order[item] = order.get(item, 0) + qty
    else:
        print("  Item not found.")

print("\n  --- Bill ---")
subtotal = 0
for item, qty in order.items():
    cost = qty * menu[item]
    subtotal += cost
    print(f"  {item} x{qty} = ₹{cost}")
gst = subtotal * 0.05
print(f"  GST (5%): ₹{gst:.2f}")
print(f"  Total: ₹{subtotal + gst:.2f}")

# ===========================================================
# Q8. Employee Salary Management System
# ===========================================================
print("\n--- Q8: Employee Salary Management System ---")

employees = {}

def calculate_salary(basic):
    hra = 0.2 * basic
    da = 0.1 * basic
    pf = 0.12 * basic
    gross = basic + hra + da
    net = gross - pf
    return {"basic": basic, "hra": hra, "da": da, "pf": pf, "gross": gross, "net": net}

while True:
    print("  1.Add Employee  2.View All  3.Search  4.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        eid = input("  Employee ID: ")
        name = input("  Name: ")
        basic = float(input("  Basic Salary: "))
        employees[eid] = {"name": name, **calculate_salary(basic)}
        print("  Employee added.")
    elif ch == "2":
        for eid, info in employees.items():
            print(f"  ID:{eid} | {info['name']} | Net Salary: ₹{info['net']:.2f}")
    elif ch == "3":
        eid = input("  Enter Employee ID: ")
        if eid in employees:
            info = employees[eid]
            print(f"  Name: {info['name']}")
            print(f"  Basic: ₹{info['basic']:.2f} | HRA: ₹{info['hra']:.2f} | DA: ₹{info['da']:.2f}")
            print(f"  PF: ₹{info['pf']:.2f} | Gross: ₹{info['gross']:.2f} | Net: ₹{info['net']:.2f}")
        else:
            print("  Employee not found.")
    elif ch == "4":
        break

# ===========================================================
# Q9. Inventory Management System
# ===========================================================
print("\n--- Q9: Inventory Management System ---")

inventory = {}

while True:
    print("  1.Add Item  2.View  3.Update Qty  4.Delete  5.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        code = input("  Item Code: ")
        name = input("  Item Name: ")
        qty = int(input("  Quantity: "))
        price = float(input("  Price: "))
        inventory[code] = {"name": name, "qty": qty, "price": price}
        print("  Item added.")
    elif ch == "2":
        for code, info in inventory.items():
            print(f"  [{code}] {info['name']} | Qty: {info['qty']} | Price: ₹{info['price']}")
    elif ch == "3":
        code = input("  Enter item code: ")
        if code in inventory:
            qty = int(input("  New quantity: "))
            inventory[code]['qty'] = qty
            print("  Updated.")
        else:
            print("  Item not found.")
    elif ch == "4":
        code = input("  Enter item code to delete: ")
        if code in inventory:
            del inventory[code]
            print("  Deleted.")
        else:
            print("  Not found.")
    elif ch == "5":
        break

# ===========================================================
# Q10. Movie Ticket Booking System
# ===========================================================
print("\n--- Q10: Movie Ticket Booking System ---")

movies = {"Inception": {"time": "7:00 PM", "price": 150, "seats": 10},
          "Interstellar": {"time": "9:30 PM", "price": 180, "seats": 8}}

print("  Available Movies:")
for movie, info in movies.items():
    print(f"  {movie} | Time: {info['time']} | Price: ₹{info['price']} | Seats: {info['seats']}")

movie = input("  Enter movie name: ").title()
if movie in movies:
    seats = int(input("  Number of tickets: "))
    if seats <= movies[movie]['seats']:
        movies[movie]['seats'] -= seats
        total = seats * movies[movie]['price']
        print(f"  Booking confirmed! Total: ₹{total}")
    else:
        print("  Not enough seats available.")
else:
    print("  Movie not found.")

# ===========================================================
# Q11. Hotel Room Reservation System
# ===========================================================
print("\n--- Q11: Hotel Room Reservation System ---")

rooms = {101: {"type": "Single", "price": 1500, "booked": False},
         102: {"type": "Double", "price": 2500, "booked": False},
         201: {"type": "Suite", "price": 5000, "booked": False}}

while True:
    print("  1.View Rooms  2.Book Room  3.Checkout  4.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        for num, info in rooms.items():
            status = "Booked" if info['booked'] else "Available"
            print(f"  Room {num} | {info['type']} | ₹{info['price']}/night | {status}")
    elif ch == "2":
        rnum = int(input("  Enter Room Number: "))
        if rnum in rooms and not rooms[rnum]['booked']:
            nights = int(input("  Number of nights: "))
            rooms[rnum]['booked'] = True
            total = nights * rooms[rnum]['price']
            print(f"  Room {rnum} booked for {nights} night(s). Total: ₹{total}")
        elif rnum in rooms:
            print("  Room already booked.")
        else:
            print("  Room not found.")
    elif ch == "3":
        rnum = int(input("  Enter Room Number to checkout: "))
        if rnum in rooms and rooms[rnum]['booked']:
            rooms[rnum]['booked'] = False
            print("  Checkout successful. Thank you!")
        else:
            print("  Room not booked or not found.")
    elif ch == "4":
        break

# ===========================================================
# Q12. Simple E-Commerce Cart System
# ===========================================================
print("\n--- Q12: E-Commerce Cart System ---")

products = {"Laptop": 45000, "Mouse": 500, "Keyboard": 1200, "Headphones": 2000}
cart = {}

print("  Available Products:")
for p, price in products.items():
    print(f"  {p}: ₹{price}")

while True:
    print("  1.Add to Cart  2.View Cart  3.Remove  4.Checkout  5.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        item = input("  Product name: ").title()
        if item in products:
            qty = int(input("  Quantity: "))
            cart[item] = cart.get(item, 0) + qty
            print("  Added to cart.")
        else:
            print("  Product not found.")
    elif ch == "2":
        if cart:
            total = 0
            for item, qty in cart.items():
                cost = qty * products[item]
                total += cost
                print(f"  {item} x{qty} = ₹{cost}")
            print(f"  Cart Total: ₹{total}")
        else:
            print("  Cart is empty.")
    elif ch == "3":
        item = input("  Enter product to remove: ").title()
        if item in cart:
            del cart[item]
            print("  Removed from cart.")
        else:
            print("  Item not in cart.")
    elif ch == "4":
        if cart:
            total = sum(qty * products[item] for item, qty in cart.items())
            print(f"  Order placed! Total: ₹{total}")
            cart.clear()
        else:
            print("  Cart is empty.")
    elif ch == "5":
        break

# ===========================================================
# Q13. Bus Ticket Reservation System
# ===========================================================
print("\n--- Q13: Bus Ticket Reservation System ---")

bus = {"seats": list(range(1, 21)), "booked": [], "price": 250}

while True:
    print("  1.View Seats  2.Book  3.Cancel  4.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        available = [s for s in bus['seats'] if s not in bus['booked']]
        print(f"  Available Seats: {available}")
    elif ch == "2":
        seat = int(input("  Enter seat number: "))
        if seat in bus['seats'] and seat not in bus['booked']:
            bus['booked'].append(seat)
            print(f"  Seat {seat} booked. Fare: ₹{bus['price']}")
        else:
            print("  Seat not available.")
    elif ch == "3":
        seat = int(input("  Enter seat number to cancel: "))
        if seat in bus['booked']:
            bus['booked'].remove(seat)
            print(f"  Seat {seat} cancelled.")
        else:
            print("  Seat not booked.")
    elif ch == "4":
        break

# ===========================================================
# Q14. Password Strength Checker
# ===========================================================
print("\n--- Q14: Password Strength Checker ---")

def check_password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add digits.")
    if any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

password = input("  Enter password to check: ")
strength, tips = check_password_strength(password)
print(f"  Strength: {strength}")
if tips:
    print("  Suggestions:")
    for tip in tips:
        print(f"    - {tip}")

# ===========================================================
# Q15. File-Based Student Result Management System
# ===========================================================
print("\n--- Q15: File-Based Student Result Management System ---")
import os

RESULT_FILE = "student_results.txt"

def save_result(roll, name, marks):
    with open(RESULT_FILE, "a") as f:
        grade = student_grade(marks)
        f.write(f"{roll},{name},{marks},{grade}\n")

def view_results():
    if not os.path.exists(RESULT_FILE):
        print("  No results found.")
        return
    with open(RESULT_FILE, "r") as f:
        lines = f.readlines()
    if not lines:
        print("  No results found.")
    for line in lines:
        roll, name, marks, grade = line.strip().split(",")
        print(f"  Roll: {roll} | Name: {name} | Marks: {marks} | Grade: {grade}")

def search_result(search_roll):
    if not os.path.exists(RESULT_FILE):
        print("  No records found.")
        return
    with open(RESULT_FILE, "r") as f:
        for line in f:
            roll, name, marks, grade = line.strip().split(",")
            if roll == search_roll:
                print(f"  Roll: {roll} | Name: {name} | Marks: {marks} | Grade: {grade}")
                return
    print("  Student not found.")

while True:
    print("  1.Add Result  2.View All  3.Search  4.Exit")
    ch = input("  Choice: ")
    if ch == "1":
        roll = input("  Roll Number: ")
        name = input("  Name: ")
        marks = float(input("  Marks (out of 100): "))
        save_result(roll, name, marks)
        print("  Result saved.")
    elif ch == "2":
        view_results()
    elif ch == "3":
        roll = input("  Enter Roll Number to search: ")
        search_result(roll)
    elif ch == "4":
        print("  Exiting. Results saved to file.")
        break

print("\n" + "="*60)
print("ALL PROGRAMS COMPLETED!")
print("="*60)