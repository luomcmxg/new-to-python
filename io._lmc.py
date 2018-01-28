import re


def re_lmc(text):
	text=text.upper()
	return re.sub('[,?! ]', "", text)

def reverse(text):
    re_lmc(text)
    return text[::-1]


def is_plaindrome(text):
    text = re_lmc(text)
    return text == reverse(text)


something = input("Enter text: ")


while(something != "quit"):
    if is_plaindrome(something):
        print("Yes, it is a palindrome!")
    else:
        print("No, it is not a palindrome!")
    something = input("Enter text: ")
