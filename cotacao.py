import requests
import webbrowser

# 1. Endereço da API, com as 4 moedas que queremos (todas convertidas para real)
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,JPY-BRL,BTC-BRL"

# 2. Faz o pedido para o site
resposta = requests.get(url)

# 3. Confere se deu certo (200 significa "tudo certo")
if resposta.status_code != 200:
    print("Não foi possível buscar as cotações agora. Tente de novo mais tarde.")
else:
    # 4. Transforma a resposta em um dicionário do Python
    dados = resposta.json()

    # 5. Lista com o nome que vamos mostrar e o código de cada moeda na API
    moedas = [
        ("Dólar", "USDBRL"),
        ("Euro", "EURBRL"),
        ("Iene", "JPYBRL"),
        ("Bitcoin", "BTCBRL"),
    ]

    # 6. Mostra a tabela no terminal
    print()
    print("COTAÇÃO ATUAL")
    print("-" * 28)
    print(f"{'Moeda':<10} {'Valor em R$':>15}")
    print("-" * 28)

    for nome, codigo in moedas:
        valor = float(dados[codigo]["bid"])  # "bid" é o valor de compra
        print(f"{nome:<10} {valor:>15.4f}")

    print("-" * 28)

    # 7. Pergunta se quer abrir o site da fonte dos dados
    resposta_usuario = input("Abrir o site da fonte dos dados? (s/n): ")
    if resposta_usuario.lower() == "s":
        webbrowser.open("https://docs.awesomeapi.com.br/")