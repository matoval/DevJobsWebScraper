import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

## get all US cities
cities_list = 'https://geo.craigslist.org/iso/us'
uClient = uReq(cities_list)
cities_html = uClient.read()
uClient.close()
cites_soup = soup(cities_html, "html.parser")
cites_li = cites_soup.findAll("li")
cites_urls = cites_soup.findAll("a")
city_url_list = []
##loop through and get url for each city
for a in cites_urls:
  cites_url = a['href']
  city_url_list.append(cites_url)


city_url_list.pop(0)
city_url_list.pop(0)
city_url_list.pop(0)



for url in city_url_list:
  my_url = '{}/d/web-html-info-design/search/web'.format(url)
  #get data from url
  uClient = uReq(my_url)
  page_html = uClient.read()
  uClient.close()
  #parse html
  page_soup = soup(page_html, "html.parser")
  #grabs each job title
  job_titles = page_soup.findAll("a", {"class": "result-title"})
  jobs_url_list = []
  for j in job_titles:
    # print(j['href'])
    if j['href']:
      jobs_url_list.append([j['href']])
  file = open('jobs.txt', 'a', newline='')
  with file:
    write = csv.writer(file)
    write.writerows(jobs_url_list)

