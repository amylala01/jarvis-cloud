from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("message", "")

    # TODO: GPT model se smart response yaha likhna
    response = f"Jarvis says: '{user_input}' ka reply yeh ho sakta hai."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
