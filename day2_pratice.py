def func(nn):
    output_var=nn+15
    return output_var
new_number=func(1110)
print(new_number)

#2nd example
def func(nn):
    pn=nn+19
    return pn
new=func(99)
print(new)

def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (100- 12)
    return pay_aftertax
# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print(pay_fulltime)

#function qith more arguments
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax
same_pay_fulltime = get_pay_with_more_inputs(40, 15, 12)
print(same_pay_fulltime)

#func with no argument 
def pinky_m():
    print("hello ,manisha")
    print("good morning")
pinky_m()