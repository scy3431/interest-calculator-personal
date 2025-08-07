#Interest calculator for capital one join account

def calculate_shares(person1_contribution, person2_contribution, total_after_interest):
    total_contribution = person1_contribution + person2_contribution
    
    person1_share = (person1_contribution / total_contribution) * total_after_interest
    person2_share = (person2_contribution / total_contribution) * total_after_interest
    
    return person1_share, person2_share

person1_contribution = float(input("Enter the contribution of Person 1: "))
person2_contribution = float(input("Enter the contribution of Person 2: "))
total_after_interest = float(input("Enter the total amount in the account after interest: "))

person1_share, person2_share = calculate_shares(person1_contribution, person2_contribution, total_after_interest)

print(f"Person 1's share: ${person1_share:,.2f}")
print(f"Person 2's share: ${person2_share:,.2f}")

#as of 10/11/2024 mom: 50.03, sean: 5745.24
#as of 10/30/2024 mom: 50.03, sean: 5753.13
#as of 11/01/2024 mom: 50.03, sean: 5758.21
#as of 11/12/2024 mom: 50.03, sean: 6385.71
#as of 12/26/2024 mom: 350.03, sean: 6385.71
#as of 7/10/2025  mom: 550.03, sean: 7785.71