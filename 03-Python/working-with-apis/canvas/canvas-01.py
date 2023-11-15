import requests
import sys

token = sys.argv[1]
headers = {'Authorization': f'Bearer {token}'}
base_url = 'https://mcckc.instructure.com'

### List courses: https://canvas.instructure.com/doc/api/courses.html#method.courses.index
response = requests.get(f'{base_url}/api/v1/courses', headers=headers)

print(response)

### https://requests.readthedocs.io/en/latest/
# print(response.json())
# print(type(response.json()))
