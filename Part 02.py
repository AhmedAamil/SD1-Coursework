# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20211096/ w1953895
# Date: 10/30/2022
'START'

# Part 01  A - D # This .py file Cont. with List (Part 02)
# The program version should allow student/Staff Members to predict their progression outcome at the end of each academic year.

# Initalizing Variables and import Modules
import time
pass_credit = 0   # Initializing variable for pass credit
defer_credit = 0  # Initializing variable for defer credit
fail_credit = 0   # Initializing variable for fail credit

# Initalizing Variables for Counting Progressions
progressCount = 0
trailerCount = 0
retrieverCount = 0
excludeCount = 0
progression = 0
output = ''

# Initalizing Variables for producing Histogram
progress = 0
trailer = 0
retriever = 0
exclude = 0

# Variables for List (Part 02)
progression_list = []

print ('''This program allows students/Staff Members to predict their progression outcome at the end of each academic year.''')

# Defining function(s)
def credit_range (credit, credit_type):  # If not in the range 0, 20, 40, 60, 80, 100 and 120
    "Validating the range 0, 20, 40, 60, 80, 100 and 120"
    while not credit in range (0,140,20):
        print ("Out of range")
        print ("\nPlease try Again")
        credit = int(input(f"Please enter your credits at {credit_type} : "))
    else:
        return credit

def list_output (progression_type): # Defining function for Part 02 – List (extension)
    "Appending progression output to a list"
    output = progression_type + ' - {}, {}, {}'.format (pass_credit,defer_credit,fail_credit)
    progression_list.append(output)

while True:

    try:
        user_input = ''
        
        # Input and Output
        print('\nPart 1 :')
        pass_credit = int(input("\nPlease enter your credits at PASS : "))  # User Input for Pass Credit
        pass_credit = credit_range (pass_credit, 'PASS')

        defer_credit = int(input("Please enter your credit at DEFER : ")) # User Input for Defer Credit
        defer_credit = credit_range (defer_credit, 'DEFER')

        fail_credit = int(input("Please enter your credit at FAIL : ")) # User Input for Fail Credit
        fail_credit = credit_range (fail_credit, 'FAIL')
       
        if not (pass_credit + defer_credit + fail_credit == 120):  # if total of pass, defer and fail credits is not 120.
          print('Total Incorrect')
          print("\nPlease try Again")

        else:
            if (pass_credit>=100): # If pass credit >= 100
                if (pass_credit==120): # If pass credit equal to 120 output Progress
                    time.sleep(1)
                    print('Progress')
                    progressCount += 1 # Adding the total progress outcomes
                    list_output ('Progress') # Adding the Progression results to a List

                else: # Else display Progress - module trailer
                    time.sleep(1)
                    print('Progress (module trailer)')
                    trailerCount += 1 # Adding the total module trailer outcomes
                    list_output ('Progress (module trailer)') # Adding the Progression results to a List

            elif (fail_credit>=80):  # Display Exclude if fail credit is greater than or equal to 80
                time.sleep(1)
                print('Exclude')
                excludeCount += 1 # Adding the total exclude outcomes
                list_output ('Exclude') # Adding the Progression results to a List

            else:   # Display progress-module retriever
                time.sleep(1)
                print('Do not Progress - Module retriever' )
                retrieverCount += 1 # Adding the total retriever outcomes
                list_output ('Module retriever') # Adding the Progression results to a List

            print ("\nYou're about to exit.")
            time.sleep(1)

            # User Input for continue or break
            while not (user_input=='Y' or user_input=='Q'):
                user_input = input('''\nWould you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results : ''')
                user_input = user_input.upper()
                
            if user_input == 'Y':
                print ("\nEnter your data")
                continue
    
            elif user_input == 'Q':
                print ('\nThanks for using Progression outcome Predictor')

                # Producing Histogram
                progress = progressCount * '*'
                trailer = trailerCount * '*'
                retriever = retrieverCount * '*'
                exclude = excludeCount * '*'
                progression = progressCount + trailerCount + retrieverCount + excludeCount

                print("————————————————————————————————————————————————————————————————————————————————")
                print ('Histogram')
                print('\nProgress', progressCount, '\t:', progress)
                print('Trailer', trailerCount, '\t:', trailer)
                print('Retriever', retrieverCount, '\t:', retriever)
                print('Excluded', excludeCount,'\t:', exclude)
                print()
                print(progression,' outcome(s) in total.') # Display Total Outcomes
                print("________________________________________________________________________________")

                # Part 02 - List (extension)
                print('\nPart 2 :')
                for count in progression_list:
                    print (count)
                print()
                break

            else:
                pass
            
    except ValueError:
        print("Integer required") # Invalid if not an integer
        continue
'STOP'


# Idea/Hint - https://stackoverflow.com/questions/58791012/