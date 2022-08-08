from flask import Flask, request, jsonify, abort
from app.parse_data import parse
import traceback
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route("/submit_data", methods=['POST'])
@cross_origin()
def post_data():
    try:
        print(request.form)
        if not ('theme' in request.form and
                'title' in request.form and
                'affiliation' in request.form and
                'first_name' in request.form and
                'last_name' in request.form and
                'email' in request.form and
                'phone_number' in request.form and
                'university' in request.form and
                'street_address' in request.form and
                'city' in request.form and
                'state' in request.form and
                'country' in request.form and
                'zip_code' in request.form):
            print(request.form)
            return jsonify({'success': False, 'error': "Missing Parameters"}), 400
        parse(theme=request.form['theme'],
              title=request.form['title'],
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
              is_travel_grant_needed=request.files['is_travel_grant_needed'] if request.files.get('is_travel_grant_needed', None) else False,
              travel_grant_cost=request.files['travel_grant_cost'] if request.files.get('travel_grant_cost', None) else 0,
              )
        return jsonify({'success': True}), 200
    except Exception as e:
        print(traceback.format_exc())
        # print(e)
        return str(e), 500


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5001)
    context = ('/etc/letsencrypt/live/servertestabctestserver.tk/fullchain.pem', '/etc/letsencrypt/live/servertestabctestserver.tk/privkey.pem')
    app.run(host='0.0.0.0', port=5001, ssl_context=context)