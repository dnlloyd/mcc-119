import requests
import sys

token = sys.argv[1]
headers = {'Authorization': f'Bearer {token}'}
base_url = 'https://mcckc.instructure.com'

response = requests.get(f'{base_url}/api/v1/courses', headers=headers)
courses = response.json()

# for course in courses:
#   print('------------------------------')
#   print(f"ID: {course['id']}")

#   if 'name' in course:
#     print(course['name'])
#   else:
#     print('N/A')
