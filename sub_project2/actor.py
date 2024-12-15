import pykka

class SubProject2Actor(pykka.ThreadingActor):
    def on_receive(self, message):
        if message["command"] == "perform_task2":
            data = message["data"]
            result = f"SubProject2 processed: {data}"
            return result
