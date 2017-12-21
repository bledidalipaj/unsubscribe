import datetime
import os
from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)

HOST = os.getenv('IP', '0.0.0.0')
PORT = int(os.getenv('PORT', 8080))

@app.route('/success')
def unsubscribe():
    return render_template('done.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        
        # add email to mails.txt
        with open('mails.txt', 'a') as f:
            date = datetime.datetime.now().strftime('%d %B %Y')
            
            f.write('{} {}\n'.format(date, email))
        
        return redirect(url_for('unsubscribe'))
            
    return render_template('unsubscribe.html')

    
app.run(host=HOST, port=PORT)
if __name__ == '__main__':
    app.run(debug=True)