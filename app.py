from flask import Flask, render_template

from controllers.contestants_controller import contestants_blueprint
from controllers.teams_controller import teams_blueprint


app = Flask(__name__)

app.register_blueprint(contestants_blueprint)
app.register_blueprint(teams_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

