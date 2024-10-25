def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    normal_years = int(input("Input a dog's age in human years: "))

    dog_y = 0
    for n in range(1,normal_years+1):
        if n<3:
            dog_y += 10.5
        else :
            dog_y+=4
    print("The dog's age in dog's years is",int(dog_y))
            
    
    

    #enter your code here

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """
    output = ""
    for n in range(1,num+1):
        if n > 1: output+=' '
        if n%3== 0 and n%5 ==0:
            output+='FizzBuzz'
        elif n%3 == 0:
            output+='Fizz'
        elif n%5==0 :
            output+='Buzz'
        else:
            output+=str(n)
            
    return output
            
    

    #enter your code here

    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    try:
        mydict = {}
        sentence = sentence.strip().split()
        for word in sentence:
            if word not in mydict.keys():
                mydict[word]=len(word)
    except:
        raise ValueError

    return mydict      
    
    #enter your code here

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    if type(number) != int or number <0:
        raise ValueError
    else:
        sum= 0
        for n in str(number):
            sum += int(n)**3
    return sum
    
    #enter your code here

