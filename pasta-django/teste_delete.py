import requests

headers={'Authorization':'Token 8f358c8625f99c5827b60c2b09d2fb8e2289bb7f'}

url_base_cursos='http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes='http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado=requests.delete(url=f'{url_base_cursos}6/', headers=headers)

#Testando o código HTTP
assert resultado.status_code==204

#Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text)==0