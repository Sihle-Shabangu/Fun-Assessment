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

    #enter your code here
    human_age =  int(input("Please input the dog age in human years upto 20 "))

    while human_age > 20:
        human_age =  int(input("Please input the dog age in human years upto 20 "))
    dog_age  = 0
    for i in range(1,human_age+1):
        if i == 1 or i == 2:
            dog_age += 10.5

        else:
            dog_age += 4
    
    print(f"The dog's age in dog's years is {round(dog_age)}")

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """
    empty_string = ""

    for i in range(num + 1):
        if i == 0:
            empty_string += ""
        elif i % 5 == 0 and i % 3 == 0:
            empty_string += "FizzBuzz"
        elif i %  5 == 0:
            empty_string += "Buzz"
        elif i % 3 == 0:
            empty_string += "Fizz"
        else:
            empty_string += str(i)
        empty_string +=" "
    

    return empty_string.strip()

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
    
    #enter your code here
    str_sent = str(sentence)

    if str_sent.isdigit():
        raise ValueError("The sentence contains numbers")

    split_sent = str_sent.split(" ")
    empty_dict = {}
    for word in split_sent:
        empty_dict[word] = len(word)
    
    return empty_dict
def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here

    str_num = str(number)
    sum = 0
    for i in str_num:
        sum += int(i)**3
    return sum