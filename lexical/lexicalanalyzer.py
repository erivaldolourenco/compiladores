# -*- coding: utf-8 -*-

class Lexeme(object):

    def __init__(self, file):
        self.file = file

    def analizer(self):
        with open(self.file) as file:
            filelines = file.readlines()
            print(filelines)
            for line in filelines:
                print("->" + line)