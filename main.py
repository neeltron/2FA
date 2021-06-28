from flask import Flask, render_template, request, make_response, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
import os




app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/', methods =["GET", "POST"])
def index():
  if request.method == "POST":
    email = request.form.get("email") 
    password = request.form.get("password")
    print("here")
    if email == "lmao" and password == "blahaj":
      
      return redirect(url_for('second'))
  
  return render_template('index.html')



# Creating different routes
@app.route('/2fa')
def second():
  return "I'm on a separate route"



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
