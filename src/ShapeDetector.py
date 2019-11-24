import clips

class ShapeDetector():
    def __init__(self,file):
        self._clips = clips.Environment()
        self._clips.load(file)

    def _add_facts(self,facts):
        for fact in facts:
            self._clips.assert_string(fact)

    def _run(self):
        self._clips.run()

    def _detect(self,shape):
        self._clips.run()

        isBentukSama = False

        for fact in self._clips.facts():
            if (str(fact) == shape):
                isBentukSama = True
        
        return isBentukSama

    def _get_facts(self):
        return self._clips.facts()