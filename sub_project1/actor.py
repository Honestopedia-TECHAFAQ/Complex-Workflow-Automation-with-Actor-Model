import pykka

class SubProject1Actor(pykka.ThreadingActor):
    def on_receive(self, message):
        if message["command"] == "perform_task1":
            data = message["data"]
            result = f"SubProject1 processed: {data}"
            return result
