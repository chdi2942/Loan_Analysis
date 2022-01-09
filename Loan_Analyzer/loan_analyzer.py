# import csv/path
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries."""

loan_costs = [500, 600, 200, 1000, 450]

#   Uses the `len` function to calculate the total number of loans in the list.
#   Prints the number of loans from the list

loan_len = len(loan_costs)
print(f"There are {loan_len} loans.")

#   Uses the `sum` function to calculate the total of all loans in the list.
#   Prints the total value of the loans

loan_sum = sum(loan_costs)
print("The sum of all loans is: ", loan_sum)

#   Uses the sum of all loans and the total number of loans, calculated the average loan price.
#   Prints the average loan amount

loan_average = (loan_sum)/(loan_len)
print("The average of all loans is: ", loan_average)

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, calculate a Present Value, or a "fair price" for what this loan would be worth. """

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#   1. Get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
        # a. Saves these values as variables called `future_value` and `remaining_months`.
        # b. Prints each variable.

loan_fv = loan.get("future_value")
loan_mo_rem = loan.get("remaining_months")
print("The future value of the loan is: ", loan_fv)
print(f"There are {loan_mo_rem} months remaining on the loan.")

#   2. Formula for Present Value to calculate a "fair value" of the loan. Used a minimum required return of 20% as the discount rate.

present_value = (loan_fv) / (1+(.20/12)) ** loan_mo_rem

#   3. Conditional statement to decide if the present value represents the loan's fair value.
        # a. If the present value of the loan is greater than or equal to the cost, prints a message that says the loan is worth at least the cost to buy it.
        # b. Else, the present value of the loan is less than the loan cost, then prints a message that says that the loan is too expensive and not worth the price.

if present_value >= loan.get("loan_price"):
    print(f"Since {present_value} > loan price, the loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function will include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function will return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#    Defines a new function that will be used to calculate present value.
#    Includes parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function returns the `present_value` for the loan.
def calculate_pv(remaining_months, annual_discount_rate, future_value):
    present_value = future_value / (1+(annual_discount_rate/12)) ** remaining_months  
    return present_value

#   Uses the function to calculate the present value of the new loan given.
#   Uses an `annual_discount_rate` of 0.2 for this new loan calculation.

present_value = format(calculate_pv(12,.2,1000), '.2f')
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.

In this section, a loop is used to iterate through a series of loans and select only the inexpensive loans.

1. Creates a new, empty list called `inexpensive_loans`.
2. Uses a for loop to select each loan from a list of loans.
    a. Inside the for loop, an if-statement determines if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500, appends that loan to the `inexpensive_loans` list.
3. Prints the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#   Creates an empty list for `inexpensive_loans`

inexpensive_loans = []

#   Loops through all the loans and appends any that cost $500 or less to the `inexpensive_loans` list

for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
    else:
        pass

#   Prints the `inexpensive_loans` list

print(inexpensive_loans)


"""Part 5: Save the results.

Outputs this list of inexpensive loans to a csv file
    1. Uses `with open` to open a new CSV file.
        a. Creates a `csvwriter` using the `csv` library.
        b. Uses the new csvwriter to write the header variable as the first row.
        c. Uses a for loop to iterate through each loan in `inexpensive_loans`.
            i. Uses the csvwriter to write the `loan.values()` to a row in the CSV file.
"""


#   Sets the output header

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

#   Sets the output file path

output_path = Path("inexpensive_loans.csv")

#   Fills each row of `loan.values()` from the `inexpensive_loans` list with header into csv file.

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(header)

    for row in inexpensive_loans:
        csvwriter.writerow(row.values())