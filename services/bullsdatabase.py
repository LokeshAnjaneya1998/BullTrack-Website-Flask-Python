import sqlite3

def insert_signup_data(name,school,email, user_name, password):
    connection = sqlite3.connect('./models/bullsDataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS signupdata (id INTEGER PRIMARY KEY, name, school, email, user_name, password, flag)")

    connection.commit()
    dbrequest.execute("INSERT INTO signupdata (name, school, email, user_name, password) \
                      VALUES (?, ?, ?, ?, ?)", (name, school, email, user_name, password))
    connection.commit()
    connection.close()

def get_signup_data():
   connection = sqlite3.connect('./models/bullsDataBase.db')
   dbrequest = connection.cursor()
   dbrequest.execute("CREATE TABLE IF NOT EXISTS signupdata (id INTEGER PRIMARY KEY, name, school, email, user_name, password, flag)")
   connection.commit()
   dbrequest.execute("SELECT * FROM signupdata")
   userdisplayData = [{'id': row[0], 'name': row[1], 'school': row[2], 'email': row[3], 'user_name': row[4], 'password': row[5], 'flag': row[6]} for row in dbrequest.fetchall()]
   connection.close()
   return userdisplayData

def update_signup_flag(userflag, userid):
   connection = sqlite3.connect('./models/bullsDataBase.db')
   dbrequest = connection.cursor()
   dbrequest.execute("CREATE TABLE IF NOT EXISTS signupdata (id INTEGER PRIMARY KEY, name, school, email, user_name, password, flag)")
   connection.commit()
   dbrequest.execute("UPDATE signupdata SET flag = ? WHERE id = ?",(userflag, userid))
   connection.commit()
   connection.close()

def dataName():
    dbname = get_signup_data()
    for user in dbname:
        if user['flag'] == 'True':
            userdbfun = user['user_name'].replace(" ","")
    print('connected to db'+ userdbfun)
    return userdbfun

def insert_event_data(dataTable, company_name,job_role, event_name, due_date):
    connection = sqlite3.connect('./models/DataBase.db')
    dbrequest = connection.cursor()
    print('debug'+dataName())
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,user_name, company_name, job_role, event_name, due_date)"
                      .format(dataTable))

    connection.commit()
    dbrequest.execute("INSERT INTO {} (user_name, company_name, job_role, event_name, due_date) \
                      VALUES (?, ?, ?, ?, ?)".format(dataTable), (dataName(), company_name, job_role, event_name, due_date))
    connection.commit()
    connection.close()

def get_event_data(dataTable):
   print('debug2'+dataName())
   connection = sqlite3.connect('./models/DataBase.db')
   dbrequest = connection.cursor()
   dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, user_name, company_name, job_role, event_name, due_date)".format(dataTable))
   connection.commit()
   dbrequest.execute("SELECT * FROM {} WHERE user_name = '{}' ORDER BY due_date".format(dataTable, dataName()))
   displayData = [{'id': row[0], 'company_name': row[2], 'job_role': row[3], 'event_name': row[4], 'due_date': row[5]} for row in dbrequest.fetchall()]
   connection.close()
   return displayData

def insert_data(dataTable, company_name, job_role, applied_on, location, salary, job_status):
    connection = sqlite3.connect('./models/DataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,user_name, company_name TEXT,job_role TEXT,\
                      applied_on TEXT,location TEXT,salary NUMERIC,job_status TEXT)".format(dataTable))

    connection.commit()
    dbrequest.execute("INSERT INTO {} (user_name, company_name, job_role, applied_on, location, salary, job_status) \
                      VALUES (?, ?, ?, ?, ?, ?, ?)".format(dataTable), (dataName(), company_name, job_role, applied_on, location, salary, job_status))
    connection.commit()
    connection.close()

def get_data(dataTable):
    connection = sqlite3.connect('./models/DataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, user_name, company_name TEXT,job_role TEXT,\
                      applied_on TEXT,location TEXT,salary NUMERIC,job_status TEXT)".format(dataTable))

    connection.commit()
    dbrequest.execute("SELECT * FROM {} WHERE user_name = '{}' ORDER BY applied_on".format(dataTable, dataName()))
    displayData = [{'id': row[0], 'company_name': row[2], 'job_role': row[3], 'applied_on': row[4], 'location': row[5], \
                    'salary': row[6], 'job_status': row[7]} for row in dbrequest.fetchall()]
    connection.close()
    return displayData

def delete_data(dataTable, id):
    connection = sqlite3.connect('./models/DataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("DELETE FROM {} WHERE user_name = '{}' AND id = ?".format(dataTable, dataName()), (id,))
    connection.commit()
    connection.close()

def update_data(dataTable, id, dataTableTargetValue):
    if dataTableTargetValue == 'WISHLIST':
        dataTableTarget = "wishlistdata"
    if dataTableTargetValue == 'IN_PROCESS':
        dataTableTarget = "inprocessdata"
    if dataTableTargetValue == 'APPLIED':
        dataTableTarget = "applieddata"
    if dataTableTargetValue == 'OFFER':
        dataTableTarget = "offerdata"
    connection = sqlite3.connect('./models/DataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, user_name, company_name TEXT,job_role TEXT,\
                      applied_on TEXT,location TEXT,salary NUMERIC,job_status TEXT)".format(dataTable))

    connection.commit()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, user_name, company_name TEXT,job_role TEXT,\
                      applied_on TEXT,location TEXT,salary NUMERIC,job_status TEXT)".format(dataTableTarget))

    connection.commit()
    dbrequest.execute("SELECT * FROM {} WHERE user_name = '{}' AND id = ?".format(dataTable, dataName()), (id,))
    data = dbrequest.fetchone()

    if data:
        dbrequest.execute("INSERT INTO {} (user_name, company_name, job_role, applied_on, location, salary, job_status) \
                          VALUES (?, ?, ?, ?, ?, ?, ?)".format(dataTableTarget), (data[1], data[2], data[3], data[4], data[5], data[6], dataTableTargetValue))
        connection.commit()


        dbrequest.execute("DELETE FROM {} WHERE user_name = '{}' AND id = ?".format(dataTable, dataName()), (id,))
        connection.commit()

    connection.close()

def chart_data(dataTable):
    connection = sqlite3.connect('./models/DataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("SELECT applied_on FROM {} WHERE user_name = '{}'".format(dataTable, dataName()))
    displayData = [{'applied_on': row[0]} for row in dbrequest.fetchall()]

    connection.commit()
    connection.close()
    return displayData

