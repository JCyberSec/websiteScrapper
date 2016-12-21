#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randrange
import requests
import random
from time import gmtime, strftime, sleep


def createHeader():
    browser = [
        'Mozilla/5.0',
        'Mozilla/4.5',
        'Mozilla/4.0',
        'Chrome/41.0.2228.0',
        'Chrome/41.0.2234.0',
        'Chrome/42.4.2228.3',
        'Opera/9.80',
        'Opera/10.80',
        'Safari/537.36',
        'Android 4.5.00.5',
        ]
    os = [
        '(Windows NT 6.1)',
        'Windows 7/8/10',
        '(Windows 7)',
        'Windows NT 4.1',
        '(Windows 10)',
        'Linux 6.1',
        '(Linux 16.1.3)',
        'OSX',
        'WOW64',
        'Trident/6.0',
        'MSIE 8.0; Windowns NT 5.1; Trident/4.0; ',
        'Windows 7/Windows 8.1; Windowns NT 6.2; Gecko/5.6; ',
        '.NET CLR 3.0.30729',
        ]
    junk = [
        'Firefox/20.0',
        'Chrome/33.04.32',
        'Firefox/19.9',
        'Opera/10.8',
        'Gecko/20100101',
        'KHTML, like Gecko',
        'Safari/537.36',
        'AppleWebKit/537.36',
        'Google App-engine',
        '.NET CLR 3.0.30729',
        ]
    idd = [
        'Simons',
        'computer3',
        'Marks',
        'WIN-7-PRO',
        'Julie',
        'VM',
        'Bobs machine',
        'pop-PC',
        'Klone-pc',
        'x86Win',
        'testing',
        'username',
        'Jim',
        ]
    uid = [
        'Newcomputer',
        'pop',
        'uop',
        'vm',
        'Cats',
        'PepperSpray',
        'Henry',
        'Mths22',
        'admin',
        'VM_2',
        'ABC',
        '12345',
        'Wilbert',
        ]
    random_index = randrange(0, len(browser))
    a = browser[random_index]
    random_index = randrange(0, len(os))
    b = os[random_index]
    random_index = randrange(0, len(junk))
    c = junk[random_index]
    random_index = randrange(0, len(idd))
    d = idd[random_index]
    random_index = randrange(0, len(uid))
    e = uid[random_index]

    finalHeader = {'User-Agent': a + ' ' + b + ' ' + c + ' id = ' + d \
                   + ' | uid = ' + e + ' | '}
    return finalHeader


def getData():
    headers = createHeader()
    webp = requests.get('http://google.com'
                        , headers=headers).text
    stringHash = str(webp)
    return stringHash


def writeText(textToWrite):
    currTime = str(strftime('%Y-%m-%d %H:%M:%S', gmtime()))
    finalText = textToWrite + '    |    ' + currTime
    with open('hashCodeOut.txt', 'a') as f:
        f.write(finalText)
        f.write('\n')


def sched():
    currTime = int(strftime('%H%M', gmtime()))
    if 1200 <= currTime <= 2359:
        return True
    else:
        return False


def main():
    while True:
        if sched():
            newData = getData()
            writeText(newData)
            sleep(43200)
        else:
            sleep(15)


if __name__ == '__main__':
    main()


			
