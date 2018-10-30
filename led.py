from handlers.rpi_handler import RPIHandler
from handlers.emul_handler import EmulHandler
from time import sleep

# LED selects either emulator mode or RPI mode based on options

class LED:
    def __init__(self, options):
        if options.get('emulator'):
            self.runner = EmulHandler(options)
        else:
            self.runner = RPIHandler(options)
    
    def clear(self):
        self.runner.flush()

    def run(self):
        while(True):
            self.runner.options['reset'] = False
            self.runner.run()
            sleep(0.5)