# Given a total amount and a list of recipients and how much money each is owed,
# you should return the list of recipients and how much each would be paid after
# following the business logic below:
# * No recipient is paid more than they are owed;
# * The amount is divided as evenly as possible between the recipients.
# * Money must be given in alphabetic order

# Ex:
# input:
#   amount = 40
#   recipients = matt: 20, anna: 20, wilfredo: 40, james: 100  
# output:
#   matt: 10, anna: 10, wilfredo: 10, james: 10 

# Ex:
# input:
#   amount = 40
#   recipients = matt: 5, anna: 5, wilfredo: 40, james: 100  
# output:
#   matt: 5, anna: 5, wilfredo: 15, james: 15

# Ex:
# input:
#   amount = 41
#   recipients = matt: 20, anna: 20, wilfredo: 40, james: 100

# output:
#   matt: 10, anna: 11, wilfredo: 10, james: 10

def calculate_money(amount, recipients):
    paid = {}
    for person in recipients:
        paid[person] = 0

    while amount > 0:
        pending = sorted([person for person in recipients if recipients[person] != paid[person]])
        assigned_amount = amount // len(pending)
        if assigned_amount == 0 and amount > 0:
            assigned_amount = amount
        for person in pending:
            if paid[person] + assigned_amount < recipients[person]:
                paid[person] += assigned_amount
                amount -= assigned_amount
            else:
                remainder = recipients[person] - paid[person]
                paid[person] += remainder
                amount -= remainder
            if amount == 0:
                break
    return paid


result = calculate_money(40, {"matt": 20, "anna": 20, "wilfredo": 40, "james": 100})
print(result)
assert result == {"matt": 10, "anna": 10, "wilfredo": 10, "james": 10}

result = calculate_money(40, {"matt": 5, "anna": 5, "wilfredo": 40, "james": 100})
print(result)
assert result == {"matt": 5, "anna": 5, "wilfredo": 15, "james": 15}

result = calculate_money(40, {"matt": 1, "anna": 5, "wilfredo": 40, "james": 100})
print(result)
assert result == {"matt": 1, "anna": 5, "wilfredo": 17, "james": 17}

result = calculate_money(41, {"matt": 20, "anna": 20, "wilfredo": 40, "james": 100})
print(result)
assert result == {"matt": 10, "anna": 11, "wilfredo": 10, "james": 10}