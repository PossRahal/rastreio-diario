import requests
from bs4 import BeautifulSoup as Bs


def info(id,option):
    url = f'https://www.linkcorreios.com.br/?id={id}'
    r = requests.get(url)
    html = r.text
    soup = Bs(html, 'html.parser')
    title = soup.find('div', class_="main_title_3").get_text().replace('\n','')
    status = soup.find('ul', class_="linha_status m-0")
    s1 = status.find_all('li')[0].get_text()
    s2 = status.find_all('li')[1].get_text()
    s3 = status.find_all('li')[2].get_text()
    information={
        'title':title,
        's1':s1,
        's2':s2,
        's3':s3
    }
    text=f'{title}\n{s1}\n{s2}\n{s3}'
    if option==0:
        return information
    else:
        return text     
