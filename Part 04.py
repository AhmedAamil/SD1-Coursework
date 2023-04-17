# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20211096/ w1953895
# Date: 31/10/2022
'START'

# Part 01  A - D # This .py file is a separated program for the dictionary (Part 04)
# The program version should allow student/Staff Members to predict their progression outcome at the end of each academic year.

# Initalizing Variables and import Modules
import time
StudentID = ''
pass_credit = 0   # Initializing variable for pass credit
defer_credit = 0  # Initializing variable for defer credit
fail_credit = 0   # Initializing variable for fail credit

# Variables for Counting Progressions
progressCount = 0
trailerCount = 0
retrieverCount = 0
excludeCount = 0
progression = 0
output = ''

# Variables for producing Histogram
progress = 0
trailer = 0
retriever = 0
exclude = 0

# Variables for Lists (Part 02 and Part 04)
dic_list = []

# Variables for Dictionary (Part 04)
progression_dic = {}

print ('''This program allows students/Staff Members to predict their progression outcome at the end of each academic year.\n''')

# Defining function(s)
def credit_range (credit, credit_type):  # If not in the range 0, 20, 40, 60, 80, 100 and 120
    " Validating the range 0, 20, 40, 60, 80, 100 and 120"
    while not credit in range (0,140,20):
        print ("Out of range")
        print ("\nPlease try Again")
        credit = int(input(f"Please enter your credits at {credit_type} : "))
    else:
        return credit

def list_output (progression_type): # Defining function Lists (Part 02, Part 03, Part 04)
    "Appending progression output to a list"
    output = progression_type + ' - {}, {}, {}'.format (pass_credit,defer_credit,fail_credit)
    dic_list.append(output) #  Appending progression I/O Data for Dictionary

def dic_output(): # Defining function Dictionary (Part 04)
    " Adding progression output to a Dictionary"
    strList = '  '.join(dic_list)
    progression_dic [StudentID] = strList
    
while True:
    try:
        dic_list = []
        user_input = ''
# Input
        # Input Student ID(s)
        StudentID = str(input("Enter the unique Student ID : "))            
        StudentID = StudentID.lower()
        while StudentID[0] != 'w' or len(StudentID) != 8: #Correct this
            print ("\nInvalid Student ID. Student Id Should Starts with 'w' in the begining and must have the length of '8'")
            StudentID = input("Enter the unique Student ID : ")
            continue
        else:
            if StudentID in progression_dic:                                        
                print ('\nStudent ID already exists')
                continue
        
        print('\nPart 1 :')
        # Input Credits
        pass_credit = int(input("Please enter your credits at PASS : "))  # User Input for Pass Credit
        pass_credit = credit_range (pass_credit, 'PASS')

        defer_credit = int(input("Please enter your credit at DEFER : ")) # User Input for Defer Credit
        defer_credit = credit_range (defer_credit, 'DEFER')

        fail_credit = int(input("Please enter your credit at FAIL : ")) # User Input for Fail Credit
        fail_credit = credit_range (fail_credit, 'FAIL')

        if not (pass_credit + defer_credit + fail_credit == 120):  # If total of pass, defer and fail credits is not 120.
          print('Total Incorrect')
          print ('\nRestarting' )
          time.sleep(1)
          print("\nPlease try Again")

        else:
            if (pass_credit>=100): # If pass credit >= 100
                if (pass_credit==120): # If pass credit equal to 120 output Progress
                    time.sleep(1)
                    print('Progress')
                    progressCount += 1 # Adding the total progress outcomes
                    list_output ('Progress') # Adding the Progression results to a List
                    dic_output() # Adding I/O progression data to a dictionary
                    
                else: # Else display Progress - module trailer
                    time.sleep(1)
                    print('Progress (module trailer)')
                    trailerCount += 1 # Adding the total module trailer outcomes
                    list_output ('Progress (module trailer)') # Adding the Progression results to a List
                    dic_output() # Adding I/O progression data to a dictionary
                    
            elif (fail_credit>=80):  # Display Exclude if fail credit is greater than or equal to 80
                time.sleep(1)
                print('Exclude')
                excludeCount += 1 # Adding the total exclude outcomes
                list_output ('Exclude') # Adding the Progression results to a List
                dic_output() # Adding I/O progression data to a dictionary
                
            else:   # Display progress-module retriever
                time.sleep(1)
                print('Do not Progress - Module retriever' )
                retrieverCount += 1 # Adding the total retriever outcomes
                list_output ('Module retriever') # Adding the Progression results to a List
                dic_output() # Adding I/O progression data to a dictionary
                
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
              
                #Part 04 – Dictionary (Separate Program)
                print('\nPart 4 :')
                for c, i in progression_dic.items(): # Output retrieved from dictionary using items()
                    print (c,': ',i)
                print()
                break
            else:
                pass
            
    except ValueError :
        print("Integer required") # Invalid if not an integer
        print ('\nRestarting' )
        time.sleep(1)
        print ('Try again')
        continue

    except IndexError :
        print ("\nIndex out of range. Try again")



'STOP'
# https://realpython.com/iterate-through-dictionary-python/
# .format() - https://www.w3schools.com/python/ref_string_format.asp
# Idea/Hints - https://stackoverflow.com/questions/58791012/