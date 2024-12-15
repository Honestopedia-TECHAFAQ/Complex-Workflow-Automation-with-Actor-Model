import pykka
import requests

from sub_project1.actor import SubProject1Actor
from sub_project2.actor import SubProject2Actor

class MasterProjectActor(pykka.ThreadingActor):
    def __init__(self):
        super().__init__()
        self.sub_project1 = SubProject1Actor.start()
        self.sub_project2 = SubProject2Actor.start()

    def on_receive(self, message):
        if message["command"] == "orchestrate_workflow":
            data = message["data"]
            step1_result = self.sub_project1.ask({"command": "perform_task1", "data": data})
            step2_result = self.sub_project2.ask({"command": "perform_task2", "data": step1_result})
            return {"result": f"Workflow result: {step2_result}"}

def main():
    master_actor = MasterProjectActor.start()
    input_data = "Initial data"
    result = master_actor.ask({"command": "orchestrate_workflow", "data": input_data})
    print(result)
    pykka.ActorRegistry.stop_all()

if __name__ == "__main__":
    main()
