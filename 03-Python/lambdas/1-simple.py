################### User defined function
def get_older(age):
    age += 1
    return age


current_age = int(input('Enter current age: '))
age_by_user_defined_function = get_older(current_age)
print(f'Age from user function: {age_by_user_defined_function}')


################### Lambda function
age_by_user_lambda_function = (lambda age: age + 1)(current_age)

print(f'Age from lambda function: {age_by_user_lambda_function}')
