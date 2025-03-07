#-*- coding:utf-8 _*-

from __future__ import absolute_import

class Logger(object):
    def __init__(self, fpath, title=None, resume=False):
        self.file = None
        self.resume = resume
        self.title = '' if title == None else title
        if fpath is not None:
            if resume:
                self.file = open(fpath, 'r')
                name = self.file.readline()
                self.names = name.rstrip().split('\t')
                self.numbers = {}
                for _, name in enumerate(self.names):
                    self.numbers[name] = []

                for numbers in self.file:
                    numbers = numbers.rstrip().split('\t')
                    for i in range(0, len(numbers)):
                        self.numbers[self.names[i]].append(numbers[i])
                self.file.close()
                self.file = open(fpath, 'a')
            else:
                self.file = open(fpath, 'w')

    def set_names(self, names):
        if self.resume:
            pass
        self.numbers = {}
        self.names = names
        for _, name in enumerate(self.names):
            self.file.write(name)
            self.file.write('\t')
            self.numbers[name] = []
        self.file.write('\n')
        self.file.flush()

    def set_split(self, names):
        if self.resume:
            pass
        self.numbers = {}
        self.names = names
        for _, name in enumerate(self.names):
            self.file.write(name)
            self.numbers[name] = []
        self.file.write('\n')
        self.file.flush()

    def append(self, numbers):
        assert len(self.names) == len(numbers), 'Numbers do not match names'
        for index, num in enumerate(numbers):
            self.file.write("{0:.6f}".format(num))
            self.file.write('\t')
            self.numbers[self.names[index]].append(num)
        self.file.write('\n')
        self.file.flush()

    def close(self):
        if self.file is not None:
            self.file.close()

# if __name__ == '__main__':
#     import numpy as np
#     logger = Logger('test.txt')
#     logger.set_names(['Train loss', 'Valid loss','Test loss'])
#
#     length = 100
#     t = np.arange(length)
#     train_loss = np.exp(-t / 10.0) + np.random.rand(length) * 0.1
#     valid_loss = np.exp(-t / 10.0) + np.random.rand(length) * 0.1
#     test_loss = np.exp(-t / 10.0) + np.random.rand(length) * 0.1
#
#     for i in range(0, length):
#         logger.append([train_loss[i], valid_loss[i], test_loss[i]])
#         logger.set_split(['----------','------------','--------'])

