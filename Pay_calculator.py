# Simple program to calculate pay, including Overtime

# Data Entry

hrs = input('Enter Hours ')
rte = input('Enter Rate ')

# Calculate Overtime

if float(hrs) > 40:
    ot = float(hrs) - 40
    regot = float(hrs) - ot
else:
    ot = 0

# Calculate pay

rpay = regot * float(rte)
otpay = ot * (float(rte) * 1.5)

pay = rpay + otpay

# Format output to have 2 decimals

formatted_rpay = "{:.2f}".format(rpay)
formatted_otpay = "{:.2f}".format(otpay)
formatted_pay = "{:.2f}".format(pay)

print('Regular Pay: ', formatted_rpay)
print('Overtime Pay: ', formatted_otpay)
print('Total Pay: ', formatted_pay)
