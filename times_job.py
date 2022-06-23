from bs4 import BeautifulSoup
import requests


def scrape_time(job,loc='',exp=0):
    html = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job}&txtLocation={loc}&cboWorkExp1={exp}').text

    #print(html)

    soup = BeautifulSoup(html,'lxml')
    job_boxs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
     
    results = []
    for job_box in job_boxs:
        comp_name = job_box.find('h3',class_='joblist-comp-name').text.strip()
        job_title = job_box.find('h2').text.strip()
        job_post_link = job_box.find('h2').a["href"]
        skills = [s.strip()  for s in job_box.find('span',class_='srp-skills').text.split(",")]
        job_dtl_ul = job_box.find('ul',class_='top-jd-dtl clearfix')
        job_dtl_li = job_dtl_ul.find_all('li')
        
        job_dtls = []
        for x in job_dtl_li:
            x.i.decompose()
            job_dtls.append(x.text)

        exp,salary,loc = "" , "", ""
        
        if len(job_dtls) == 3 :
            exp = job_dtls[0]
            salary = job_dtls[1]
            loc = job_dtls[2].replace('\n',"")
        else :
            exp = job_dtls[0]
            loc = job_dtls[1].replace('\n',"")

        res = {
            "Company_Name" : comp_name,
            "Job_Title" : job_title,
            "skills" : skills,
            "Experience" : exp,
            "Salary" : salary,
            "Location" : loc,
            "Job_post_link" : job_post_link,
        }
        results.append(res)

    return results