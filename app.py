from flask import Flask, request, jsonify, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Spam Classifier GUI</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 2rem;
      max-width: 600px;
    }
    textarea {
      width: 100%;
      height: 100px;
      font-size: 1rem;
      padding: 0.5rem;
      margin-bottom: 1rem;
      resize: vertical;
    }
    button {
      padding: 0.6rem 1.2rem;
      font-size: 1rem;
      cursor: pointer;
    }
    #result {
      margin-top: 1rem;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Spam Classifier</h1>
  <textarea id="message" placeholder="Type your message here..."></textarea>
  <br />
  <button onclick="predict()">Check Spam</button>
  <div id="result"></div>

  <script>
    async function predict() {
      const message = document.getElementById('message').value.trim();
      if (!message) {
        alert('Please enter a message.');
        return;
      }
      document.getElementById('result').textContent = 'Predicting...';

      try {
        const response = await fetch('/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message })
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById('result').textContent = 'Prediction: ' + data.prediction;
      } catch (err) {
        document.getElementById('result').textContent = 'Error: ' + err.message;
      }
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)  # force=True helps if content-type is correct but Flask has trouble parsing
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400
    try:
        prediction = model.predict([message])
        return jsonify({"prediction": str(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # fallback for local
    app.run(host="0.0.0.0", port=port, debug=True)
