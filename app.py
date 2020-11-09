from flask import Flask, render_template

from controllers.park_controller import parks_blueprint

app = Flask(__name__)

app.register_blueprint(parks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

