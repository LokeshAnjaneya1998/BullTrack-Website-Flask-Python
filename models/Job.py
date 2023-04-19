class Job:

    def __init__(self, company, job_role, applied_on, location, salary, status):
        self.company = company
        self.job_role = job_role
        self.applied_on = applied_on
        self.location = location
        self.salary = salary
        self.status = status

    def getDictObject(self):
        data = {
            "company": self.company,
            "job_role": self.job_role,
            "applied_on": self.applied_on,
            "location": self.location,
            "salary": self.salary,
            "status": self.status,
            }
        return data