from files import sourceFilePath


class FileLength(object):

    length = 0

    def __call__(self, *args, **kwargs):
        with open(args[0], 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self.length += len(line)

        return self.length
