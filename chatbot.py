import mysql.connector as m

# Establish a connection to the MySQL database
mydb = m.connect(
    host="localhost",
    user="root",
    password="password")

# Get a cursor to the database
c = mydb.cursor()

# Execute SQL commands to create and use the database
c.execute("create database hospital")
c.execute("use hospital")

# Create a table named 'cleveland' in the 'hospital' database
c.execute("create table cleveland(Name varchar(15), Age integer(3), Weight integer(5), Height integer(4), Medical history varchar(20), Temperature integer(4), Blood Pressure integer (3), Doctor varchar(30))")

# Print welcome messages
print("-----------------------------------------------------")
print("Hey, Welcome to Cleveland Healthcare!")
print("-----------------------------------------------------")

con = int(input("Hi, enter 1 to begin"))

while con == 1:
    client = int(input("If you are a new customer enter 1\nif you are a doctor, enter 2\n\n"))
    print("-------------------------------------------------")
    
    if client == 1:
        # Get the patient's details
        fname = input("enter your first name")
        lname = input("enter your Last name")
        name = fname + " " + lname
        age = int(input('please enter your age'))
        weight = int(input("enter your weight in kilograms"))
        height = int(input("enter your height in centimeters"))
        medhis = input("if you have any medical allergies or any chronic disease, please specify. (if none, type no)")
        fever = input("if you have checked your temperature in the last 2 days, please specify. ( if no, type no)")
        pressure = input("if you have checked your blood pressure in the last 2 days, please specify. ( if no, type no)")
        
        if age < 16:
            field = "pediatrics"
            print("The Doctor is Andrew Sebastian")
        else:
            # Ask the patient to choose a field of medical issue
            field = int(input(" please type the field number of the medical issue you wish to consult today.\n 1- cardiology ( heart) \n 2-Neurology (Brain) \n 3- Polmonary \n 4- Traumotology \n 5-Dentistry (Tooth and Gum) \n 6-General Physician \n 7-Other"))
            
            # Assign doctors based on the chosen field
            if field == 1:
                field = "cardiology"
                print("The Doctor is Dr. Harrison Samuel")
            elif field == 2:
                field = "Neurology"
                print("The Doctor is Dr. James Alexander")
            elif field == 3:
                field = "Polmonory"
                print("The Doctor is Dr. Jack Barnes")
            elif field == 4:
                field = "Traumatology"
                print("The Doctor is Dr. Gary Lynch")
            elif field == 5:
                field = "Dentistry"
                print("The Doctor is Dr.Thomas Henry")
            elif field == 6:
                field = "General Physician"
                print("The Doctor is Dr. Michael Garett")
            else:
                field = "Other"
                print("The Doctor is Dr. Steven Castillo")
        
        # Insert the patient's details into the 'cleveland' table
        c.execute(f"insert into cleveland values({name},{age},{weight},{height},{medhis},{fever},{pressure},{field})")
        c.execute("desc cleveland")
