
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'secret_key_here'

# Mail config (replace with your real credentials or Mailtrap later)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'drhomeproducts20@gmail.com'
app.config['MAIL_PASSWORD'] = 'kwnmrwixweqntbse'
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
    print(">>> Contact route was accessed")
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject=f"Contact from {name}",
                      sender=email,
                      recipients=['redando.dieujuste00@gmail.com'],
                      body=message)
        mail.send(msg)
        flash('Message sent successfully!')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
