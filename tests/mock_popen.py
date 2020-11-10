class MockedPopen:

    def __init__(self, args, **kwargs):
        self.args = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        pass

    def communicate(self, *args):
        return 'output', 'error'