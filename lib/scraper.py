from bs4 import BeautifulSoup
import requests

# Set headers to avoid 403 Forbidden
headers = {'user-agent': 'my-app/0.0.1'}

# Request the HTML content from Flatiron School's courses page
html = requests.get("https://flatironschool.com/our-courses/", headers=headers)

# Parse HTML with BeautifulSoup
doc = BeautifulSoup(html.text, 'html.parser')

# Select course titles using combined CSS classes
courses = doc.select('.heading-60-black.color-black.mb-20')

# Print each course title, cleaned up
for course in courses:
    text = course.contents[0].strip()
    print(text)
