import mysql.connector as m
mydb=m.connect(
    host=&quot;localhost&quot;,
    user=&quot;root&quot;,
    password=&quot;password&quot;)
c=mydb.cursor()
c.execute(&quot;create database hospital&quot;)
c.execute(“use hospital”)
c.execute(&quot;create table cleveland(Name
varchar(15),Age integer(3),Weight
integer(5),Height integer(4),Medical history
varchar(20),Temperature integer(4),Blood
Pressure integer (3),Doctor varchar(30)&quot;)
print(&quot;-----------------------------------------------------
------&quot;)


print(&quot;Hey, Welcome to Cleveland
Healthcare!&quot;)
print(&quot;-----------------------------------------------------
------&quot;)
con=int (input(&quot;Hi, enter 1 to begin&quot;))
while con == 1:
    client=int(input(&quot;If you are a new
customer enter 1\nif you are a doctor, enter
2\n\n&quot;))
    print(&quot;-------------------------------------------------
----------&quot;)
    if client == 1:
        print(&quot;Hi! We are glad that you came to
the state of the art healthcare provider -
Cleveland Healthcare\nAs you are a new
patient, we will require some details:&quot;)
        fname=input(&quot;enter your first name&quot;)
        print(&quot; &quot;)
        lname=input(&quot;enter your Last name&quot;)
        print(&quot; &quot;)


        name=fname +&quot; &quot;+lname
        print(&quot;Thank you&quot; ,name,&quot;,\nnow our
chatbot will be asking some basic details
about you and your medical history.&quot;)
        print(&quot; &quot;)
        age=int(input(&#39;please enter your age&#39;))
        print(&quot; &quot;)
        weight=int(input(&quot;enter your weight in
kilograms&quot;))
        print(&quot; &quot;)
        height=int(input(&quot;enter your height in
centimeters&quot;))
        print(&quot; &quot;)
        medhis=input(&quot;if you have any
medical allergies or any chronic disease ,
please specify. (if none, type no) &quot;)
        print(&quot; &quot;)
        fever= input(&quot;if you have checked your
temperature in the last 2 days, please
specify. ( if no, type no)&quot;)


        print(&quot; &quot;)
        pressure= input(&quot;if you have checked
your blood pressure in the last 2 days,
please specify. ( if no, type no)&quot;)
        print(&quot; &quot;)
        if age &lt; 16:
            field = &quot;pediatrics&quot;
            print(&quot;The Doctor is Andrew
Sebastian&quot;)
        else:
            field = int(input(&quot; please type the
field number of the medical issue you wish
to consult today.\n 1- cardiology ( heart) \n
2-Neurology (Brain) \n 3- Polmonary \n 4-
Traumotology \n 5-Dentistry (Tooth and
Gum) \n 6-General Physician \n 7-Other&quot;))
            if field ==1:
              field = &quot;cardiology&quot;
              print(&quot;The Doctor is Dr. Harrison
Samuel&quot;)


            elif field ==2:
              field = &quot;Neurology&quot;
              print(&quot;The Doctor is Dr. James
Alexander&quot;)
            elif field ==3:
              field = &quot;Polmonory&quot;
              print(&quot;The Doctor is Dr. Jack
Barnes&quot;)
            elif field ==4:
              field = &quot;Traumatology&quot;
              print(&quot;The Doctor is Dr. Gary
Lynch&quot;)
            elif field ==5:
              field = &quot;Dentistry&quot;
              print(&quot;The Doctor is Dr.Thomas
Henry&quot;)
            elif field ==6:
              field = &quot;General Physician&quot;
              print(&quot;The Doctor is Dr. Michael
Garett&quot;)


            else:
          
              field = &quot;Other&quot;
              print(&quot;The Doctor is Dr. Steven
Castillo&quot;)
    print(&quot;Thank You for your cooperation,
we appreciate it.&quot;)
    print(&quot; &quot;)
    print(&quot;Here is the summary of your
responses&quot;)
    print(&quot; &quot;)
    print(&quot;Name:&quot;, name)
    print(&quot; &quot;)
    print(&quot;Age:&quot;, age)
    print(&quot; &quot;)
    print(&quot;Weight:&quot;, weight)
    print(&quot; &quot;)
    print(&quot;Height:&quot;, height)
    print(&quot; &quot;)
    print(&quot;Medical History:&quot;, medhis)


    print(&quot; &quot;)
    print(&quot;Fever:&quot;, fever)
    print(&quot; &quot;)
    print(&quot;Pressure:&quot;, pressure)
    print(&quot; &quot;)
    print(&quot;Doctor:&quot;, field)
    print(&quot; &quot;)
c.execute(&quot;insert into cleveland
values(name,age,weight,height,medhis,
fever,pressure,field )&quot;)
c.execute(&quot;desc cleveland&quot;)
    print(&quot;Thank You, You may proceed.
Next customer.&quot;)
    print(&quot; &quot;)
while con == 2:
    client=int(input(&quot;Hi doctor, if you would
you like to see your list of patients please
enter 1&quot;))
    if client==1:
      print(&quot; &quot;)
      print(&quot;Here is the summary of your
patients responses&quot;)
      print(&quot; &quot;)
      print(&quot;Name:&quot;, name)
      print(&quot; &quot;)
      print(&quot;Age:&quot;, age)
      print(&quot; &quot;)
      print(&quot;Weight:&quot;, weight)
      print(&quot; &quot;)
      print(&quot;Height:&quot;, height)
      print(&quot; &quot;)
      print(&quot;Medical History:&quot;, medhis)
      print(&quot; &quot;)
      print(&quot;Fever:&quot;, fever)
      print(&quot; &quot;)
      print(&quot;Pressure:&quot;, pressure)
      print(&quot; &quot;)
      print(&quot;Doctor:&quot;, field)
      print(&quot; &quot;)
