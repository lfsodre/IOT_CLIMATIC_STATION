import machine
import dht
import time
import network
import urequests
from internet_connection import connection

relay = machine.Pin(2, machine.Pin.OUT)
sensor = dht.DHT11(machine.Pin(4))
relay.value(0)

while True:
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    print("Disciplina: Cloud, IOT, e Industria 4.0")
    print("Professor: Valmir Moro")
    print("-" * 50)
    print("Equipe")
    print("Aluno: Marlon Segalla Filho")
    print("Aluno: Luis Felipe Sodre")
    print("Aluno: Victor Paixão de Souza")
    print("-" * 50)
    print("Climate Season")
    print("A Temperatura atual é: {}°C.".format(temperature))
    print("A Humidade atual é: {}%.".format(humidity))
    print()
    print("-" * 50)
    print("Condiçoes de acionamento do Relé")
    print("Temperatura > 0°C.")
    print("Humidade > 1%.")
    print()
    time.sleep(5)
    if temperature > 0 or humidity > 1:
        relay.value(1)
        print("Relé ligado.")
        print()
    else:
        relay.value(0)
        print("Relé desligado.")
        print()
    time.sleep(5)
    print()
    
    print("Conectando com a rede WIFI...")
    time.sleep(2)
    print()
    station = connection("ESTACIO-VISITANTES", "estacio@2014")
    if not station.isconnected():
        print("Erro de conexão com a rede WIFI! Tente novamente.")
    else:
        print("Conexão realizada com sucesso!")
        print("Acessando a plataforma ThingSpeak...")
        time.sleep(2)
        print()
        print("Acesso a plataforma ThingSpeak realizado com sucesso")
        print()
        print("Enviando os dados...")
        response = urequests.get("https://api.thingspeak.com/update?api_key=6U20Y8I6F7VM9ND9&field1={}&field2={}".format(temperature, humidity))
        time.sleep(2)
        print("Dados enviados com sucesso!")
        response.text
        station.disconnect()
        time.sleep(2)