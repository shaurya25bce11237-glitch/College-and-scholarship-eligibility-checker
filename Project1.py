print("COLLEGE & SCHOLARSHIP ELIGIBILITY CHECKER TOOL") #project title

#Asking name from the user
name=input("Enter your full name:")
print("Hello",name)

#Dictionary containing colleges and their minimum eligibility requirements
#Each college has criteria for 10th marks,12th marks,JEE percentile and age
colleges={"IIT Roorkee":{  "min_10th":75, "min_12th":75,"min_jee":95,"min_age":17},
"NIT": {"min_10th":70,"min_12th":70, "min_jee":85,"min_age":17},
    "State College":    {"min_10th": 65,"min_12th":60,"min_jee": 70, "min_age":17},
    "Delhi University":{"min_10th":55,"min_12th":50,"min_jee":0,"min_age":16},
    "XYZ University":   {"min_10th":40,"min_12th":40,"min_jee":0,"min_age": 16}}

# Dictionary containing scholarships and their eligibility criteria
# Scholarships consider academic marks, family income, gender, and sports achievements
scholarships={"Merit Scholarship":{"min_10th":90,"min_12th":90 ,"min_jee" :0, "family_income": 500000},
"Economically Weaker Section": {"min_10th": 60, "min_12th": 60, "min_jee": 0, "family_income": 800000},
"Sports Scholarship":{"min_10th":50,"min_12th": 50,"min_jee":0,"sports_level":"state"},
 "Girl Child Scholarship":{"min_10th":60, "min_12th": 60,"min_jee": 0,"gender":"female"}}
#Starting a while loop till user exits the program
while True:
    #Inteface for the user
    print("\n1.Check eligibility for colleges")
    print("2.Check eligibility for scholarships")
    print("3.Exit the program")
#Taking input from the user
    inp1=int(input("Enter your choice from 1 to 3:"))

    if inp1 ==1:
        print("COLLEGE ELIGIBILITY CHECKER")
#Taking required information from the user
        age= int(input("What is your age?: "))
        tenth=int(input("Percentage in class 10th: "))
        twelveth=int(input("Percentage in class 12th: "))
        jee=int(input("Your JEE percentile: "))
#Making a empty list to store the eligible colleges
        eligible_colleges=[]
#for loop to iterate over each element of dictionary and checking against the minimum criteria
        for college,criteria in colleges.items():
            #Verify if user meets all minimum requirements for this college
            if(age>= criteria["min_age"] and
                 tenth >= criteria["min_10th"] and
                twelveth>=criteria["min_12th"] and
                jee>=criteria["min_jee"]):
                #Add college to eligible list if all criteria are met
                eligible_colleges.append(college)
        #Displaying result
        print(f"\nHello {name},you are eligible for:")
        if eligible_colleges:
            count = 1
            for college in eligible_colleges:
                print(f"{count}.{college}")
                count += 1
        #If no colleges are found then print statement
        else:
                print("No colleges found.")

    #2:Scholarship eligibility check
    elif inp1 ==2:
        print("\nSCHOLARSHIP ELIGIBILITY CHECK")
        #Collect academic and personal information for scholarship check
        tenth=int(input("Percentage in class 10th: "))
        twelveth=   int(input("Percentage in class 12th: "))
        family_income= int(input("Annual family income (in INR): "))
        gender =input("Gender (male/female): ")
        sports_level =input("Sports level (none/school/state/national): ")
        #Creating a list to store eligible scholarships
        eligible_scholarships=[]
        #Checking each scholarship's eligibility criteria
        for scholarship, criteria in scholarships.items():
            #We are assuming here that the user is eligible for all scholarships
            eligible =True

# Iterating each scholarship against the given input
            if tenth<criteria["min_10th"] or twelveth<criteria["min_12th"]:
                eligible= False
            if"family_income" in criteria and family_income>criteria["family_income"]:
                eligible =False
            if"gender" in criteria and gender != criteria["gender"]:
                eligible= False
            if"sports_level" in criteria:
                if criteria["sports_level"] =="state" and sports_level not in ["state","national"]:
                    eligible = False
                elif criteria["sports_level"]  =="national" and sports_level!="national":
                    eligible = False
            if eligible:
                eligible_scholarships.append(scholarship)

#Printing eligible scholarships
        print(f"\nHello {name}, you are eligible for these scholarships:")
        if eligible_scholarships:
            count = 1
            for scholarship in eligible_scholarships:
                print(f"{count}. {scholarship}")
        else:
            #If no scholarships are available print a statement
            print("No scholarships available.")
    #For exiting the program
    elif inp1 ==3:
        print(("Good luck with your future studies!"))
        break
    #For Invalid Inputs
    else:
        print("Invalid input!,Please enter 1,2,or3 only")