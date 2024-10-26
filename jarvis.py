from RealtimeSTT import AudioToTextRecorder
import assist_local as assist
import time

if __name__ == '__main__':
    recorder = AudioToTextRecorder(spinner=True, model="tiny.en", language="en", post_speech_silence_duration =0.2, silero_sensitivity = 0.4)
    hot_words = ["jarvis", "javis", "jovis" , "javi", "jovi", "chavez", "minifab", "jollis"]
    skip_hot_word_check = True
    print("Say something...")
    while True:
        current_text = recorder.text()
        print(current_text)
        if any(hot_word in current_text.lower() for hot_word in hot_words) or skip_hot_word_check:
                    #make sure there is text
                    if current_text:
                        print("User: " + current_text)
                        recorder.stop()                        
                        #get time
                        current_text = current_text + " " + time.strftime("%Y-m-%d %H-%M-%S")
                        response = assist.ask_question_memory(current_text)
                        print('Jarvis: ' + response)
                        speech = response.split('#')[0]
                        #done = assist.TTS(speech)
                        assist.speak(speech)
                        #skip_hot_word_check = True if "?" in response else False
                        if len(response.split('#')) > 1:
                            command = response.split('#')[1]
                            #tools.parse_command(command)
                        recorder.start()
 