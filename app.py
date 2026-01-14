from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
	"status": "success",
	"message": "Flask App Successfully Deployed on Docker/Jenkins!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "health"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
