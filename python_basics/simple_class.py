# define log class
class InfoLog:
    def __init__(self, msg):
        self.message = msg

    def print_message(self):
        print(f"INFO | {self.message}")

# create an object of the InfoLog clas,
# initialize with simple message

log = InfoLog("This is an info message")

log.print_message()
