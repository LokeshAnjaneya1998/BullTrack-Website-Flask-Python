
from models.Job import Job

class DataService:

    def __init__(self):
        self.allJobData = [
            {
            "id": 1,
            "company": "Microsoft",
            "job_role": "Software Engineer",
            "applied_on": "2023/03/21",
            "location": "Tampa, FL",
            "salary": "50000",
            "status": "IN_PROCESS",
            },
            {
            "id": 2,
            "company": "Microsoft",
            "job_role": "Software Engineer",
            "applied_on": "2023/03/21",
            "location": "Tampa, FL",
            "salary": "50000",
            "status": "APPLIED",
            },
            {
            "id": 3,
            "company": "Microsoft",
            "job_role": "Software Engineer",
            "applied_on": "2023/03/21",
            "location": "Tampa, FL",
            "salary": "50000",
            "status": "OFFER",
            },
            {
            "id": 4,
            "company": "Microsoft",
            "job_role": "Software Engineer",
            "applied_on": "2023/03/21",
            "location": "Tampa, FL",
            "salary": "50000",
            "status": "APPLIED",
            },
            {
            "id": 5,
            "company": "Microsoft",
            "job_role": "Software Engineer",
            "applied_on": "2023/03/21",
            "location": "Tampa, FL",
            "salary": "50000",
            "status": "WISHLIST",
            },
            {
            "id": 6,
            "company": "Microsoft",
            "job_role": "Software Engineer",
            "applied_on": "2023/03/21",
            "location": "Tampa, FL",
            "salary": "50000",
            "status": "APPLIED",
            },
            {
            "id": 7,
            "company": "Microsoft",
            "job_role": "Software Engineer",
            "applied_on": "2023/03/21",
            "location": "Tampa, FL",
            "salary": "50000",
            "status": "IN_PROCESS",
            }
        ]

    
    def getData(self): 
        data = {
            "wishlist": ["Microsoft", "Google", "Uber"],
            "inprogress": ["Twitter", "Pearson"],
            "applied": ["Amazon", "NetApp"],
            "offers": ["Perfios", "Amazon"]
        }
        return data
    
    def getUpcomingEvents(self):
        upcoming_events = [
            {"duedate": "28th Sept, 2021",
            "company": "Apple"
            },
            {"duedate": "19th Dec, 2021",
            "company": "Microsoft"
            },
            {"duedate": "21st Dec, 2021",
            "company": "Amazon"
            },
            {"duedate": "21st Dec, 2021",
            "company": "Amazon"
            },
            {"duedate": "21st Dec, 2021",
            "company": "Amazon"
            }
        ]
        return upcoming_events
    
    def addJob(self, job_data):
        job = Job(job_data['company'], job_data['job_role'],
                   job_data['applied_on'], job_data['location'], 
                   job_data['salary'], job_data['job_status'])
        # TODO: Write code to save job in DB
        job_object = job.getDictObject()
        max_id = 1
        for item in self.allJobData:
            if item['id'] > max_id:
                max_id = item['id']
        job_object['id'] = max_id + 1
        self.allJobData.append(job_object)
        pass

    def deleteJob(self, job_id):
        # TODO: Write code to delete job in DB
        self.allJobData[:] = [d for d in self.allJobData if d.get('id') != job_id]
        pass

    def updateJobStatus(self, job_id, newStatus):
        #TODO: Write code to update job status in DB
        for item in self.allJobData:
            if item['id'] == job_id:
                my_item = item
                break
        else:
            my_item = None
        
        self.deleteJob(job_id)
        my_item['status'] = newStatus
        self.allJobData.append(my_item)
        

    def getAllJobData(self):
        return sorted(self.allJobData, key=lambda d: d['id'])

