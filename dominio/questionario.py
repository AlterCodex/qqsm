import uuid as uuid


class Questionario():

    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self.preguntas =[]

    def add(self, p):
        self.preguntas.append(p)




