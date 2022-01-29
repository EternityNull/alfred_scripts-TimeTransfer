#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Alfred:
    def __init__(self):
        self.title = str()
        self.subtitle = str()
        self.arg = str()
    
    def __init__(self, title, subtitle, arg):
        self.title = title
        self.subtitle = subtitle
        self.arg = arg
        


if __name__ == '__main__':
    # alfred = Alfred()
    # alfred.title = '111'
    # alfred.subtitle = '222'
    # alfred.arg = '333'

    # print(alfred.__dict__)


    alfred = Alfred('111', '222', 'aaaa')
    print(alfred.__dict__)