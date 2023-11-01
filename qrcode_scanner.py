import binascii
import string
import sys
import evdev
from sys import stdin
from evdev import InputDevice
from select import select
import logging

logging.basicConfig( level=logging.DEBUG, filename='bc_log.log')

class barcode_scanner():
    def __init__(self):
        #self.__keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
        self.__capital_keys = {
        # Scancode: ASCIICode
        0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
        10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
        20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
        30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
        40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
        50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
        }
        self.__lower_keys = {
        # Scancode: ASCIICode
        0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
        10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'q', 17: u'w', 18: u'e', 19: u'r',
        20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
        30: u'a', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u';',
        40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'z', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n',
        50: u'm', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
        }
        pass

    def readBarcodeScannerInput(self):
        self.__dev = InputDevice('/dev/input/event0')
        self.__line = ""
        print(">> Read from scanner ... ")
        cap = False
        for event in self.__dev.read_loop():
            if event.type == evdev.ecodes.EV_KEY and event.value == 1:
                #DEBUG
                print("key code {}".format(event.code))
                print("key name {}".format(evdev.ecodes.KEY[event.code]))
                #DEBUG
                if evdev.ecodes.KEY[event.code] == "KEY_LEFTSHIFT":                        
                    cap = True
                else:
                    if cap == True:
                        self.__line += (self.__capital_keys[ event.code ])
                        cap = False
                    else:
                        self.__line += (self.__lower_keys[ event.code ])
                if evdev.ecodes.KEY[event.code] == "KEY_ENTER":
                    logging.info("Enter code read")
                    self.__dev.close()
                    break
            else:
                pass

        #Note: [:-n] because of CRLF at the end of self.__line string
        return str(self.__line[:-4])

    def getDataFromScan(self, data):
        data_str=str(data)
        data_list = data_str.split(",")
        return data_list
