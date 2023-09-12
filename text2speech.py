import os

def textToSpeech(text, voice):
    # Use osascript to execute AppleScript for text-to-speech
    script = f'''
    say "{text}" using "{voice}"
    '''
    os.system(f"osascript -e '{script}'")

if __name__ == "__main__":
    print("Welcome to the Text-to-Speech Converter")

    while True:
        inputText = input("Enter the text you want to convert to speech (or 'exit' to quit): ")
        if inputText.lower() == 'exit':
            break

        selectVoice = input("Enter the name of the voice you want to use(Male - Daniel, Female - Samantha, Robot - Zarvox):  ")

        # Convert text to speech with the selected voice
        textToSpeech(inputText, selectVoice)




