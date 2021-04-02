import requests
from bs4 import BeautifulSoup as bs
import csv
Links =[]
URL = 'https://sante.sec.gouv.sn/actualites'
url_Base = 'https://sante.sec.gouv.sn'
page = requests.get(URL)
soup = bs(page.content, 'html.parser')
results= soup.find_all('span', class_='card-title')
# print(results.len())
for result in results:
    link = result.find('a')['href']
    new_link = url_Base +link
    page = requests.get(newLink)
    soup = bs(page.content, 'html.parser')
    PDFs= soup.find_all('span', class_='file')
    for pdf in PDFs:
        pdf_link = pdf.find('a')['href']



    
    # with open('techtrack100.csv','w', newline='') as f_output:
    # csv_output = csv.writer(f_output)
    # csv_output.writerows(rows)

