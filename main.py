from core.intent_classifier import classify_intent
from core.command_router import route_command

def main():
    print("🛡 Sentinel-X Activated")
    print("Type 'exit' to shutdown.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Sentinel-X shutting down...")
            break

        intent = classify_intent(user_input)
        response = route_command(intent, user_input)

        print("Sentinel-X:", response)

if __name__ == "__main__":
    main()

