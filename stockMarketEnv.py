import csv
from time import sleep


class stockMarketSimulations:
    csvfile = None
    currentClose = 0
    currentOpen = 0
    currentLow = 0
    currentHigh = 0
    def __init__(self, csvfile):
        self.csvfile = csvfile

    def start(self):
        with open(self.csvfile, mode ='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)
            for row in csv_reader:
                self.currentOpen = float(row[1])
                self.currentHigh = float(row[2])
                self.currentLow  = float(row[3])
                self.currentClose = float(row[4])
                self.currentVolume = float(row[5])
                sleep(.5)

    def getClose(self):
        if self.currentClose !=0:
            return self.currentClose
        else:
            return None

    def getOpen(self):
        if self.currentOpen != 0:
            return self.currentClose
        else:
            return None

    def getHigh(self):
        if self.currentHigh != 0:
            return self.currentHigh
        else:
            return None

    def getLow(self):
        if self.currentLow != 0:
            return self.currentLow
        else:
            return None

    def getVolume(self):
        if self.currentLow != 0:
            return self.currentVolume
        else:
            return None



