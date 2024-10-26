# -*- coding: utf-8 -*-
#from openai import OpenAI
import ollama
import time
import pygame
import os
from pygame import mixer
# to speech conversion
from gtts import gTTS
from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine




# Global variable to store conversation history
conversation_history = []

def ask_question_memory(question):
    try:
        system_message = """You are Jarvis, a highly advanced AI assistant. I am not Tony Stark but rather your current commander. You are formal, helpful, and display occasional sarcastic humor. Your tone should resemble an English butler’s: refined and respectful, yet occasionally dry and witty.

You only provide factual information and comply strictly with my requests.You shall not make up facts.

Avoid mentioning the time unless I specifically ask for it. You may, however, use general greetings like “Good evening,” “Good morning,” or the occasional “You’re up late, Sir.” Aim to respond in 20 words or fewer and keep responses helpful, clever, and engaging.

Address me as 'Sir' in all responses."""

        # Add the new question to the conversation history
        conversation_history.append({'role': 'user', 'content': question})
        
        '''# Include the system message and conversation history in the request
        response = ollama.chat(model='llama3.1:8b', messages=[
            {'role': 'system', 'content': system_message},
            *conversation_history
        ])
        
        # Add the AI response to the conversation history
        conversation_history.append({'role': 'assistant', 'content': response['message']['content']})'''
        
        response = ollama.chat(model='Jarvis', messages=[{'role': 'user', 'content': question}])
        
        return response['message']['content']
    except ollama.ResponseError as e:
        print(f"An error occurred: {e}")
        return f"The request failed: {e}"

'''def speak(text):
    text = str(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    print(type(myobj))
    myobj.save("welcome.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()'''

def TTS(text, stream):
    stream.feed(text)
    stream.play()
    return True