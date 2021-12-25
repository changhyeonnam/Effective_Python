import requests
url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.request("GET",url,headers={},data={})
print(response.status_code)
# 200
data = response.content
print(data)
print(type(data))
# b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
# <class 'bytes'>
import json
data = json.loads(response.content)
print(data)
print(type(data))
# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
# <class 'dict'>
for k,v in data.items():
    print(f"key:{k}, value:{v}")
# key:userId, value:1
# key:id, value:1
# key:title, value:delectus aut autem
# key:completed, value:False

