from flask import Flask, render_template, request,  redirect
import smtplib
from email.mime.multipart import MIMEMultipart
import os
import random



def sendOTP():
  sender_address = os.environ['email']
  sender_pass = os.environ['pass']
  receiver_address = 'nprosofficial@gmail.com'
  otp = random.randint(1000, 9999)

  message = MIMEMultipart()

  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = 'Your OTP is ' + str(otp)

  session = smtplib.SMTP('smtp.gmail.com', 587)
  session.starttls()
  session.login(sender_address, sender_pass)
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()
  print('Mail Sent')
  return otp



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
    if email == "neeltr.n@gmail.com" and password == "blahaj":
      return redirect(url_for('second'))
  
  return render_template('index.html')



# Creating different routes
@app.route('/2fa', methods = ["GET", "POST"])
def second():
  a = sendOTP()
  flag = 0
  if request.method == "POST" and flag == 0:
    otp = request.form.get("otp")
    flag = 1
    if a == otp:
      return "Verified!"
    else:
      return "Incorrect OTP!"
  return render_template('2fa.html')



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
