from flask import make_response, jsonify


def response_data(data, code):
    headers = {
        "Content-Type": "text/json",
    }
    return make_response(jsonify(data), code, headers)


def response_error(text: str = None, code=500):
    headers = {
        "Content-Type": "text/json",
    }
    if text:
        msg = {"message": text}
    else:
        msg = {"message": "Internal Server Error"}

    return make_response(jsonify(msg), code, headers)
