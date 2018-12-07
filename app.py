import os
from flask import Flask, request, send_file, url_for
from flask_json import FlaskJSON, JsonError, json_response, as_json
import numpy as np
import cv2
import image_detection
import fetching_satellite


app = Flask(__name__)
FlaskJSON(app)


@app.route("/", methods=['GET', 'POST'])
def welcome():
    return json_response(welcome=True)


@app.route("/state", methods=['GET', 'POST'])
def fetch_lastest():
    im = cv2.imread("./tmp/img1.jpg")
    if image_detection.white_percentage(im) > 40:
        return json_response(text="DANGER ne pas sortir aujourd'hui!")
    return json_response(text="Pas de problème aujourd'hui!")


@app.route('/latest-image', methods=['GET', 'POST'])
def get_image():
    filename = './tmp/img1.jpg'
    return send_file(filename, mimetype='image/jpg')


@app.route('/latest-image-perturbation', methods=['GET', 'POST'])
def get_image_pert():
    filename = './tmp/img1-pert.jpg'
    return send_file(filename, mimetype='image/jpg')


def close():
    # os.system("rm -rf /home/omni/repos/geo-spatial-api/tmp/*")
    pass


if __name__ == "__main__":
    app.run(debug=False)
    close()
