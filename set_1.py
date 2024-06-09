def savings(gross_pay, tax_rate, expenses):
   after_tax_pay = gross_pay * (1-tax_rate)
   remaining_pay = int(after_tax_pay) - expenses
   return remaining_pay 
 
def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    remaining_material = total_material - total_consumed
    return f"{remaining_material}{material_units}"

def interest (principal, rate, periods):
    investment = principal * rate * periods
    final_investment = principal + investment
    return int(final_investment)