import requests

s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)
# {
#   "cookies": {
#     "sessioncookie": "123456789"
#   }
# }

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('https://httpbin.org/headers', headers={'x-test2':'true'})
print(s.headers)
s.headers.update({'x-test2': 'true'})
print(s.headers)
# {'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive', 'x-test': 'true'}
# {'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive', 'x-test': 'true', 'x-test2': 'true'}

s = requests.Session()

r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

r = s.get('https://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'

s.cookies.update({'cookie':'1234'})
print(s.cookies)
r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# <RequestsCookieJar[<Cookie cookie=1234 for />]>
# {
#   "cookies": {
#     "cookie": "1234",
#     "from-my": "browser"
#   }
# }
s = requests.Session()

s.cookies.update({'cookie':'1234'})
print(s.cookies)
r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# <RequestsCookieJar[<Cookie cookie=1234 for />]>
# {
#   "cookies": {
#     "cookie": "1234",
#     "from-my": "browser"
#   }
# }