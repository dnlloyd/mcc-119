import requests
import sys

token = sys.argv[1]
headers = {'Authorization': f'Bearer {token}'}
base_url = 'https://mcckc.instructure.com/api/v1'

response = requests.get(f'{base_url}/courses', headers=headers)
courses = response.json()

course_ids = []

for course in courses:
  course_ids.append(course['id'])

print(course_ids)

for course_id in course_ids:
  if course_id == 10089:
    print('================================')
    print(f'Course ID: {course_id}')
    print('================================')
    ### https://canvas.instructure.com/doc/api/courses.html#method.courses.effective_due_dates
    response = requests.get(f'{base_url}/courses/{course_id}/effective_due_dates', headers=headers)
    assignment_due_dates = response.json()
    
    for assignment_id, info in assignment_due_dates.items():
      print(f'Assignment: {assignment_id}')
      # print(json.dumps(info))
      for student_id, data in info.items():
        print(f"  - Student: {student_id} - Due date: {data['due_at']}")

      print('\n')
