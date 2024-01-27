# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20211125

dictionary = {}

def id_validation():
    while True:
        global id_num
        id_num = input("enter Id number:").upper()#getting Id number
        if len(id_num) == 8 and id_num[0] == 'W'and id_num[1:8].isnumeric():# validating ID number
            if  id_num not in dictionary: #checking wether ID number exist in the ditionary  
                return id_num
            else:
                print("Id alreday exists please try again")
        else:
            print("invalid Id number please try again") 

def input_and_validation():
    #------------------- defining global veriables -------------------------#
    global Pass,Defer,Fail

    #------------------- getting and validating Pass input -------------------------#
    while True:
        try:
            Pass = int(input("Enter you PASS credits:")) #getting pass input
        except:
            print ("integer required")
            continue
        if Pass > 120: # validating wether the input is lesser than or equal to 120
            print ("out of range")
        elif Pass == 0 or Pass == 20 or Pass == 40 or Pass == 60 or Pass == 80 or Pass == 100 or Pass == 120:
            break 
        else:
            print ("out of range")

    #------------------- getting and validating defer input -------------------------#
    while True:
        try:
            Defer = int(input("Enter you Defer credits:")) #getting Defer input
        except:
            print ("integer required")
            continue
        if Defer > 120: # validating wether the input is lesser than or equal to 120
            print ("out of range")
        elif Defer == 0 or Defer == 20 or Defer == 40 or Defer == 60 or Defer == 80 or Defer == 100 or Defer == 120:
            break 
        else:
            print ("out of range") 

    #------------------- getting and validating fail input -------------------------#    
    while True:
        try:
            Fail = int(input("Enter you Fail credits:")) #getting Fail input
        except:
            print ("integer required")
            continue
        if Fail > 120: # validating wether the input is lesser than or equal to 120
            print ("out of range")
        elif Fail == 0 or Fail == 20 or Fail == 40 or Fail == 60 or Fail == 80 or Fail == 100 or Fail == 120:
            break 
        else:
            print ("out of range")
            
def nxt():
    while True:
        Nxt = input("""Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results:""")

        if Nxt == "q" : 
            final_dictionary = str(dictionary).replace("(","").replace(")","").replace("'","").replace("{","").replace("}","") # removing "(",")","'","{","}" in the dictionary 
            print(final_dictionary) # printing the dictiobary 
            raise SystemExit
        elif Nxt == "y":
            break 
        else:
            print ("invalid response. Please enter again")

#------------------- main program -------------------------#
while True:
    id_validation()
    input_and_validation()
    total = Pass+Defer+Fail
    if total == 120 :
        if Pass == 120 :
            # progress
            dictionary[id_num]="Progress :" +str(Pass),str(Defer),str(Fail) # entering to the dictionary 
            nxt()
                
        elif Pass == 100:
            # progress - module trailer
            dictionary[id_num]="progress - module trailer :"+str(Pass),str(Defer),str(Fail) # entering to the dictionary 
            nxt()
                
        elif Fail >= 80:
            # Exclude
            dictionary[id_num]="Exclude :"+str(Pass),str(Defer),str(Fail) # entering to the dictionary 
            nxt()
                
        else :
            # Do not Progress – module retriever
            dictionary[id_num]="Do not Progress - module retriever :"+str(Pass),str(Defer),str(Fail) # entering to the dictionary 
            nxt()
                
    else:
        print("invalid response please try again")

#------------------- references  -------------------------#
#1 “Python String Methods.” Python String Methods, https://www.w3schools.com/python/python_ref_string.asp 
#2 “Python String Replace() Method.” Python String Replace() Method, https://www.w3schools.com/python/ref_string_replace.asp
#3 “Python Dictionaries.” Python Dictionaries, https://www.w3schools.com/python/python_dictionaries.asp
