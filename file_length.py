

class FileLength(object):

    length = 0

    fileEncoding = ""

    def __call__(self, *args, **kwargs):
        try:
            with open(args[0], 'r', encoding=FileEncoding.UTF_8) as f:
                for line in f.readlines():
                    self.length += len(line)
            self.fileEncoding = FileEncoding.UTF_8
        except UnicodeDecodeError:
            self.length = 0
            with open(args[0], 'r', encoding=FileEncoding.GB18030) as f:
                for line in f.readlines():
                    self.length += len(line)
            self.fileEncoding = FileEncoding.GB18030
        print("--- 当前文件编码: [%s] ---" % self.fileEncoding)

        return self.length


class FileEncoding(object):
    UTF_8 = "utf-8"
    GB18030 = "gb18030"
