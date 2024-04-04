import requests

nome_municipio = input("Digite o nome do município: ")

def regiaocidade(nome_municipio):
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        for municipio in dados:
            if municipio['nome'].upper() == nome_municipio.upper():
                mesorregiao = municipio['microrregiao']['mesorregiao']['nome']
                return mesorregiao
        
        return "Não foi possivel encontar a cidade."
    else:
        return "ERRO."

mesorregiao = regiaocidade(nome_municipio)
print(f"A mesorregião do município {nome_municipio} é: {mesorregiao}")
