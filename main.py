from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('buscar.html');

@app.route('/gpsbus', methods=['POST',])
def buscar():
    linha = request.form['linha']
    variavel_consulta = "http://dadosabertos.rio.rj.gov.br/apiTransporte/apresentacao/rest/index.cfm/obterPosicoesDaLinha/" + linha
    resultado_consulta = requests.get(variavel_consulta)
    valores = json.loads(resultado_consulta.content)
    recuperado = valores['DATA']
    tamanho_lista = len(recuperado)
    print(tamanho_lista)
    # Contador para o While
    contador = 0
    contador_ordem = 0
    coordenadas = ""
    centro_coord = ""
    while (contador < tamanho_lista):
        # Imprime a linha atual
        # print(recuperado[contador])
        valor_atual = recuperado[contador]
        coordenadas = coordenadas + "{lat: " + str(valor_atual[3]) + ", lng:"+  str(
            valor_atual[4]) + "},"
        contador = contador + 1
        if contador_ordem == 0:
            centro_coord = coordenadas + "{lat: " + str(valor_atual[3]) + ", lng:" + str(
                valor_atual[4])
            contador_ordem = 1
            # return centro_coord

    return render_template("mapa2.html", coordenada_centro=centro_coord, coordenada=coordenadas, titulo=linha)
    # print(coordenadas)


app.run()

