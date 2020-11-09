from flask import Flask, render_template

from controllers.player_controllers import players_blueprint
from controllers.game_controllers import games_blueprint
from controllers.tournament_controllers import tournaments_blueprint

app = Flask(__name__)

app.register_blueprint(players_blueprint)
app.register_blueprint(games_blueprint)
app.register_blueprint(tournaments_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)