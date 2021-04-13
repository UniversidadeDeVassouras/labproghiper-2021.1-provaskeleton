class Video:

    __id: int
    __titulo: str
    __filename: str

    def __init__(self, id, titulo, filename):
        self.__id = id
        self.__titulo = titulo
        if filename is None:
            self.__filename = 'img/default.jpg'
        else: 
            self.__filename = 'img/' + filename

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_filename(self):
        return self.__filename

