from flask import Flask, request, jsonify, abort
from app.parse_data import parse
import traceback
app = Flask(__name__)


@app.route("/submit_data", methods=['POST'])
def post_data():
    try:
        # request.form.get('first_name', "")
        # if not (request.form['theme'] or
        #         request.form['affiliation'] or
        #         request.form['first_name'] or
        #         request.form['last_name'] or
        #         request.form['email'] or
        #         request.form['phone_number'] or
        #         request.form['university'] or
        #         request.form['street_address'] or
        #         request.form['city'] or
        #         request.form['state'] or
        #         request.form['country'] or
        #         request.form['zip_code']):
        #     return jsonify({'success': False, 'error': "Missing Parameters"}), 400
        print(request.form)
        parse(theme=request.form['theme'],
              affiliation=request.form['affiliation'],
              first_name=request.form['first_name'],
              last_name=request.form['last_name'],
              email=request.form['email'],
              phone_number=request.form['phone_number'],
              university=request.form['university'],
              street_address=request.form['street_address'],
              city=request.form['city'],
              state=request.form['state'],
              country=request.form['country'],
              zip_code=request.form['zip_code'],
              secondary_authors=request.form.get('secondary_authors', None),
              abstract=request.files.get('abstract', None),
              file_name=request.files['abstract'].filename if request.files.get('abstract', None) else None,
              mime_type=request.files['abstract'].mimetype if request.files.get('abstract', None) else None,
              )
        return jsonify({'success': True}), 200
    except Exception as e:
        print(traceback.format_exc())
        # print(e)
        return str(e), 500



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
