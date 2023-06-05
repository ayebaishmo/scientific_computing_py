"""smallest = None
print("Before", smallest)

for interval in [3,41,12,9,74,15]:
    if smallest is None or interval < smallest:
        smallest = interval
    print("Loop", interval, smallest)
print("Smallest:", smallest)"""

# What does the following code print

"""for n in "banana":
    print(n)"""

# What is the value of i in the following code?
"""word = "bananay"
i =word.find("y")
print(i)"""

# What is the value of x after running this code:
"""word = "banana"
print(word[3])"""

# What does n equal in this code?
"""words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]
print(n)"""

# dictionary
# What does dict equal after running this code?:
"""dict = {'Fri' : 20,
        'Thus' : 6,
        'Sat' : 1}
dict['Sat'] = 2
dict['Thu'] = 13
dict['Sun'] = 9
print(dict)"""

# What will the following code print?
"""counts = {'quincy' : 1,
          'mrugesh' : 42,
          'beau' : 100,
          '0' : 10}
print(counts.get('kris', 0))"""

#same
"""counts = {'chuck' : 1,
          'annie' : 42,
          'jan' : 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])"""

# Tuples
"""d = dict()
d['quincy'] = 1
d['beau'] = 1
d['Kris'] = 1

for (k,i) in d.items():
    print(k,i)"""

# Tuples sort by values
"""counts = {'apple': 3, 'banana': 5, 'orange': 2}
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)"""

# regex
"""import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)"""

# Socket
"""import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()"""

# Http E
"""import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())"""



"""The code you provided demonstrates the use of the urllib.request module in Python for retrieving data from a URL. Here's a breakdown of what each part does:

import urllib.request: This line imports the urllib.request module, which provides functions for making HTTP requests and working with URLs.

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt'): This line opens a connection to the specified URL using the urlopen() function from urllib.request. It retrieves the content of the 'romeo.txt' file from the server and assigns it to the variable fhand.

The following block of code creates a loop that iterates over each line of the content received from the URL.

print(line.decode().strip()) decodes each line from bytes to a string using the decode() method and removes leading and trailing whitespace using the strip() method. The resulting string is then printed to the console.

The overall effect of this code is that it opens a connection to the specified URL, retrieves the content of the 'romeo.txt' file, and prints each line of the content to the console after decoding it from bytes to a string.

It's worth noting that the urllib.request module is a higher-level module that provides a convenient interface for making HTTP requests. In comparison to the previous code that used the socket module, this approach abstracts away many low-level details and simplifies the process of fetching data from a URL."""


# Classes
"""class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)
an = PartyAnimal()
an.party()
an.party()"""

# Arithmetic formatter
# Create a function that has an argument problem
def arithmetic_arranger(problems , show_answers = False):
    # Declare the lines where the result will sit
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    arranged_problems = ""

    # The problems should not exceed 5
    if len(problems) > 5:
        return "Error: Too many problems"
    
    # Iterate through the problem to split it in to three parts
    for problem in problems:
        num1, operator, num2 = problem.split()

        # Checking if the operator are + or -
        if operator not in ["+", "-"]:
            return "Error: Operator must be + or  -."
        
        # Checking if the nums are digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits"
        
        # Checks of the digits are more than 4
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"
        
        # This line calculates the maximum length between num1 and num2 plus 2 account for additional space plus to
        #account for additional space needed fot the operator. It uses to align numbers
        width = max(len(num1), len(num2)) + 2

        # The eval method solves the problem by turning it in to solution 3 + 4 =7
        # However we have to turn the solution in to string. str
        result = str(eval(problem))

        # The rjust method is used to right align the numbers within specified width.
        line1 += num1.rjust(width)
        line2 += operator + num2.rjust(width - 1)
        line3 += "-" * width
        line4 += result.rjust(width)

        # These lines add four spaces to each line.
        if problem != problems[-1]:
            line1 = line1 + "    "
            line2 = line2 + "    "
            line3 = line3 + "    "
            line4 = line4 + "    "
    
    # The lines are then concatenated into the arranged_problems string, with newlines (\n) separating each line.
    arranged_problems += line1 + "\n" + line2 + "\n" + line3
    if show_answers:
        arranged_problems += "\n" + line4
    print(arranged_problems)

arithmetic_arranger(["2 + 3", "3 - 5", "9 + 5", "745 + 32"], True)


