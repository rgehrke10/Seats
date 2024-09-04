
def firstClass():
    global booking, choice, seat
#I defined booking, choice, and seat as global variables because they will be used by all functions    
#control needs to be initialized with any number different from 2, so it can get in the while loop

    control = 1
    print(booking)
    seat = 0
    seat = int(input('Please select your seat (1 - 5): ')) 
#above, user is asked to choose a value for seat

    while control != 2:
#first if needs to check if the seat is already taken
#becuase booking is a list, the position of the elements will not translate exactly to the seat value
#that said, we need to use seat-1 to find the correct index in the list
#in addition to that, we also need to check if the seat is between 1 and 5 to analyze only the first class seats
        
        if booking[seat-1] == 'X' and seat > 0 and seat < 6:    
            print('Seat already taken.')
            seat = int(input('Please select your seat (1 - 5): '))
            
#if we see that the seat is not takes, we can replace the A in the designated position by an X:
#and of course, also checking if the seat is between 1 and 5
        elif seat > 0 and seat < 6:
            booking[seat-1] = 'X'
            print('\n')
            print(booking)
            print('\n')
#inside the elif, we added a statement that will make us go back to the menu if the seats are all taken            
            if booking[0:5] == ['X','X','X','X','X']:
                control = 2
            else:           
#in case they are not all taken, the user can choose if he wants to choose another seat or go back to menu                
                print('Would you like to choose another seat in First Class?', '1. Yes', '2. No', sep = '\n')
                control = int(input('Please choose a number: ' ))
                print('\n')
            
#this statement forces the user to choose either 1 or 2. Any number other than them will not move the program forward            
            while control != 1 and control != 2:
                control = control = int(input('Please choose a valid number: ' ))
#if the user chooses 1, he can choose another seat from first class
            if control == 1:
                seat = int(input('Please select your seat (1 - 5): '))
# this statement makes the user choose another number if seat is not between 1 and 5       
        else:
            print('This seat is not available.')
            seat = int(input('Please select your seat (1 - 5): '))
        
    
def economy():
    global booking, choice, seat
    
#economy works exactly like first class, just the range of seat are different.
#booking, choice, and seat are also declared as global variables
#control is a local variable because we use it to control the while statement    
    control = 1
    print(booking)
    seat = 0
    seat = int(input('Please select your seat (6 - 10): ')) 

    while control != 2:
        if booking[seat-1] == 'X' and seat > 5 and seat < 11:    
            print('Seat already taken.')
            seat = int(input('Please select your seat (6 - 10): '))
            
        elif seat > 5 and seat < 11:
            booking[seat-1] = 'X'
            print('\n')
            print(booking)
            print('\n')
            if booking[5:10] == ['X','X','X','X','X']:
                control = 2
            else:    
                print('Would you like to choose another seat in Economy?', '1. Yes', '2. No', sep = '\n')
                control = int(input('Please choose a number: ' ))
                print('\n')
            while control != 1 and control != 2:
                control = control = int(input('Please choose a valid number: ' ))
            if control == 1:
                seat = int(input('Please select your seat (6 - 10): '))
    
        else:
            print('This seat is not available.')
            seat = int(input('Please select your seat (6 - 10): '))
            
def menu():
    global booking, choice, seat
#in menu, booking, choice, and seat are also global variables
#we start with checking if either first class or economy are all X.
#if so, they will have FULL next to their names.
#if they are not full, FULL will not appear.
    if booking[0:5] == ['X','X','X','X','X']:
        print('1. First Class', '(Rows: 1 to 5)  FULL', sep ='   ')
    else:
        print('1. First Class', '(Rows: 1 to 5)', sep ='   ')
#same is done with economy        
    if booking[5:10] == ['X','X','X','X','X']:
        print('2. Economy', '(Rows: 6 to 10) FULL', sep ='       ')
    else:
        print('2. Economy', '(Rows: 6 to 10)', sep ='       ')
#printing the 3rd option, to exit the program       
    print('3. Exit')
    print('\t')
    print('Seating Chart: ', booking)
#also print the booking chart
    choice = int(input('Choice ==> '))
#for last, we ask the user to choose what option they want
    print('\n')

def main():
#delcaring booking, choice, and seat as global.    
    global booking, choice, seat    
    booking = ['A','A','A','A','A','A','A','A','A','A']
    choice = 0
    seat = 0
#declaring booking as a list with 10 'A' as all the seat are available in the beginning.
#choice and seat are 0s.
#the while statemnt keeps running if the choice is different of 3 (exit)    
    while choice != 3:
        menu()
#first thing that we do is to call menu
#with menu, the user will choose a number for choice. If it is one, we will first check if there are seats available
#if there aren't, we will tell the user that the first class is full, and not call any function    
        if choice == 1:
            if booking[0:5] == ['X','X','X','X','X']:
                print('First class is full.')
#if there are seats, we call function first class.
            else:
                firstClass()            
#same thing is done with economy, fist check if there are seats available. If so, we call the function
   
        elif choice == 2:
           if booking[5:10] == ['X','X','X','X','X']:
               print('Economy is full.')
           else:
            economy()
#if the client chooses 3, it will say the following and take us to the exit function
        elif choice == 3:
            print('Thank you for using our service.')
            exit()
       
#in case the user does not choose 1, 2 or 3, we will display the following message and call menu one more time.        
        else:
            print('Invalid number. Try again.')
            print('\n')
            menu()
    print('Thank you for using our service.')
#after all the funcitons are ready, we call the main function.            
main()
