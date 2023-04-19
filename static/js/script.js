async function deleteJob(id) {
    let response = await post('/deleteJob', { "job_id": +id });
    alert("Job has been deleted");
    console.log(response);
    window.location.reload();
}

async function addNewJob() {
    let company_name = document.getElementById('company_name').value;
    let location = document.getElementById('location').value;
    let job_profile = document.getElementById('job_profile').value;
    let salary = document.getElementById('salary').value;
    let job_status = document.getElementById('status').value;
    let applied_on = document.getElementById('date_applied').value;

    let data = {
        'company': company_name,
        'job_role': job_profile,
        'applied_on': applied_on,
        'location': location,
        'salary': salary,
        'job_status': job_status
    };

    let response = await post('/addNewJob', data);
    alert("Added New Job")
    window.location.reload();
}

async function updateJobStatus(job_id, job_status) {
    let data = {
        'job_id': +job_id,
        'job_status': job_status
    };
    console.log(job_id);

    let response = await post('/updateJobStatus', data);
    console.log(response)
    alert("Job Status Updated");
    window.location.reload();
}