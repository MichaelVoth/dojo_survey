from flask import render_template, session, redirect, request    #Imports flask functionalilty
from flask_app import app   #Imports flask app

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_survey():
    session['form_data'] = request.form
    return redirect('/results')

@app.route('/results')
def results_page():
    return render_template('results.html')