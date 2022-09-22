import datetime
import mysql.connector
card=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="atm_1"
    
)
mycursor=card.cursor()
sql="insert into user_details(name,language,transaction_type,amount)values(%s,%s,%s,%s)"
val=("sathya","English","deposite",6000)
mycursor.execute(sql,val)
card.commit()
x= datetime.datetime.now()
print(x)
print("*************************!!!Welcome to indian Bank ATM!!!*******************************")

print("STEP 1:*************** please! insert your credit card ************")
try:
    print("Enter valid number only 0 or 1")

    card_valid_no=int(input("Enter your card valid number:"))

    if card_valid_no==0:


         print("your credit card is invalid and try agian")
    elif card_valid_no==1:

        print("your credit card is valid and properly insert")

        print("STEP 2: ********** Select your language!************")

        print("1.Tamil")

        print("2.English")

        print("3.Hindi")

        print("4.malayalam")

        language=int(input("select your language:"))

        def tamil():

             print("your select language is Tamil !!")

        def english():

            print("your select language is English !!")

        def hindi():

            print("your select language is Hindi !!")

        def malayalam():

            print("your select language is malayalam !!")

        if language==1:

            tamil()
        elif language==2:

             english()
        elif language==3:

            hindi()
        elif language==4:

            malayalam()     
        print("STEP 3:  Enter your 4 digit**** ATM pin  number!!")

        pin_no=int(input("Enter your 4 digit pin number:"))

        if pin_no>1000:

           print("your ATM pin number is correct!!")
        else:

           print("sorry!! your pin number is incorrect")

        print("STEP 4: ************ select your Account type!!*************************")

        account=input("choose your account type savings/ current:")

        if account=="savings":

            print("your account type is !!savings account!!")
        else:

            print("your account type is !!current account !!")

        print("STEP 5: ******Transaction type!!*******")


        print("select option 1 (or) 2")

        print("1.withdraw a money")

        print("2.deposite a money")
            

        option=int(input("select your transaction type:"))

        def withdraw(balance):

           amount=int(input("Enter your withdrawal amount:"))

           if amount<10000:

            print(f"your withdrawal amount is{amount}")

            print("widthdraw a cash!!! ")

            x=amount-balance
            print(f"your current balance is{x}")
            print("Remove your ATM card!!")

           else:

            print("your amount is 100000 above!Not transaction")
    
        def deposite():

            t1=int(input("enter your deposite amount:"))

            if t1>=100:

               print(f"your deposite amount is{t1}")
            else:

              print("maximum deposite amount is 100")
    
        if option==1:

         withdraw(10000)

        elif option==2:

          deposite()
except:
    print("valid number is incorrect!!")









                                

