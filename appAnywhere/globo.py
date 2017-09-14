# by ATM

import requests

from bs4 import BeautifulSoup
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def get_links(lista,url):

    base = url.replace('http://www.globo.com/','')

    links = []

    for texto in lista:
        title = texto['title'].replace('<br/>','').replace('\n', '').replace('\r', '')
        href = texto['href'].replace(base,'')
        links.append({'title': title, 'href': href})
        
    return links


def get_noticias(ano=datetime.now().year, mes=datetime.now().month, dia=datetime.now().day):

    # Python-anywhere bloqueia acesso a sites externos; https://www.pythonanywhere.com/whitelist/
    # data = date(ano,mes,dia)
    # today = date(datetime.now().year, datetime.now().month, datetime.now().day)
    # if (data == today):
    #    url = 'http://globo.com'

    base = 'http://archive.org/wayback/available?url=globo.com&timestamp={0:04}{1:02}{2:02}235959'.format(ano, mes, dia)
    r = requests.get(base)
    data = r.json()
    url = data['archived_snapshots']['closest']['url']
    time = data['archived_snapshots']['closest']['timestamp']
    print(time)
    archive = datetime.strptime(time[0:8], '%Y%m%d').date()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lista = soup.find_all('a', class_='hui-premium__link')
    lista_botton = soup.find_all('ol', class_='topglobocom__content-news')

    main = get_links(lista,url)
    geral = get_links(lista_botton[0].find_all('a', class_='topglobocom__content-title'),url)
    esportes = get_links(lista_botton[1].find_all('a', class_='topglobocom__content-title'),url)
    cotidiano = get_links(lista_botton[2].find_all('a', class_='topglobocom__content-title'),url)

    return main, geral, esportes, cotidiano, archive


if __name__ == "__main__":

    main, geral, esportes, cotidiano, data = get_noticias()
    # main, geral, esportes, cotidiano, data  = get_noticias(2016,9,21)

    print(data)
    for item in cotidiano:
        print(item['title'])
        print(item['href'])
        print('')

