function Result({res}){
   
    return <div className="grid grid-cols-2 gap-4 mt-6">
        <div>
            <div className="border-b-2">
            <h1>TimesJobs.com</h1>
            </div>

            <div className="flex flex-col mt-2 space-y-4">
                 {res && res.timesJob_com && res.timesJob_com.map((c,i) => {
                    return (
                    <div className="border-2 p-4" key={i}>
                    <h1 className="truncate font-bold">{c.Job_Title}</h1>
                    <h3 className="truncate  truncate" >{c.Company_Name}</h3>
                    <h4><span className="text-teal-700">Experience</span> : {c.Experience}</h4>
                    <h4><span  className="text-teal-700">Location</span> : {c.Location}</h4>
                    <h4><span className="text-teal-700">Salary</span> : {c.Salary === ""?"Not disclosed":c.Salary}</h4>
                    <h4> <span className="text-teal-700" >Key Skills</span> : {c.skills.map(s=>s+", ")} </h4> 
                  <a href={c.Job_post_link} target="_blank" rel="noreferrer">
                  <button className="bg-teal-500 p-2 text-white hover:bg-teal-700 rounded mt-4">Apply Now</button>
                    </a>  
                </div>
                    )
                })} 
                
            </div>
            
        </div>
        <div>
            <div className="border-b-2">
            <h1>Naukri.com</h1>
            </div>

            <div className="flex flex-col mt-2 space-y-4">
            {res && res.naukri_com && res.naukri_com.map((c,i) => {
                    return (
                    <div className="border-2 p-4" key={i}>
                    <h1 className="truncate font-bold">{c.Job_Title}</h1>
                    <h3 className="truncate  truncate" >{c.Company_Name}</h3>
                    <h4>Experience : {c.Experience}</h4>
                    <h4>Location : {c.Location}</h4>
                    <h4>Salary : {c.Salary}</h4>
                    <h4>Key Skills : {c.skills.map(s=>s+", ")} </h4> 
                    <a href={c.Job_post_link} target="_blank" rel="noreferrer">
                  <button className="bg-teal-500 p-2 text-white hover:bg-teal-700 rounded mt-4">Apply Now</button>
                    </a> 
                </div>
                    )
                })} 
            </div>
            
        </div>
    </div>

}

export default Result;