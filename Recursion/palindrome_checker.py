def is_palindrome(word):

    # base case
    if len(word) <= 2 and word[0] == word[-1]:
        return True
    elif word[0] == word[-1]:
        is_palindrome(word[1:-1])
    else:
        return False
        
