from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# In-memory user storage
users = []

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Simple validation
    if username and email and password:
        users.append({'username': username, 'email': email, 'password': password})
        flash("Registration successful!", "success")
        return redirect(url_for('success'))
    flash("Please fill in all fields.", "error")
    return redirect(url_for('home'))

@app.route('/success')
def success():
    return render_template('success.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
