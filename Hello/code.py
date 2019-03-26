class Hello():
    def __init__(self, obj=None):
        if obj is not None:
            self.word = obj.word
        else:
            self.word = None

    def say_hello(self):
        if self.word is not None:
            return self.word
        return 'Hello World!'
