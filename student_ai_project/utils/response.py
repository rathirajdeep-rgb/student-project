def success_response(data):
    return {
        "status": "success",
        "data": data,
        "error": None

    }

def error_response(message):
    return {
        "status": "error",
        "data": None,
        "error": message
    }