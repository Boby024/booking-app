from flask import make_response, jsonify


def response_data(data, code, serialized=False):
    headers = {
        "Content-Type": "text/json",
    }
    if serialized == True:
        data = [item.serialize() for item in data]
        print(data)
        return make_response(jsonify(data), code, headers)
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
