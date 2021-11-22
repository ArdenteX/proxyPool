class ReWriteSpiderError(Exception):
    def __init__(self, name):
        self.name = name
        Exception.__init__(self)

    def __str__(self):
        return repr(f"this class {self.name} does not has 'gets' method")

