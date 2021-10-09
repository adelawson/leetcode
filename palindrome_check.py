def palindrome(word):
    y=[i for i in word]
    y.reverse()
    y = "".join(y)

    if (y == word):
        print("it is a palindrome")
        return True
    else:
        print("it is not a palindrome")
        return False
    
    
