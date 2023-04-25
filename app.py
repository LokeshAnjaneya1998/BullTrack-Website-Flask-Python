from flask import Flask, render_template, jsonify, request,send_file
from services.data_service import DataService

app = Flask(__name__)

dataService = DataService()

@app.route("/")

@app.route("/home")
def home():

    return render_template('home.html', data=dataService.getData(), upcoming_events=dataService.getUpcomingEvents())

@app.route('/image')
def serve_image():
    return send_file('./img/fullusflogo.png', mimetype='image/png')

@app.route('/view', methods=['GET'])
def view():
    return render_template('view_list.html', data=dataService.getAllJobData())

@app.route('/addNewJob', methods=['POST'])
def addNewJob():
    job_data = request.get_json()
    dataService.addJob(job_data)
    response = {"status": "Success"}
    return jsonify(response)

@app.route('/deleteJob', methods=['POST'])
def delete():
    job_data = request.get_json()
    dataService.deleteJob(job_id=job_data['job_id'])
    print('delete called')
    response = {"status": "Success"}
    return jsonify(response)

@app.route('/updateJobStatus', methods=['POST'])
def updateJobStatus():
    job_data = request.get_json()
    print(job_data)
    job_id = job_data['job_id']
    job_status = job_data['job_status']
    dataService.updateJobStatus(job_id, newStatus=job_status)
    response = {"status": job_status}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=7778)