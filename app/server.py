from flask import Flask, request, jsonify, abort
from app.parse_data import parse

app = Flask(__name__)


@app.route("/data", methods=['POST'])
def post_data():
    # request.form.get('first_name', "")
    print(request.form)
    parse(request.form['event_type'],
          request.form['first_name'],
          request.form['last_name'],
          request.form['email'],
          request.files.get('abstract', None),
          request.files['abstract'].filename if request.files.get('abstract', None) else None,
          request.files['abstract'].mimetype if request.files.get('abstract', None) else None,
          )
    return jsonify({'success': True}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
