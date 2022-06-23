from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch

html = ""


async def scrape_naukri(job,loc='',exp=0):
    
    async def main():
        browser = await launch()
        page  = await browser.newPage()
        await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
        await  page.goto(f'https://www.naukri.com/{job}-jobs-in-{loc}?k={job}&l={loc}&experience={exp}',{
        'waitUntil' : 'networkidle0',
        })
        global html
        html = await page.content()
        await browser.close()

    #asyncio.get_event_loop().run_until_complete(main())
    await main()
    #
    # print(html)
    soup = BeautifulSoup(html,'lxml')
    #

    job_boxs = soup.find_all('article',class_='jobTuple bgWhite br4 mb-8')
    results = []
    for job_box in job_boxs:
        job_title = job_box.find('a',class_='title fw500 ellipsis').text
        job_link = job_box.find('a',class_='title fw500 ellipsis')['href']
        comp_name = job_box.find('div',class_='mt-7 companyInfo subheading lh16').text
        
        skill_list = job_box.find_all('li',class_='fleft fs12 grey-text lh16 dot')
        skills = [s.text for s in skill_list]
        
        exp = job_box.find('li',class_='fleft grey-text br2 placeHolderLi experience').text
        salary = job_box.find('li',class_='fleft grey-text br2 placeHolderLi salary').text    
        loc = job_box.find('li',class_='fleft grey-text br2 placeHolderLi location').text
        res = {
            "Company_Name" : comp_name,
            "Job_Title" : job_title,
            "skills" : skills,
            "Experience" : exp,
            "Salary" : salary,
            "Location" : loc,
            "Job_post_link" : job_link,
        }
        results.append(res)
    
    return results
        
        