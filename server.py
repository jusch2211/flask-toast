from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Erforderlich für Flash-Nachrichten

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger-toast')
def trigger_toast():
    # Hier wird eine Flash-Nachricht hinzugefügt
    flash("Dies ist ein Toast mit Flask!")
    return redirect(url_for('index'))  # Weiterleitung zur Startseite

if __name__ == '__main__':
    app.run(debug=True)
