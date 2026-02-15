def classify_intent(text):
    text = text.lower()

    if "open" in text:
        return "open_app"
    elif "study" in text:
        return "study_mode"
    elif "save" in text:
        return "save_memory"
    else:
        return "unknown"

