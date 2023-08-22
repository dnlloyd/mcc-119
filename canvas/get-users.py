import requests
import sys
import json


students_file = "/Users/dan/github/dnlloyd/mcc-csis-119-private/students.json"

token = sys.argv[1]
headers = {'Authorization': f'Bearer {token}'}

response = requests.get(f'https://mcckc.instructure.com/api/v1/courses/10089/users?per_page=50', headers=headers)

print(response.status_code)
student_info = json.loads(response.content.decode())

student_emails = {}

for student in student_info:
  student_emails[student['login_id']] = student['email']

with open(students_file, 'w') as outfile:
  json.dump(student_emails, outfile)