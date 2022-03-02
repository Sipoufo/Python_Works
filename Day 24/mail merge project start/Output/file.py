class File:
    def __init__(self, path):
        self.namePath = path

    def readFileList(self):
        with open(self.namePath) as file:
            return file.readlines()

    def readFile(self):
        with open(self.namePath) as file:
            return file.read()

    def writeFile(self, text):
        with open(self.namePath, 'w') as file:
            file.write(text)