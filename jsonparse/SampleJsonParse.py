import json

content = '{"name":"RahulShetty","languages": ["Java","Python"]}'

# loads() method parse json string and it returns dictionary

dict_content = json.loads(content)
print(dict_content)
print(type(dict_content))
print(dict_content['name'])
print(dict_content['languages'][0])
# print(type(dict_content['languages']))

