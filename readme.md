# Credit Card Validator using Luhn's Algorithm

A Python application that validates credit card numbers using Luhn's algorithm. This program takes a credit card number, performs calculations as per the Luhn algorithm, and determines if the number is valid.


## Description

This program implements Luhn's algorithm, which is commonly used to validate various identification numbers, especially credit card numbers. The algorithm verifies if a given credit card number is valid based on its digit pattern.


## Installation 
1. Clone this repository: 
```bash 
git clone https://github.com/yourusername/credit-card-validator.git
```
2. Navigate to the project directory: 
```bash
cd credit-card-validator
```
3. Ensure you have Python installed. You can check by running:
```bash
python --version
```

## Usage

1. Open the Python file containing the Luhn's algorithm script.
2. Modify the `cc_number` variable in the script with the credit card number you want to validate.
3. Run the script
4. The script will output whether the card is "Valid" or "Invalid" in the terminal.

## How it works

The algorithm performs the following steps:

1.  **Separation of odd and even digits**: It separates digits based on their positions (odd or even).
2.  **Doubling even-positioned digits**: The digits in even positions are doubled. If doubling results in a two-digit number, the digits are split and summed.
3.  **Summing odd-positioned digits**: The digits in odd positions are summed directly.
4.  **Total Sum**: The sums from odd and even positions are added together.
5.  **Validation**: If the total sum is divisible by 10, the card is valid; otherwise, it is invalid.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

