from handlers.rpi_handler import RPIHandler
from handlers.emul_handler import EmulHandler

# LED selects either emulator mode or RPI mode based on options

class LED:
    def __init__(self, options):
        if options.get('emulator'):
            self.runner = EmulHandler(options)
        else:
            self.runner = RPIHandler(options)
    
    def print(self, msg):
        self.runner.print(msg)

    def run(self, display):
        self.runner.display = display
        self.runner.run()