def validate_input(data):
    required = ["name", "email", "phone"]

    for field in required:
        if not data.get(field):
            return False

    return True