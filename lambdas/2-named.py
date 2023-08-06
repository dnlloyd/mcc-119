current_age = int(input('Enter current age: '))

################### User defined function
def get_older(age):
    age += 1
    return age

age_by_user_defined_function = get_older(current_age)

################### Lambda function
get_age_by_user_lambda_function = lambda age: age + 1
age_by_user_lambda_function = get_age_by_user_lambda_function(current_age)

################### Verification
print(f'Age from user function: {age_by_user_defined_function}')
print(f'Age from lambda function: {age_by_user_lambda_function}')