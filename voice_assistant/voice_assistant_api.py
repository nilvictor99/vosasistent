import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import speech_to_text_wav2vec2 as stt_w2v2
from microservices import *

# Load model of speech to text
model, processor = stt_w2v2.load_model()

# Deploying FastAPI
app = FastAPI()

class Audio(BaseModel):
    audio_path: str

@app.get('/foxie/')
async def foxie(audio_path: Audio):
    
    """ > Loading audio """
    if os.path.exists('audios_foxie/'):
        path = 'audios_foxie/'
        print(path)
    else:
        print('else')
        path = '../bot/audios_telegram/'
        print(path)
    
    # Getting audio name
    audio_name = audio_path.audio_path
    
    # Getting audio full path
    audio_path = os.path.join(path, audio_name)

    # Audio to array conversion
    audio_array = stt_w2v2.audio_to_array(audio_path)

    """ > Speech to text """
    predicted_sentence = stt_w2v2.inference_model(model, processor, audio_array)
    prediction = predicted_sentence[0]

    """ > Request to microservices via Keyword in prediction """
    understand = 0

    ### Temperature microservice
    if 'temperatura' in prediction:
        response = temperatura()
        understand = 1
    
    if understand == 0:
        response = "🤷🏻‍♂️Lo siento, no entiendo tu mensaje."
  
    output = jsonable_encoder({'response':response})
    return JSONResponse(output)
    
