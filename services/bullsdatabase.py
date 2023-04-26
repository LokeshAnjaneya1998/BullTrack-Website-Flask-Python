import sqlite3


def insert_data(dataTable, company_name, job_role, applied_on, location, salary, job_status):
    connection = sqlite3.connect('./models/bullsDataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,company_name TEXT,job_role TEXT,\
                      applied_on TEXT,location TEXT,salary NUMERIC,job_status TEXT)".format(dataTable))

    connection.commit()
    dbrequest.execute("INSERT INTO {} (company_name, job_role, applied_on, location, salary, job_status) \
                      VALUES (?, ?, ?, ?, ?, ?)".format(dataTable), (company_name, job_role, applied_on, location, salary, job_status))
    connection.commit()
    connection.close()


