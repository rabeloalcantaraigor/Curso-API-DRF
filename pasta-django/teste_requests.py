import requests

# GET Avaliacoes


avaliacoes=requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

#Acessando o código de status HTTP
#print(avaliacoes.status_code)

#if avaliacoes.status_code==200:
#    print('200 OK')

#elif avaliacoes.status_code ==404:
#    print('404 ERROR')

# Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

# Acessando a quantidade de registros
#print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
#print(avaliacoes.json()['next'])

# Acessando os resultados desta página
#print(avaliacoes.json()['results'])
#print(type(avaliacoes.json()['results']))

#Acessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])

#Acessando o último elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])

#Acessando somente o nome da pessoa que fez a última avaliacao
#print(avaliacoes.json()['results'][-1]['nome'])

#GET Avaliacao

#avaliacao=requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/3/')

#print(avaliacao.json())

#GET Cursos
headers= {'Authorization':'Token 8f358c8625f99c5827b60c2b09d2fb8e2289bb7f'}

cursos=requests.get(url='http://127.0.0.1:8000/api/v2/cursos/',headers=headers)
print(cursos.status_code)
print(cursos.json())