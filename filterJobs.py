import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

with open('jobs.csv') as f:
  l = list(map(str.split, f.read().split('\n\n')))

## get only developer jobs
job_urls = l[0]
counter = 0
for j in job_urls:
  counter = counter + 1
  print(counter)
  filtered_list = []
  uClient = uReq(j)
  job_html = uClient.read()
  uClient.close()
  job_soup = soup(job_html, "html.parser")
  job_removed = job_soup.find("span", {"id": "has_been_removed"})
  if job_removed == None:
    job_title = job_soup.findAll("span", {"id": "titletextonly"})
    job_body = job_soup.findAll("section", {"id": "postingbody"})
    if (len(job_title[0]) != 0 and len(job_body[0]) != 0):
      if (job_title[0].text.find("developer") != -1 or job_body[0].text.find("developer") != -1 ):
        filtered_list.append(j)
      if len(filtered_list) != 0: 
        file = open('filteredJobs.txt', 'a', newline='')
        with file:
          write = csv.writer(file)
          write.writerow(filtered_list)
