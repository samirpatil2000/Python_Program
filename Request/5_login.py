import requests
url='https://curiosityishere.pythonanywhere.com/login/'

with requests.Session() as s:
    USERNAME='Samir'
    PASS='Samir@123'
    s.get(url)
    csrf_token=s.cookies['csrftoken']
    login_data=dict(csrfmiddlewaretoken=csrf_token,username=USERNAME,password=PASS)
    login=s.post(url,login_data)
    print(login.status_code)
    print(login.text)
    page=s.get('https://curiosityishere.pythonanywhere.com/U/profile/')
    print(page.status_code)
    print(page.text)
    