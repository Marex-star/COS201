def compute_tax():
    
    print("Filing Status Options:")
    print("0: Single filers")
    print("1: Married filing jointly or qualified widow(er)")
    print("2: Married filing separately")
    print("3: Head of household")
    
    try:
        status = int(input("Enter the filing status (0-3): "))
        income = float(input("Enter the taxable income: $"))   
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    if status == 0: 
        brackets = [8350, 33950, 82250, 171550, 372950]
    elif status == 1: 
        brackets = [16700, 67900, 137050, 208850, 372950]
    elif status == 2:  
        brackets = [8350, 33950, 68525, 104425, 186475]
    elif status == 3:  
        brackets = [11950, 45500, 117450, 190200, 372950]
    else:
        print("Error: Invalid filing status selected. Please restart and choose 0-3.")
        return

   
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    
    tax = 0.0
    previous_limit = 0

    
    for i in range(len(brackets)):
        current_limit = brackets[i]
        current_rate = rates[i]

        if income > current_limit:
          
            taxable_amount_in_bracket = current_limit - previous_limit
            tax += taxable_amount_in_bracket * current_rate
            previous_limit = current_limit
        else:

            taxable_amount_in_bracket = income - previous_limit
            tax += taxable_amount_in_bracket * current_rate
            return tax 

    if income > brackets[-1]:
        taxable_amount_in_bracket = income - brackets[-1]
        tax += taxable_amount_in_bracket * rates[-1]

    return tax


calculated_tax = compute_tax()

if calculated_tax is not None:
    print(f"Your total tax is: ${calculated_tax:,.2f}")