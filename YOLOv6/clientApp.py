from flask import Flask, request, jsonify, render_template,Response
import os
from flask_cors import CORS, cross_origin
from include.decode_utils.utils import decodeImage
from detect import Detector

import sys
# sys.path.insert(0, './com_ineuron_apparel')

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
       
      


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        fileformat = 'https://www.youtube.com/watch?v=XvNsLKd5gsg'
        clApp = ClientApp()
        Object_detection = Detector(clApp.filename, fileformat)
        decodeImage(image, clApp.filename)
        result = Object_detection.detect_action()

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    port = 9501
    app.run(host='127.0.0.1', port=port)