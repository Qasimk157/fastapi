
from pydantic import BaseModel

class Responses(BaseModel):

    status: bool
    message: str
    
class InputField(BaseModel):
    enterText: str
        
class Output(BaseModel):
    id: str
    InputField: str

