from modules.system_control import open_application
from modules.study_mode import start_study_session
from modules.memory_manager import save_memory

def route_command(intent, text):
    if intent == "open_app":
        return open_application(text)

    elif intent == "study_mode":
        return start_study_session()

    elif intent == "save_memory":
        return save_memory(text)

    else:
        return "I don't understand that yet."

