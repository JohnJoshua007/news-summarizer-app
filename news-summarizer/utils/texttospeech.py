import os
import asyncio
from gtts import gTTS
from googletrans import Translator

async def text_to_hindi_speech(text, output_file="output.mp3"):
    """
    Translates English text to Hindi and converts it to speech.
    
    :param text: English text to be translated and converted to speech.
    :param output_file: Filename for the saved audio file.
    :return: File path of the generated speech file.
    """
    translator = Translator()
    
    # Use `await` because `translate` is now async
    translated = await translator.translate(text, src="en", dest="hi")
    
    # Convert Hindi text to speech
    tts = gTTS(translated.text, lang="hi")
    tts.save(output_file)
    
    return os.path.abspath(output_file)

# Example usage
async def main():
    file_path = await text_to_hindi_speech("jljlfajls")
    print(f"Audio file saved at: {file_path}")
    # Windows (Ensure path is enclosed in quotes)
    os.system(f'start "" "{file_path}"')
    # os.system(f"mpg321 {file_path}")  # Linux

# Run the async function
# asyncio.run(main())
