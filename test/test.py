strings = """
Welcome!
Are you completely new to programming?
If not then we presume you will be looking for information
about why and how to get started with Python.
Fortunately an experienced programmer in any programming language 
(whatever it may be) can pick up Python very quickly.
It is also easy for beginners to use and learn.
Installing Python is generally easy, and nowadays many Linux and UNIX distributions
include a recent Python. Even some Windows computers (notably those from HP) now
come with Python already installed.
If you do need to install Python and are not confident 
about the task you can find a few notes on the BeginnersGuide 
or Download wiki page, but installation is unremarkable on most platforms.
"""

counts = dict()

for i in range(ord("a"), ord("z") + 1):  # ascii code가 아닌 unicode
    counts[chr(i)] = 0

# print(counts)

strings = strings.lower()

for char in strings:
    if char.isalpha() == True:
        counts[char] += 1

print(counts)
