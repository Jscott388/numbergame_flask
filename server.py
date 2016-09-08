from flask import Flask, flash, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = '\xb8?\xff\xd4\x1a\xdf\x11\xeaiP2[\x8cs\x1d\x17\x9d\xc5\xcf\x7f\xbb\xf0P\xd3'

def randomNum():
    session['num'] = random.randint(1,100)

def setMessage(status):
    number = request.form['guess']
    if status == 'success':
        session['message'] = ['success', '{} was the number! Play again'.format(number)]
    elif status == 'high':
        session['message'] = ['wrong', 'Too high!']
    else:
        session['message'] = ['wrong', 'Too low!']


@app.route('/')
def index():
    try:
        session['num']
    except:
        randomNum()
    print session['num']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        guess = int(request.form['guess'])
        if request.method == 'POST':
            if guess == session['num']:
                setMessage('success')
            elif guess > session['num']:
                setMessage('high')
            elif guess < session['num']:
                setMessage('low')
            else:
                print "Invaild"
        else:
            print "Invaild"
    except ValueError:
        print "Invaild"


    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('num')
    session['message'] = []
    return redirect('/')

app.run(debug=True)
