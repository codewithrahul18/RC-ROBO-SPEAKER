import pyttsx3

if __name__ == '__main__':
    print("Welcome to ROBOSpeaker 1.1 - Created by Rahul 👨‍💻🤖")

    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak (or type 'exit' to quit): ")
        if x.lower() == "exit":
            print("ROBO Speaker shutting down... Goodbye!")
            break

        engine.say(x)
        engine.runAndWait()
