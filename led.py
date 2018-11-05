from handlers.rpi_handler import RPIHandler
from handlers.emul_handler import EmulHandler
from time import sleep, localtime, strftime

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
            if(self.runner.options.get('time')):
                message = strftime("%-I:%M%p %b %d", localtime())
                self.runner.options['message'] = message
            self.runner.options['reset'] = False
            self.runner.run()