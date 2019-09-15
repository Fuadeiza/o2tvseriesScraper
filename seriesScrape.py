from bs4 import BeautifulSoup
import requests


def series_title(name,season,episode):
    links=[]
    titles=[]
    links_2_visit=[]
    url = 'http://o2tvseries.com/search/list_all_tv_series/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    for link in soup.findAll('a'):
      href= link.get('href')
      title=(link.string)
      links.append(href)
      titles.append(title)
    for i in titles:
      if i==name:
        title_index=titles.index(i)
        print(title_index)
        link_2_visit=(links[title_index])
      else:
        pass
    resp = requests.get(link_2_visit, headers=headers)
    soup=BeautifulSoup(resp.text,'html.parser')
    for link in soup.findAll('a'):
      link_2_visit_href= link.get('href')
      links_2_visit.append(link_2_visit_href)
    sea_link= link_2_visit.split('/i')[0] +'/season-'+season+'/episode-' + episode +'/index.html/'
    print(sea_link)


series_title('The Blacklist','05','12')
