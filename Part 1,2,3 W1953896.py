# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20211125

#------------------- initializing veriables  -------------------------#
Pass = 0
Fail = 0
Defer = 0
progress = 0
module_trailer = 0
Exclude = 0
module_retriever = 0
stud_count = 0
record_list = []

#-------------------creating user define functions -------------------------#

def nxt():
    while True:
        Nxt = input("""Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results:""")
                
        if Nxt == "q" or Nxt == "Q":
            histogram()

        elif Nxt == "y"or Nxt == "Y":
            break
        else:
            print("")
            print("invalid responce please try again")
            print("")


def user_input_and_validation():
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

def text_file_records() :
    #------------------- creating text file -------------------------#
    try:
        f = open("myfile.txt", "x")
    except:
        pass
    #------------------- writing in the text file -------------------------#
    with open('myfile.txt', 'w') as n: # opening text file to write
        for i in range (0,len(record_list)):
            print (*record_list[i],file=n) # writing previous records in the file  
    print("")
    n.close()

    print("---------------------------------------------------------------")
    print("")
    print ("part #3")
    print ("Reading text file,")
    #------------------- reading the text file -------------------------#
    with open('myfile.txt', 'r') as fo: # opening text file to read
        print (fo.read()) # reading the text file 
    print("")
    fo.close()

def histogram():
    stud_count = progress + module_trailer + module_retriever + Exclude  # getting the student count
    
    #------------------- creating the histogram -------------------------#
    print ("""
---------------------------------------------------------------
Histogram """)
    print ("Progress "+str(progress)+": ",end="")
    for i in range (progress):
        print("*",end="")
    print("")
    print ("Trailer "+str(module_trailer)+": ",end="")
    for i in range (module_trailer):
        print("*",end="")
    print("")
    print ("Retriever "+str(module_retriever)+": ",end="")
    for i in range (module_retriever):
        print("*",end="")
    print("")
    print ("Exclude "+str(Exclude)+": ",end="")
    for i in range (Exclude):
        print("*",end="")
    print("")
    print(stud_count,"outcomes in total")
    print("----------------------------------------------------------------")
    print("")
    #------------------- printing input text_file_records -------------------------#
    print ("part #2")
    print("Printing entered records")
    for i in range (0,len(record_list)):
        print (*record_list[i])
    text_file_records()
    raise SystemExit


#------------------- Main program  -------------------------#

#------------------- selection of program from terminal  -------------------------#

while True:
    print("")
    print("part #1")
    print("")
    first_input = int(input("""Select the program output for;
1. student Program
2. staff program

Enter input number: """))

    #------------------- student program  -------------------------#
    if first_input == 1:
        while True:
        # -------------------Ask User for inputs and Validate -------------------------#
            user_input_and_validation()
            total_credits = Pass+Defer+Fail

            if total_credits == 120:
                # ------------------- Progress -------------------------#
                if Pass == 120:
                    print("")
                    print("Progress")
                    raise SystemExit

                # ------------------- progress - module trailer -------------------------#
                elif Pass == 100:
                    print("")
                    print("progress - module trailer")
                    raise SystemExit

                # ------------------- Exclude -------------------------#
                elif Fail >= 80:
                    print("")
                    print("Exclude")
                    raise SystemExit

                # ------------------- Do not Progress – module retriever -------------------------#
                else:
                    print("")
                    print("Do not Progress - module retriever")
                    raise SystemExit

            else:
                print("")
                print("""total credits are out of range
    please enter again below
    """)
        
    #------------------- staff program  -------------------------#
    elif first_input == 2:
        while True:
            #-------------------Ask User for inputs and Validate -------------------------#
            print("")
            user_input_and_validation()
            total_credits = Pass+Defer+Fail
            if total_credits == 120:
                #------------------- Progress -------------------------#
                if Pass == 120:
                    print("")
                    print("Progress")
                    progress = progress + 1
                    record = ["progress                               :"+str(Pass),str(Defer),str(Fail)]
                    record_list.append(record) # appending records entered to the record list
                    print("")                   
                    nxt()

                #------------------- progress - module trailer -------------------------#
                elif Pass == 100:
                    print("")
                    print("progress - module trailer")
                    module_trailer = module_trailer + 1
                    record = ["progress - module trailer              :"+str(Pass),str(Defer),str(Fail)]
                    record_list.append(record) # appending records entered to the record list
                    print("")
                    nxt()
                
                #------------------- Exclude -------------------------#
                elif Fail >= 80:
                    print("")
                    print("Exclude")
                    Exclude = Exclude + 1
                    record = ["Exclude                                :"+str(Pass),str(Defer),str(Fail)]
                    record_list.append(record) # appending records entered to the record list
                    print("")
                    nxt()
                
                #------------------- Do not Progress – module retriever -------------------------#
                else:
                    print("")
                    print("Do not Progress - module retriever")
                    module_retriever = module_retriever + 1
                    record = ["Do not Progress - module retriever     :"+str(Pass),str(Defer),str(Fail)]
                    record_list.append(record) # appending records entered to the record list
                    print("")
                    nxt()
            else :
                print("")
                print ("""total credits are out of range
please enter again below
""")  

    #------------------- providing error  -------------------------#    
    else :
        print("")
        print ("invalid input please try again") 
        print ("")
        

#------------------- references  -------------------------#
#1 “How Do I Print the Content of a .Txt File in Python?” Stack Overflow, 15 Aug. 2013, https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python
#2 “Python Exit Commands: Quit(), Exit(), sys.exit() and Os._Exit() - GeeksforGeeks.” GeeksforGeeks, 27 Dec. 2019, https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/  
