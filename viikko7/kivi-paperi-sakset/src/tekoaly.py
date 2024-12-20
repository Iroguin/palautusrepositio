from tekoaly_interface import TekoalyInterface

class Tekoaly(TekoalyInterface):
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        self._siirto = (self._siirto + 1) % 3

        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        return "s"

    def aseta_siirto(self, siirto):
        pass
