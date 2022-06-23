import axios from "axios";
import { useState } from "react";
import Result from "./Result";

function Form(){

    const [job,setJob] = useState("");
    const [exp,setExp] = useState("");
    const [loc,setLoc] = useState("");
    const [load,setLoad] = useState(false);

    const[res,setRes] = useState();
 
    const getJobs = async ()=>{
       setLoad(true);
       setRes({});
       const {data} = await axios.get(`http://127.0.0.1:8000/jobs/${job}/${loc}/${exp}`);
       console.log(data);
       setRes(data);
       setLoad(false);
    }

    return <div className="w-8/12 mx-auto mt-16 ">
<div className="flex flex-row space-x-4 ">
<input value={job} onChange={(e)=>setJob(e.target.value)} className="basis-1/3 border-2 p-2 rounded-lg focus:border-teal-500 focus:outline-none" type="text" placeholder="Enter Job Title."/>
<input value={exp} onChange={(e)=>setExp(e.target.value)} className="basis-1/3 border-2 p-2 rounded-lg focus:border-teal-500 focus:outline-none" type="text" placeholder="Enter Experience."/>
<input value={loc} onChange={(e)=>setLoc(e.target.value)} className="basis-1/3 border-2 p-2 rounded-lg focus:border-teal-500 focus:outline-none" type="text" placeholder="Enter Location."/>
</div>
<div className="flex justify-center mt-6">
<button disabled={!(exp&&job&&loc)} onClick={getJobs} className="bg-teal-500 p-2 text-white rounded disabled:opacity-50"> {load? "Loading..." : "Find Job" }</button>
</div>
<Result res={res}/>
    </div> 
 



}

export default Form;