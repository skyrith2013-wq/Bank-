# CBSE Bank System

## Overview

This project is a simple console-based banking system that allows users to create accounts, log in, check balances, withdraw and deposit money, and receive monthly interest. Account data is stored in a JSON file named `CBSE_Store.json`.

## Features

* Create new bank accounts
* Login for existing users
* Deposit money
* Withdraw money
* Check account balance
* Automatic interest after 30 days

## File Required

* **CBSE_Store.json** : This file stores all user account records.

If the file does not exist, the program will create it automatically.

## Sample Account for Testing

Use the following credentials to test login:

* **Account Number:** 226991532315
* **PIN:** 5566
* **Mobile Number:** 1234567890

Or you can create your own account through the program.

> If you'd like to manage or generate accounts from another tool, check the repository named **"Bank"**.

## Requirements

* Python 3.x
* Standard Python libraries (no external dependencies)

## Running the Program

```
python main.py
```

Follow on-screen instructions to create or log into an account.

## Notes

* Mobile numbers must be 10 digits.
* PIN must be 4 digits.
* Users must be at least 18 years old.
* Withdrawals are only allowed if there is sufficient balance.

## Future Improvements

* Encrypt PIN values for better security
* Add transaction history
* Add GUI support

---

This project is intended for learning and practice purposes.
