class GroupLimitError(Exception):
    def __init__(self, message='В групi не може бути бiльше 10 студентiв!'):
        self.message = message
        super().__init__(self.message)