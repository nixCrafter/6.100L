## 6.100A PSet 1: Part A
## Name: An Dang
## Time Spent: 0:10
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
cost_of_down_payment = cost_of_dream_home * portion_down_payment
monthly_saving = yearly_salary / 12 * portion_saved
amount_saved = 0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
while amount_saved < cost_of_down_payment:
    amount_saved *= 1 + (r / 12)
    amount_saved += monthly_saving
    months += 1

print(f"Number of months: {months}")
