import requests
import sys
import json
import base64
import gnupg
import os
import re

students_file = "/Users/dan/github/dnlloyd/mcc-csis-119-private/students.json"

token = sys.argv[1]
headers = {'Authorization': f'Bearer {token}'}

def get_users():
  response = requests.get(f'https://mcckc.instructure.com/api/v1/courses/10089/users?per_page=50', headers=headers)

  # print(response.status_code)
  student_info = json.loads(response.content.decode())

  student_emails = {}

  for student in student_info:
    student_emails[student['login_id']] = student['email']
    print(f'{student["id"]}: {student["name"]} ({student["login_id"]})')

  with open(students_file, 'w') as outfile:
    json.dump(student_emails, outfile)


def send_message(id, context_code, subject, message):
  post_data = {
    'recipients[]': id,
    'subject': subject,
    'body': message,
    'force_new' : True,
    'context_code': f'course_{context_code}',
    # 'scope': 'unread'
  }
  
  response = requests.post('https://mcckc.instructure.com/api/v1/conversations', headers=headers, data=post_data)
  # print(response.status_code)
  response_json = json.loads(response.content.decode())
  # print(response_json)


def decode_password(encoded_password):
  decoded_password = base64.b64decode(encoded_password)
  gpg = gnupg.GPG()
  password = gpg.decrypt(decoded_password)
  
  return password


def get_user(student_id):
  response = requests.get(f'https://mcckc.instructure.com/api/v1/courses/10089/users?search_term={student_id}', headers=headers)

  print(f'Looking up student: {student_id}')
  # print(response.status_code)
  if response.status_code != 200:
    print('Unable to find student')
  else:
    student_info = json.loads(response.content.decode())
    print(f'Found student: {student_info[0]["name"]}')
    
    return student_info[0]["id"] 


## Main #####

# 1. write student info to students_file
create_users = False
if create_users:
  get_users()
  print('')

# 2. run terraform to provision IAM users

# 3. write encrypted passwords to passwords file
#    tf output -json passwords > /Users/dan/github/dnlloyd/mcc-csis-119-private/passwords.json

# 4. decrypt passwords and send to students
user_accounts_created = True
if user_accounts_created:
  passwords_file = open('/Users/dan/github/dnlloyd/mcc-csis-119-private/passwords.json')
  student_passwords = json.load(passwords_file)

  passwords_plain_text = {}
  invalid_passwords = {}
  manual_provision_script = "/Users/dan/github/dnlloyd/mcc-csis-119-private/manual_user_provisions.sh"

  for student in student_passwords:
    student_id = student
    encrypted_password = student_passwords[student]
    password = decode_password(encrypted_password)

    send_passwords = False
    if send_passwords:
      # lookup student by student ID (e.g. S1234567) and return Canvas ID
      canvas_id = get_user(student_id)

      print(f'Sending password to: {student_id} ({canvas_id})')
      message = f'https://166865586247.signin.aws.amazon.com/console \nIAM user name: {student_id} \npassword: {password}'
      print(message)
      send_message(canvas_id, '10089', "Linux server credentials", message)
      print('')

    translate_table = str.maketrans({"$": r"\$"})

    pass_plain_text = str(password)
    pass_plain_text_trans = pass_plain_text.translate(translate_table)

    # print(pass_plain_text_escaped)
    # print(pass_plain_text)
    # os.system(f'echo {pass_plain_text_escaped_trans}')
    # print('')

    if "!" in pass_plain_text_trans:
      invalid_passwords[student_id] = pass_plain_text_trans
    else:
      passwords_plain_text[student_id] = pass_plain_text_trans

  passwords_plain_text_json = json.dumps(passwords_plain_text)
  with open("/Users/dan/github/dnlloyd/mcc-csis-119-private/passwords-plain-text.json", "w") as outfile:
    outfile.write(passwords_plain_text_json)

  if len(invalid_passwords) != 0:
    print('WARNING: Some users were created with invalid passwords. Create manually:')
    print(f'Writing commands to :{manual_provision_script}\n')
    with open(manual_provision_script, "w") as outfile:    
      for student in invalid_passwords:
        student_id = student
        password = invalid_passwords[student]

        new_pass = password.replace("!", "\"'!'\"")
        print(f'useradd {student_id}\necho "{new_pass}" | passwd {student_id} --stdin')
        outfile.write(f'useradd {student_id}\necho "{new_pass}" | passwd {student_id} --stdin\n')

# 5. Run terraform to provision EC2
# 6. Manually provision users with invalid passwords
