from flask import Flask, request, jsonify
from flask_cors import CORS
import gpt4web

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json['query']
    try:
        # Get a doc chunk
        doc_chunk = next(gpt4web.doc_gen)
    except StopIteration:
        # No more docs
        doc_chunk = ""
    response = gpt4web.generate_response(query, doc_chunk)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(port=5000)