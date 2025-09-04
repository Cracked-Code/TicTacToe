from flask import Flask, request, jsonify, render_template
from game import TicTacToe

app = Flask(__name__)
game = TicTacToe()
print(game.won())
@app.route("/")
def home():
    return render_template("index.html")  # serves frontend

@app.route("/state", methods=["GET"])
def get_state():
    return jsonify(game.get_state())

@app.route("/move", methods=["POST"])
def make_move():
    data = request.json
    row = data.get("row")
    col = data.get("col")
    return jsonify(game.make_move(row, col))

@app.route("/reset", methods=["POST"])
def reset_game():
    game.reset()
    return jsonify({"message": "Game reset", "state": game.get_state()})

if __name__ == "__main__":
    app.run(debug=True)
