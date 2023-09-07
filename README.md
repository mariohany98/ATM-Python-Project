# ATM Python Project

This is a simple ATM (Automated Teller Machine) simulation implemented in Python. It allows users to log in with a PIN, check their balance, withdraw money, and log out.
This project is a simple demonstration and should not be used for real-world financial transactions. It does not provide any security or encryption for sensitive data. Use it for educational purposes only.

## Features

- Secure login with a PIN code.
- Check account balance.
- Withdraw money within the specified limits.
- Logout and return the card.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your computer.
- Required Python libraries: `termcolor`, `pyfiglet`.

## Customize
You can customize the ATM by modifying the following variables in the atm.py file:

- pin: Set your desired PIN code.
- balance: Set your initial account balance.
- withdraw_limit: Set your daily withdrawal limit.

## ATM Functions
Login: Enter your PIN code to access your account. After three incorrect attempts, you will need to wait for 5 minutes.

Check Balance: View your account balance.

Withdraw: Choose how much money you want to withdraw. You can only withdraw up to a specified daily limit, and your balance must cover the withdrawal amount.

Logout: Safely log out of your account.

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/mariohany98/atm-python-project.git

2. Change into the project directory:
   cd atm-python-project

3. Run the ATM program:
   python atm.py

## Author
Mario Hany

Feel free to contribute, report issues, or suggest improvements. Thank you for using the ATM Python Project!
