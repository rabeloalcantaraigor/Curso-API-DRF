import requests

headers={'Authorization':'Token 8f358c8625f99c5827b60c2b09d2fb8e2289bb7f'}

url_base_cursos='http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes='http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado=requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

#print(resultado.status_code)

#Testando se o endpoint está correto

assert resultado.status_code == 200

#Testando a quantidade de registros

assert resultado.json()['count']==5

#Testando se o título do primeiro curso está correto

assert resultado.json()['results'][0]['titulo']=='Programação com JavaScript'