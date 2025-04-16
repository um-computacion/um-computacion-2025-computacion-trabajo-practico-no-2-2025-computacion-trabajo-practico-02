print ("Lector de palindromos - Consigna 2 Computacion - Francisco Robledo \n")


class Palindromo ():
    
    def is_palindrome(palindrome):
        palindrome = palindrome.lower()
        palindrome = palindrome.replace(" ", "")
        palindrome = palindrome.replace("à", "a")
        palindrome = palindrome.replace("è", "e")
        palindrome = palindrome.replace("ì", "i")
        palindrome = palindrome.replace("ò", "o")
        palindrome = palindrome.replace("ù", "u")
        a = 0
        b = len(palindrome) - 1
        for i in range(0, len(palindrome)):
            if palindrome[a] == palindrome[b]:
                a += 1
                b -= 1
            else: 
                return False
        return True    

    palindrome = str(input("Ingrese una palabra o frase: "))
    
    if is_palindrome(palindrome):
        print(palindrome + ". " + "Es una palabra o frase palíndroma")
    else: 
        print(palindrome + ". " + "No es una palabra o frase palíndroma")
