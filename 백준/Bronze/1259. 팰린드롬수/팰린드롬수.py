while True:
    palindrome = input()

    if palindrome == '0':
        break
    
    else:        
        if all(int(i) - int(j) == 0 for i, j in zip(palindrome, palindrome[::-1])):
            print('yes')
        else:
            print('no')