from flask import Flask, request, jsonify, render_template
from game import TicTacToe

app = Flask(__name__)
game = TicTacToe()

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
    game.make_move(row, col)
    return jsonify(game.get_state())

@app.route("/ai_move", methods=["POST"])    
def ai_move():
    game.ai_move()
    return jsonify(game.get_state())    

@app.route("/reset", methods=["POST"])
def reset_game():
    game.reset()
    return jsonify({"message": "Game reset", "state": game.get_state()})

if __name__ == "__main__":
    app.run(debug=True)
