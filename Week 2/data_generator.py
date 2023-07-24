# Integer Data Generator
# @author: Chayapol Moemeng 
import random
import csv
import sys

def dataGenerator(dataSize,outputfile):
    with open(outputfile, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile,delimiter=",")
        data = []
        for x in range(0,dataSize):
            data.append(random.randint(0,dataSize))
        wr.writerow(data)

if __name__ == "__main__":
    try:
        dataGenerator(int(sys.argv[1]),sys.argv[2])
    except (IndexError, ValueError):
        print('usage: %s <data size> [outputfile]' % sys.argv[0])
