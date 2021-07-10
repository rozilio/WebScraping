from bs4 import BeautifulSoup
import requests
import pandas as pd

job_num = 0
npo_jobs = {}
url = "https://boston.craigslist.org/search/sof"

while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    jobs = soup.findAll("p",{"class":"result-info"})
    
    for job in jobs:
        title = job.find("a", {"class":"result-title"}).text
        location_tag = job.find("span",{"class":"result-hood"})
        location = location_tag.text[2:-1] if location_tag else "N/A"
        date = job.find("time",{"class":"result-date"}).text
        link = job.find('a',{'class':'result-title'}).get('href')
        
        job_response = requests.get(link).text
        job_soup = BeautifulSoup(job_response, 'html.parser')
        job_desc = job_soup.find('section', {'id':'postingbody'}).text
        job_attr_tag = job_soup.find('p',{'class':'attrgroup'})    
        job_attr = job_attr_tag.text if job_attr_tag else 'N/A'
        
        job_num += 1
        npo_jobs[job_num] = [title, location, date, link, job_attr, job_desc]

#        print('Job Title: ', title, '\nLocation: ', location, '\nDate: ', date, '\nLink: ', link, job_attr, '\nJob Description: ', job_desc,'\n---')

    url_tag = soup.find('a',{'title':'next page'})
    if url_tag.get('href'):
        url = 'https://boston.craigslist.org' + url_tag.get('href')
        #print(url)
    else:
        break
    
# print('Total Jobs: ', job_num)
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns = ['Job Title', 'Location', 'Date', 'Link', 'Job Attributes', 'Job Description'])
# print (npo_jobs_df.head())
npo_jobs_df.to_csv('npo_jobs.csv')
