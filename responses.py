def handle_response(message):
    p_message = message.lower() # Makes user message in lower_case

    if p_message == "!help":
        return "Our help message"

    if p_message == "!info":
        return "This is a testbot"
