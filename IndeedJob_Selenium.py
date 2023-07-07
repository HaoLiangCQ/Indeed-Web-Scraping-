import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver. support.ui import WebDriverWait
from selenium.webdriver. support import expected_conditions as EC
# specify driver path
DRIVER_PATH = '/Users/Nian/Desktop/School/BusinessSchool_RA/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

location = ["Green Bay", "San Francisco", "Omaha"]


def crawler():
    try:
        pop_window = driver.find_element(by=By.ID, value='popover-x')
        pop_window.click()
    except:
        pass
    links = []
    detail_paths = driver.find_elements(by=By.CLASS_NAME, value='jcs-JobTitle')
    for detail_path in detail_paths:
        links.append(detail_path.get_attribute("href"))
    current_page = driver.current_url
    for m in range(len(links)):
        driver.get(links[m])

        try:
            pop_window = driver.find_element(by=By.ID, value='popover-x')
            pop_window.click()
        except:
            pass

        try:
            job_title = driver.find_element(by=By.XPATH, value=
            '//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/h1').text
        except:
            try:
                job_title = driver.find_element(by=By.XPATH, value=
                '//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[3]/div[1]/div[1]/h1').text
            except:
                job_title = "None"
        titles.append(job_title)

        try:
            job_company = driver.find_element(by=By.XPATH, value=
            '//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/a').text
        except:
            try:
                job_company = driver.find_element(by=By.XPATH, value=
                '//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div').text
            except:
                job_company = "None"
        companies.append(job_company)

        try:
            job_location = driver.find_element(by=By.XPATH, value=
            '//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text
        except:
            try:
                job_location = driver.find_element(by=By.XPATH, value='//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div/div/div/div[2]/div').text
            except:
                job_location = "None"
        locations.append(job_location)

        try:
            job_salary = driver.find_element(by=By.XPATH, value='//*[@id="jobDetailsSection"]/div[2]/span').text
        except:
            job_salary = "None"
        salaries.append(job_salary)

        try:
            job_type = driver.find_element(by=By.XPATH, value='//*[@id="jobDetailsSection"]/div[2]/div[2]').text
        except:
            job_type = "None"
        types.append(job_type)

        try:
            job_description = driver.find_element(by=By.XPATH, value='//*[@id="jobDescriptionText"]').text
        except:
            job_description = "None"
        descriptions.append(job_description)

        try:
            review_page = driver.find_element(by=By.XPATH, value='//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[3]/div/div/a').get_attribute("href")
            driver.get(review_page)
            OverallRating.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[1]/div/div/span').text)
            WorkLife_Balance.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[1]/div/div').text)
            Compensation_Benefits.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[2]/div/div').text)
            JobSecurity_Advancement.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[3]/div/div').text)
            Management.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[4]/div/div').text)
            Culture.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[5]/div/div').text)
            review_combine = ""
            visible_reviews = driver.find_elements(by=By.XPATH, value='//span[@aria-hidden="false"]//span[@class="css-82l4gy eu4oa1w0"]')
            for visible_review in visible_reviews:
                review_combine += visible_review.text
            hidden_reviews = driver.find_elements(by=By.XPATH, value='//span[@aria-hidden="true"]//span[@class="css-82l4gy eu4oa1w0"]')
            for hidden_review in hidden_reviews:
                review_combine += hidden_review.text
            Reviews.append(review_combine)
        except:
            try:
                review_page = driver.find_element(by=By.XPATH, value='//*[@id="viewJobSSRRoot"]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[3]/div/div/a').get_attribute("href")
                driver.get(review_page)
                OverallRating.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[1]/div/div/span').text)
                WorkLife_Balance.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[1]/div/div').text)
                Compensation_Benefits.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[2]/div/div').text)
                JobSecurity_Advancement.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[3]/div/div').text)
                Management.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[4]/div/div').text)
                Culture.append(driver.find_element(by=By.XPATH, value='//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[2]/div[3]/div[3]/div[5]/div/div').text)
                review_combine = ""
                visible_reviews = driver.find_elements(by=By.XPATH, value='//span[@aria-hidden="false"]//span[@class="css-82l4gy eu4oa1w0"]')
                for visible_review in visible_reviews:
                    review_combine \
                        += visible_review.text
                hidden_reviews = driver.find_elements(by=By.XPATH, value='//span[@aria-hidden="true"]//span[@class="css-82l4gy eu4oa1w0"]')
                for hidden_review in hidden_reviews:
                    review_combine += hidden_review.text
                Reviews.append(review_combine)
            except:
                OverallRating.append("None")
                WorkLife_Balance.append("None")
                Compensation_Benefits.append("None")
                JobSecurity_Advancement.append("None")
                Management.append("None")
                Culture.append("None")
                Reviews.append("None")

    driver.get(current_page)

    try:
        pop_window = driver.find_element(by=By.ID, value='popover-x')
        pop_window.click()
    except:
        pass

    try:
        next_page = driver.find_element(by=By.CSS_SELECTOR, value='a[aria-label=Next]')
        next_page.click()
        crawler()
    except:
        try:
            more_page = driver.find_element(by=By.XPATH, value='//*[@id="resultsCol"]/p/a').get_attribute("href")
            driver.get(more_page)
            crawler()
        except:
            print("all page loaded")

for i in range(len(location)):
    # go to indeed advanced search website
    driver.get('https://www.indeed.com/advanced_search')
    try:
        pop_window = driver.find_element(by=By.ID, value='popover-x')
        pop_window.click()
    except:
        pass
    # search job contains words retail
    search_job = driver.find_element(by=By.XPATH, value='//*[@id="as_any"]')
    search_job.send_keys(['retail'])
    # set the job perimeter to exact location
    job_perimeter = driver.find_element(by=By.XPATH, value='//*[@id="radius"]/option[1]')
    job_perimeter.click()
    # input location preference
    search_location = driver.find_element(by=By.XPATH, value='//*[@id="where"]')
    search_location.send_keys(location[i])
    # set the display to 50 jobs per page
    display_limit = driver.find_element(by=By.XPATH, value='//*[@id="limit"]/option[4]')
    display_limit.click()
    # sort by date
    sort_option = driver.find_element(by=By.XPATH, value='//*[@id="sort"]/option[2]')
    sort_option.click()
    # click search button
    search_button = driver.find_element(by=By.XPATH, value='//*[@id="fj"]')
    search_button.click()
    #let the driver wait 3 seconds to locate the element before exiting out
    driver.implicitly_wait(3)
    titles = []
    companies = []
    locations = []
    types = []
    all_links = []
    salaries = []
    descriptions = []
    WorkLife_Balance = []
    Compensation_Benefits = []
    JobSecurity_Advancement = []
    Management = []
    Culture = []
    OverallRating = []
    Reviews = []
    crawler()

    df = pd.DataFrame()
    df['Title'] = titles
    df['Company'] = companies
    df['Location'] = locations
    df['Salary'] = salaries
    df['Type'] = types
    df['Description'] = descriptions
    df['Overall Rating'] = OverallRating
    df['Work/Life Balance'] = WorkLife_Balance
    df['Compensation/Benefits'] = Compensation_Benefits
    df['Job Security/Advancement'] = JobSecurity_Advancement
    df['Management'] = Management
    df['Culture'] = Culture
    df['Reviews'] = Reviews
    df.to_csv(location[i]+" Retail.csv", mode='a', header=False, index=False, encoding='gb18030')

print(1)

