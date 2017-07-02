def is_palindrome(word):

    # base case
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
        
