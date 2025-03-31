income = {
    "salary" : 15000,
    "freelance" : 10000
}

category = {
    "rent" : 2000,
    "food" : 4000
}

def cal_total_income(income_dict):
    return sum(income_dict.values())

def cal_total_expences(category_dict):
    return sum(category_dict.values())

total_income = cal_total_income(income)
total_expences = cal_total_expences(category)
balance = total_income - total_expences
 
print(f"income = {total_income},expences = {total_expences}, balance ={balance}")