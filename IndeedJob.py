import pandas as pd
from bs4 import BeautifulSoup
from requests import get
from time import time, sleep
from random import randint
from warnings import warn
from IPython.core.display import clear_output

# Elements needs to extract
job_titles = []
company_names = []
job_locations = []
salaries = []
job_description = []
date_of_posting = []
location = ["California", "Chapel Hill", "Omaha"]
start_time = time()
request = 0

# Using for loop to go through every location required
for i in range(len(location)):
    response = get('https://www.indeed.com/jobs?q=retail&l='+location[i]+'&sort=date')
    sleep(randint(8,15))

    # Monitor the requests
    request += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(request, request/elapsed_time))
    clear_output(wait = True)

    # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(request, response.status_code))

    # Break the loop if the number of requests is greater than expected
    if request > 100:
        warn('Number of requests was greater than expected.')
        break

    bs = BeautifulSoup(response.text, 'html.parser')
    mv_containers = bs.find_all('div', {'class': {'job_seen_beacon'}})
    for container in mv_containers:
        # job title
        tt = container.find('span', {'title'}).text
        job_titles.append(tt)

        # company name
        cn = container.find('span', {'class': 'companyName'}).text
        company_names.append(cn)

        # job locations
        jl = container.find(['div', 'span'], {'class':{'location accessible-contrast-color-location'}})
        try:
            job_locations.append(jl.text)
        except:
            job_locations.append('Missing')

        #salaries
        sl = container.find('span',{'class':'salaryText'})
        try:
            salaries.append(sl.text)
        except:
            salaries.append('Missing')

        #job description
        try:
            jd = container.find('div', {'class': 'summary'}).find_all('ul')[0]
            jd2 = jd.find_all('li')
            text = ''
            for element in jd2:
                text = text+element.text
            job_description.append(text)
        except:
            job_description.append('Missing')

        #date of posting

        try:
            dp = container.find('span',{'class':'date date-a11y'}).text
            date_of_posting.append(dp)
        except:
            date_of_posting.append('Missing')
    print(1)