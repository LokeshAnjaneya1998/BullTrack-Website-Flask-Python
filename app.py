from flask import Flask, render_template, jsonify, request,send_file, url_for, flash, redirect
from services.data_service import DataService
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '21c879ef1a404fe8cc172681bb290b9f'

dataService = DataService()

@app.route("/home")
def home():

    return render_template('home.html', data=dataService.getData(), upcoming_events=dataService.getUpcomingEvents())

@app.route('/image')
def serve_image():
    return send_file('./static/images/fullusflogo.png', mimetype='image/png')

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

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=7778)