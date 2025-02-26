from svWebCra import __init__


class Config:
    def __init__(self):
        self.Driver = __init__()

    def teardown(self):
        self.Driver.quit()

