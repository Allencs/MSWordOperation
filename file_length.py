

class FileLength(object):

    length = 0

    def __init__(self, encoding):
        self.encoding = encoding

    def __call__(self, *args, **kwargs):
        with open(args[0], 'r', encoding=self.encoding) as f:
            for line in f.readlines():
                self.length += len(line)

        return self.length
