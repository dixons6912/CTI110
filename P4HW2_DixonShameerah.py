# Shameerah Dixon
# April 26, 2026
# P4HW2.py
# Calculating Salary

total_overtime = 0.0
total_regular = 0.0
total_gross = 0.0
employee_count = 0

while True:
# Enter employee name
        name = input("Enter employee's name or \"Done\" to terminate: ")
        
        
        if name.lower() == "done":
            break
            
        # User input for hours and rate
        hours = float(input(f"How many hours did {name} work? "))
        rate = float(input(f"What is {name}'s pay rate? "))
        
        employee_count += 1
        
# Calculation of hours
        if hours > 40:
            overtime_hours = hours - 40
            reg_hours = 40
        else:
            overtime_hours = 0
            reg_hours = hours
            
        overtime_pay = overtime_hours * (rate * 1.5)
        reg_pay = reg_hours * rate
        gross_pay = reg_pay + overtime_pay
        
        
        total_overtime += overtime_pay
        total_regular += reg_pay
        total_gross += gross_pay
        
# Results for each employee
        print(f"\nEmployee name:  {name}\n")
        print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime':<10}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
        print("-" * 80)
        print(f"{hours:<15.1f}{rate:<10.1f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:<15.2f}\n")

# Final Totals 
if employee_count > 0:
        print(f"\nTotal number of employees entered: {employee_count}")
        print(f"Total amount paid for overtime: ${total_overtime:.2f}")
        print(f"Total amount paid for regular pay: ${total_regular:.2f}")
        print(f"Total amount paid in gross: ${total_gross:.2f}")
