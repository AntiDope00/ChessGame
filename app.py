from flask import Flask, render_template, request, jsonify
import chess

app = Flask(__name__)
board = chess.Board()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    uci_move = data.get("move")
    try:
        move = chess.Move.from_uci(uci_move)
        if move in board.legal_moves:
            board.push(move)
            return jsonify({"status": "ok", "fen": board.fen(), "is_game_over": board.is_game_over()})
        else:
            return jsonify({"status": "illegal"})
    except:
        return jsonify({"status": "error"})

@app.route("/reset", methods=["POST"])
def reset():
    global board
    board = chess.Board()
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True)

