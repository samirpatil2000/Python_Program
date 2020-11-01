import requests
from bs4 import BeautifulSoup
url='https://curiosityishere.pythonanywhere.com/login/'
#url='https://www.codechef.com'
LOGIN_ROUTE = 'login/'

headers={  #this is stop automation
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'origin':url, 'referer':url+LOGIN_ROUTE
}
s = requests.session()
s.get(url)
csrf_token = s.cookies['csrftoken']
print(csrf_token)

login_data = {
'csrfmiddlewaretoken':csrf_token,
'username': 'Samir',
'password': 'Samir@123',

}

login_req=s.post(url,data=login_data)
print(login_req.status_code)
cookies=login_req.cookies
print(cookies)

# with requests.Session() as a:
#     r=a.get(url,headers=headers)
#     soup=BeautifulSoup(r.content,'html5lib')
#     # print(r.content)
#     # print(r.text)
#     login_data['csrfmiddlewaretoken']=soup.find('input',attrs={'name':'csrfmiddlewaretoken'})['value']
#     r=a.post(url,data=login_data,headers=headers)
#     print(r.content)
#     print(r.text)
#     print(r.status_code)

# this is giving erro


