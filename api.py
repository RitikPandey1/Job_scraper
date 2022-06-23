from fastapi import FastAPI

from  times_job import scrape_time
from naukri_com import scrape_naukri
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/jobs/{title}/{loc}/{exp}")
async def get_jobs(title,loc,exp):

    time_job_jobs =  scrape_time(title,loc,exp)
    naukri_com_jobs = await scrape_naukri(title,loc,exp) 
    print(len(time_job_jobs))
    print(len(naukri_com_jobs))
    return {
        "timesJob_com" : time_job_jobs[:11],
        "naukri_com" : naukri_com_jobs[:11] 
    }
