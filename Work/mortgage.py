# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
payment_month = 1
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0

while principal > 0:
    if (payment_month >= extra_payment_start_month) and (payment_month <extra_payment_end_month):
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    payment_month += 1

print(f'Last payment on {payment_month}, total paid {total_paid}')
