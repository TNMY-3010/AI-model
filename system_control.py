import os

def open_application(text):
    if "chrome" in text:
        os.system("start chrome")
        return "Opening Chrome..."
    else:
        return "Application not recognized."

