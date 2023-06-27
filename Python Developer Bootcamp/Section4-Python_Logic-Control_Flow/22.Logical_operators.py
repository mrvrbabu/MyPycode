# ----------------------------------------------------------------------- #
# --------------- ** Logical Operators **  ---------------------------- #


# Example 1 **** Processing Loans *****

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


high_income_ram = False
good_credit_ram = False

if high_income_ram or good_credit_ram:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")
