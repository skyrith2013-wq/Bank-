import json, random, time, os
from datetime import datetime

def main():
    # Define the Bank class which manages accounts, balances, and transactions
    class Bank:

        # Constructor: initialize filename and load existing data if available
        def __init__(self, filename="CBSE_Store.json"):
            self.filename = filename
            try:
                # Try reading existing bank account data
                with open(self.filename, "r") as file:
                    content = file.read().strip()
                    if content:
                        loaded = json.loads(content)
                        # Ensure the data is stored as a list of accounts
                        self.data = loaded if isinstance(loaded, list) else [loaded]
                    else:
                        self.data = []
            except FileNotFoundError:
                # If no file exists yet, start with an empty data list
                self.data = []
            self.current_user = {}

        # Identify and set the current user from stored accounts
        def set_current_user(self, acc_no, pin, mobile):
            with open(self.filename, "r") as J:
                accounts = json.load(J)
            for inx, u in enumerate(accounts):
                try:
                    # Match account details with user input
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

        # Main function to interact with user
        def working(self):
            self.greeting()
            NO = input("You Are New Or Old ? --> ").lower()

            if NO.isdigit():
                print("Enter Something Valid!")

            if NO == "new":
                # Create a new account
                self.new_user()

            elif NO == "old":
                # Login existing account
                input("Enter Your Name --> ")
                acc_no = input("Enter Account Number --> ")
                pin = input("Enter PIN --> ")
                mobile = int(input("Enter Your Mobile Number --> "))

                # Authenticate user
                self.set_current_user(acc_no, pin, mobile)

                # Provide menu options
                print("\n1 : Check Bank Balance\n2 : Withdraw Money\n3 : Deposit Money\n4 : Obtain Interest\n")
                choice = int(input("What Do You Wanna Do ? --> "))

                # Choose operation
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

        # Static greeting message with time-based salutation
        @staticmethod
        def greeting():
            try:
                ct = datetime.now().hour
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

        # Display the current user's bank balance
        def bank_balance(self):
            if not self.current_user:
                return
            print(f"Welcome Back {self.current_user['Name']},")
            print(f"Your Bank Balance is {self.current_user['Bank Balance']} ₹")

        # Save the updated account data back to the JSON file
        def storing(self):
            try:
                with open(self.filename, "r") as J:
                    accounts = json.load(J)
                    if not isinstance(accounts, list):
                        accounts = [accounts]
            except (FileNotFoundError, json.JSONDecodeError):
                accounts = []

            # Update the current user's record
            if hasattr(self, "current_index"):
                accounts[self.current_index] = self.current_user
            else:
                print("⚠️ Error: current user index not found, cannot update safely.")
                return

            with open(self.filename, "w") as f:
                json.dump(accounts, f, indent=4)

        # Create a new user account
        def new_user(self):
            while True:
                self.time = time.time()
                print("Let's Create A Account For You!\n")

                # Gather user details with validation
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

                # Validate mobile number
                self.Mobile_Number = int(input("Enter Your Mobile Number --> "))
                if len(str(self.Mobile_Number)) != 10:
                    print("Enter A Valid Mobile Number!")
                    continue

                # Validate date of birth and age
                self.DOB = int(input("Enter Your Date of Birth (DDMMYYYY) --> "))
                self.Date_Of_Birth = f"{str(self.DOB)[0:2]}-{str(self.DOB)[2:4]}-{str(self.DOB)[4:8]}"
                self.DOB_STR = str(self.DOB)
                if len(self.DOB_STR) != 8:
                    continue
                elif datetime.now().year - int(self.DOB_STR[4:8]) < 18:
                    print("You must be at least 18 years old.")
                    continue

                # PIN validation
                self.PIN = int(input("Enter Your 4-digit PIN --> "))
                if len(str(self.PIN)) != 4:
                    continue

                # Aadhaar validation
                self.Adhar = int(input("Enter Your Aadhaar Number --> "))
                if len(str(self.Adhar)) != 12:
                    continue

                # PAN validation
                self.PAN = int(input("Enter Your PAN Number --> "))
                if len(str(self.PAN)) != 10:
                    continue

                # Create initial deposit and account number
                time.sleep(3)
                print(f"{self.name}, Your Account Is Successfully Created")
                self.money = int(input("Please Make Your First Transaction --> "))

                x = int(input("Enter Your Account Number --> "))
                if len(str(x)) != 12:
                    print("Enter A Valid Account Number!")
                    continue
                y = int(input("Enter Your PIN --> "))
                if len(str(y)) != 4:
                    print("Enter A Valid PIN!")
                    continue

                self.acc_no = str(random.randint(100000000000, 999999999999))
                print(f"""Your account contains {self.money} ₹ and,
Your account number is {self.acc_no} (Kindly Save This In A Safe Place)""")
                break

            # Store the new account information
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

            # Save to JSON file
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
                json.dump(accounts, J, indent=4)

        # Withdraw money from user's account
        def Withdraw_Money(self):
            if not self.current_user:
                return
            WM = int(input("Enter Money To Be Withdrawn --> "))
            if WM < 0:
                print("Enter A Valid Number")
                return

            # Check balance before withdrawal
            if self.current_user['Bank Balance'] >= WM:
                OBB = self.current_user['Bank Balance']
                NBB = OBB - WM
                print(f'Your Old Bank Balance Was {OBB} and Your New Bank Balance is {NBB}')
                self.current_user['Bank Balance'] = NBB
                self.storing()
            else:
                print("Insufficient Balance!")

        # Deposit money into user's account
        def Deposite_Money(self):
            if not self.current_user:
                return
            while True:
                DM = int(input("Enter Money To Be Deposited --> "))
                if DM < 0:
                    print("Enter A Valid Number")
                    continue

                x = int(input("Enter Account Number --> "))
                if len(str(x)) != 12:
                    print("Enter A Valid Account Number!")
                    continue
                y = int(input("Enter PIN --> "))
                if len(str(y)) != 4:
                    print("Enter A Valid PIN!")
                    continue

                OBB = self.current_user['Bank Balance']
                NBB = OBB + DM
                print(f"Your Old Bank Balance Was {OBB},\nAnd Your New Bank Balance Is {NBB}")
                self.current_user['Bank Balance'] = NBB
                self.storing()
                break

        # Calculate interest after 30 days
        def intrest(self):
            if not self.current_user:
                return
            # Check if 30 days (2592000 seconds) passed since last interest
            if self.current_user['Last Intrested'] - time.time() >= 2592000:
                interest = self.current_user['Bank Balance'] * 0.05
                total = self.current_user['Bank Balance'] * 1.05
                self.current_user['Last Intrested'] += 2592000
                self.current_user['Bank Balance'] += interest
                self.storing()
                print(f"You Received Interest Of {interest} ₹, Total Balance: {total} ₹")
            else:
                # Show remaining days for next interest
                IID = round((2592000 + self.current_user['Last Intrested'] - time.time()) / 86400, 0)
                print(f"You Will Receive Interest After {int(IID)} days")

    # --- Run the main interface ---
    bank = Bank()
    bank.working()


if __name__ == "__main__":
    main()
