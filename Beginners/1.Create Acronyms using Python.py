"""
user_input =  str(input("Enter a phrase"))

text = user_input.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()

print(a)
"""

"""
# python program to print initials of a name
def name(s):
    # split the string into a list
    l = s.split()
    new = ""

    # traverse in the list
    for i in range(len(l) - 1):
        s = l[i]

        # adds the capital first character
        new += (s[0].upper() + '.')

    # l[-1] gives last item of list l. We
    # use title to print first character in
    # capital.
    new += l[-1].title()

    return new


# Driver code
s = str(input("Enter any name"))
print(name(s))
"""

# Python program to print
# initials of a name

# user define function
def printInitials(name):
	if(len(name) == 0):
		return
	print(name[0].upper()),
	for i in range(1, len(name) - 1):
		if (name[i] == ' '):
			print (name[i + 1].upper()),

def main():
	name = str(input("Enter any name"))
	printInitials(name)

if __name__=="__main__":
	main()
