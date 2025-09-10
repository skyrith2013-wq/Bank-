import json , random , time , os
from datetime import datetime

def main():
    # try:
    class Bank():

        # current_user

        def set_current_user(self, acc_no, pin, mobile):
            with open(self.filename, "r") as J:
                accounts = json.load(J)    
            for inx,u in enumerate(accounts):
                try:
                    if (
                        u["Account Number"] == acc_no
                        and int(u["PIN"]) == int(pin)
                        and int(u["Mobile Number"]) == int(mobile)
                    ):
                        self.current_user = u
                        self.current_index = inx
                        return True
                except (KeyError, ValueError, TypeError):
                    continue
            return False
        
        # WORKING

        def working(self):
            self.greeting()
            NO = input("You Are New Or Old ? --> ").lower()
            if NO.isdigit():
                print("Enter Something Valid!")

            if NO == "new":
                self.new_user()
            elif NO == "old":

                input("Enter Your Name --> ")
                acc_no = input("Enter Account Number --> ")
                pin = input("Enter PIN --> ")
                mobile = int(input("Enter Your Mobile Number --> "))

                self.set_current_user(acc_no, pin, mobile)
                print("\n1 : Cheak Bank Balance\n2 : Withdraw Money\n3 : Deposite Money\n4 : Obtain Intrest\n")
                choice = int(input("What Do You Wanna Do ? --> "))
                if choice == 1:
                    self.bank_balance()
                elif choice == 2:
                    self.Withdraw_Money()
                elif choice == 3:
                    self.Deposite_Money()
                elif choice == 4:
                    self.intrest()
                else:
                    print("Enter A Valid Number!")

            else:
                print("Enter something valid!")

        # GREETING

        @staticmethod
        def greeting():
            try:
                ct =  datetime.now().hour
                if ct < 12:
                    print("\n     Good Morning")
                elif ct < 17:
                    print("\n     Good Afternoon")
                else:
                    print("\n     Good Evening")
            finally:
                print("""\n<====================>
Welcome To CBSE Bank
<====================>\n""")

        # READING BANK BALANCE

        def __init__(self , filename = "CBSE_Store.json"):
            self.filename = filename
            try:
                with open(self.filename, "r") as file:
                    content = file.read().strip()
                    if content:
                        loaded = json.loads(content)
                        if isinstance(loaded , list):
                            self.data = loaded
                        else:
                            self.data = [loaded] 
                    else:
                        self.data = {}

            except FileNotFoundError:
                self.current_user = {}

        def bank_balance(self):
            if not self.current_user: return
            print(f"Welcome Back {self.current_user['Name']},")
            print(f"Your Bank Balance is {self.current_user['Bank Balance']} ₹")

        # STORE current_user
    
        def storing(self):
            try:
                with open(self.filename, "r") as J:
                    accounts = json.load(J)
                    if not isinstance(accounts, list):
                        accounts = [accounts]
            except (FileNotFoundError, json.JSONDecodeError):
                accounts = []

            if hasattr(self, "current_index"):
                accounts[self.current_index] = self.current_user
            else:
                print("⚠️ Error: current user index not found, cannot update safely.")
                return

            with open(self.filename ,"w") as f:
                json.dump(accounts , f , indent=4)

        # NEW USER
        
        def new_user(self):
                while True:
                    self.time = time.time()
                    print("Let's Create A Account For You!\n")
                    self.name = input("Enter Your Name --> ")
                    if self.name.isdigit():
                        print("Enter A Valid Name!")
                        continue

                    self.Fname = input("Enter Your father's name --> ")
                    if self.Fname.isdigit():
                        print("Enter a proper name!")
                        continue 

                    self.Mname = input("Enter Your mother's name --> ")
                    if self.Mname.isdigit():
                        print("Enter a proper name!")
                        continue 

                    self.Mobile_Number = int(input("Enter Your Mobile Number --> "))
                    if len(str(self.Mobile_Number)) != 10:
                        print("Enter A Valid Moblie Number!")
                        continue

                    self.DOB = int(input("Enter Your Date of birh (DDMMYYYY) --> "))
                    self.Date_Of_Birth = f"{str(self.DOB)[0:2]}-{str(self.DOB)[2:4]}-{str(self.DOB)[4:8]}"
                    self.DOB_STR = str(self.DOB)
                    if len(self.DOB_STR) != 8:
                        continue
                    elif datetime.now().year - int(self.DOB_STR[4:8]) < 18:
                        print("You must be at least 18 years old.")
                        continue

                    self.PIN = int(input("Enter Your 4-digit PIN --> "))
                    if len(str(self.PIN)) != 4:
                        continue

                    self.Adhar = int(input("Enter Your Adhar Number --> "))
                    if len(str(self.Adhar)) != 12:
                        continue

                    self.PAN = int(input("Enter Your PAN Number --> "))
                    if len(str(self.PAN)) != 10:
                        continue
                    
                    time.sleep(3)
                    print(f"{self.name}, Your Account Is Sucssesfully created  ")
                    self.money = int(input("please Make Your First Transtiction --> "))

                    x = int(input("Enter Your Account Number --> "))
                    if len(str(x)) != 12:
                        print("Enter A valid Account Number!")
                        continue
                    y = int(input("Enter Your PIN --> "))
                    if len(str(y)) != 4:
                        print("Enter A valid PIN!")
                        continue
                        
                    self.acc_no = str(random.randint(100000000000, 999999999999))
                    print(f"""your account contain {self.money} ₹ and,
Your account number is {self.acc_no} (Kindly Save This In A Safe Place)""")
                    break

                data = {
                        "Name": self.name,
                        "D.O.B": self.Date_Of_Birth,
                        "Father Name": self.Fname,
                        "Mother Name": self.Mname,
                        "Mobile Number": self.Mobile_Number,
                        "PIN": self.PIN,
                        "PAN": self.PAN,
                        "Adhar": self.Adhar,
                        "Account Number": self.acc_no,
                        "Bank Balance": self.money,
                        "Last Intrested": self.time
                    }

                filename = "CBSE_Store.json"
                if os.path.exists(filename):
                    with open(filename, "r") as J:
                        try:
                            accounts = json.load(J)
                            if not isinstance(accounts, list):
                                accounts = [accounts]
                        except json.JSONDecodeError:
                            accounts = []
                else: 
                    accounts = []
                accounts.append(data)

                with open(filename, 'w') as J:
                    json.dump(accounts, J,indent=4)

        # WITHDRAW MONEY

        def Withdraw_Money(self):
            if not self.current_user: return
            WM = int(input("Enter Money To Be Withdraw --> "))
            if WM < 0:
                print("Enter A valid Number")
                exit()

            if self.current_user['Bank Balance'] >= WM:
                OBB = self.current_user['Bank Balance']
                NBB = OBB - WM
                print(f'Your Old Bank Balance Was {OBB} and Your New Bank Balance is {NBB}')
                self.current_user['Bank Balance'] = NBB
                self.storing()
            else:
                print("Insufficient Balance!")


        # DEPOSITE MONEY

        def Deposite_Money(self):
            if not self.current_user: return
            while True:
                DM = int(input("Enter Money To Be Deposited --> "))
                if DM < 0:
                    print("Enter A valid Number")
                    continue

                x = int(input("Enter Account Number --> "))
                if len(str(x)) != 12:
                    print("Enter A valid Account Number!")
                    continue
                y = int(input("Enter PIN --> "))
                if len(str(y)) != 4:
                    print("Enter A valid PIN!")
                    continue

                OBB = self.current_user['Bank Balance']
                NBB = OBB + DM
                print(f"Your Old Bank Balance Was {OBB},\nAnd Your New Bank Balance Is {NBB}")
                self.current_user['Bank Balance'] = NBB
                self.storing()
                break

        # INTREST

        def intrest(self):
                if not self.current_user: return
                if self.current_user['Last Intrested'] - time.time() >= 2592000:
                    intrest = self.current_user['Bank Balance'] * 0.05
                    total = self.current_user['Bank Balance'] * 1.05
                    self.current_user['Last Intrested'] += 2592000
                    self.storing()
                    print(f"You Recived The Intrest Of {intrest} So, the total is {total}")
                    self.current_user['Bank Balance'] += intrest
                    self.storing()

                else:
                    IID = round((2592000 + self.current_user['Last Intrested'] - time.time())/86400, 0)
                    print(f"You Will Be Intrested After {int(IID)} days")

    #  RUNNING PANNEL

    bank = Bank()
    bank.working()



if __name__ == "__main__":
    main()