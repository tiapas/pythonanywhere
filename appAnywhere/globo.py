# by ATM

import requests

from bs4 import BeautifulSoup
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def ajusta(texto):
    return texto.replace('<br/>','').replace('\n', '').replace('\r', '')


def get_noticias(ano=datetime.now().year, mes=datetime.now().month, dia=datetime.now().day):

    data = date(ano,mes,dia)
    today = date(datetime.now().year, datetime.now().month, datetime.now().day)

    if (data == today):
        url = 'http://globo.com'
    else:
        base = 'http://archive.org/wayback/available?url=globo.com&timestamp={0:04}{1:02}{2:02}'.format(ano, mes, dia)
        r = requests.get(base)
        data = r.json()
        url = data['archived_snapshots']['closest']['url']

    busca = []

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    lista = soup.find_all('a', class_='hui-premium__link')
    for texto in lista:
        title = ajusta(texto['title'])
        href = texto['href'] 
        busca.append({'title': title, 'href': href, 'ano': ano, 'mes': mes, 'dia': dia})

    lista = soup.find_all('ol', class_='topglobocom__content-news')
    for id, texto in enumerate(lista):
        topicos = texto.find_all('a', class_='topglobocom__content-title')
        for id_seq, item in enumerate(topicos):
            title = ajusta(item['title'])
            href = item['href'] 
            busca.append({'title': title, 'href': href, 'ano': ano, 'mes': mes, 'dia': dia})

    return busca


if __name__ == "__main__":

    retorno = get_noticias()
    # retorno = get_noticias(2016,9,21)

    for item in retorno:
        print(item['title'])
        print(item['href'])
        print(item['ano'],item['mes'],item['dia'])
        print('')

