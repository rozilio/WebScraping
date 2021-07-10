from bs4 import BeautifulSoup
import requests
import pandas as pd

api_num = 0
npo_apis = {}
website = 'https://www.programmableweb.com'
url = 'https://www.programmableweb.com/apis/directory'
#url = 'https://www.programmableweb.com/apis/directory?page=2100'

while True:  
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    apis = soup.findAll('tr',{'class':['odd', 'even']})
    
    for api in apis:
        api_links = api.findAll('a', {'class':''})
        api_name = api_links[0].text if len(api_links)>=1 else 'N/A'
        api_category = api_links[1].text if len(api_links)>=2 else 'N/A'
        api_url = website + api.find('a',{'class':''}).get('href')
        api_desc_tag = api.find('td', {'class':'views-field-field-api-description'})
        api_desc = api_desc_tag.text if api_desc_tag else 'N/A'
    
        api_num += 1
        print('row number: ', api_num)
        npo_apis[api_num] = [api_name, api_url, api_category, api_desc]


    next_page_tag = soup.find('a',{'title':'Go to next page'})
    if next_page_tag and next_page_tag.get('href'):
        url = website + next_page_tag.get('href')
    else:
        break
    
# print('Total apis: ', api_num)
npo_apis_df = pd.DataFrame.from_dict(npo_apis, orient = 'index', columns = ['Api Name', 'Api URL','Category', 'Description'])
# print (npo_apis_df.head())
npo_apis_df.to_csv('npo_apis_Assignment.csv')