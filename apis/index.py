from fastapi import Depends, FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import os
import pyttsx3
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/voiceResponse', tags=['Voice_response'], status_code=status.HTTP_201_CREATED, response_model=schemas.Output,
          responses={
    status.HTTP_400_BAD_REQUEST: {"model":  schemas.Responses},
    status.HTTP_422_UNPROCESSABLE_ENTITY: {"model":  schemas.Responses},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model":  schemas.Responses}})
def create(request: schemas.InputField, db: Session = Depends(get_db)):
    new_category = models.InputField(
        enterText=request.enterText)
    # print(new_category.enterText)
    try:
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume',1.0)  
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(new_category.enterText)
        engine.save_to_file(new_category.enterText, 'test.mp3')
        engine.runAndWait()
        engine.stop()
# upwork link(https://www.upwork.com/freelancers/~01c5ef601175f0bdbc)
# https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-windows.html
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(new_category))
    except Exception:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder(schemas.Responses))




















# # Import the required module for text 
# # to speech conversion
# from gtts import gTTS
 
# # This module is imported so that we can 
# # play the converted audio
# import os
 
# # The text that you want to convert to audio
# mytext = 'Welcome to geeksforgeeks!'
 
# # Language in which you want to convert
# language = 'en'
 
# # Passing the text and language to the engine, 
# # here we have marked slow=False. Which tells 
# # the module that the converted audio should 
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
 
# # Saving the converted audio in a mp3 file named
# # welcome 
# myobj.save("welcome.mp3")
 
# # Playing the converted file
# os.system("mpg321 welcome.mp3")


