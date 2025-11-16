## 6.100A PSet 1: Part C
## Name: An Dang
## Time Spent: 0:10
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
cost_of_down_payment = cost_of_dream_home * portion_down_payment
epsilon = 100
months = 36
low = 0
high = 1
r = (high + low) / 2
amount_saved = initial_deposit * (1 + high / 12) ** months
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if cost_of_down_payment > amount_saved:
    r = None
else:
    while abs(amount_saved - cost_of_down_payment) > epsilon:
        if amount_saved < cost_of_down_payment:
            low = r
        else:
            high = r
        r = (high + low) / 2
        amount_saved = initial_deposit * (1 + r / 12) ** months
        steps += 1

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")
