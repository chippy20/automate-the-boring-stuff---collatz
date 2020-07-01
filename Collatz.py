def collatz(number):        #define function 
    
        if number % 2 == 0: #if / else statement to determine if even or odd number 
            x = number // 2
            print (x)       #and then output result
            return x
        else:
            y = 3 * number + 1
            print (y)
            return y

print ('Enter number:')     #print command to enter number
number = int(input())       #number is input and made into integer
while number > 1:           #while loop to keep calling collatz until number = 1
    number = collatz(number)#keep calling collatz on number


    
