def bill_calc(bill_amt, tip_perc):
    """hello"""
    total = bill_amt * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

bill_calc(float(input("Give the original price please. ")), float(input("Give the tip percentage please. ")))


print(bill_calc.__doc__)