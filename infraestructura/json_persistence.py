import jsonpickle as jsonpickle


class jsonPersistence():

    @classmethod
    def save_json(cls, questionario):
        text_open = open("files/" + str(questionario.uuid) + '.json', mode='w')
        json_file = jsonpickle.encode(questionario)
        text_open.write(json_file)
        text_open.close()


    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_file = text_open.readline()
        questionario = jsonpickle.decode(json_file)
        text_open.close()
        return questionario