from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

from domain.value_objects.simulation_configuration import SimulationConfiguration
from infrastructure.factories.ai_factory import AiFactory
from root.factories.controllers.interview_simulation_controller_factory import make_interview_simulation_controller

load_dotenv()

app = FastAPI()
class InitiateInterviewRquest(BaseModel):
    simulation_configuration: SimulationConfiguration
    prompt: str
    
@app.post("/initiate_interview")
def initiate_interview(req: InitiateInterviewRquest):
    ai_provider = AiFactory.create(req.simulation_configuration.primary_model)
    interview_simulation_controller = make_interview_simulation_controller(ai_provider)
    response = interview_simulation_controller.handle_initiate_interview(req.prompt)
    return {
      "response": response
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)