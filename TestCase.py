class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(Self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
