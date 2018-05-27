#!/usr/bin/env python

import time, os, sys
import csv
import pymysql
import string
import random

def string_generator(size=50, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def writetofile(filename,mysizeMB):
    # writes string to specified file repeatedly, until mysizeMB is reached. Then deletes fle
    mystring = string_generator()
    writeloops = int(1000000*mysizeMB/len(mystring))
    try:
        f = open(filename, 'w')
    except:
        # no better idea than:
        raise
    for x in range(0, writeloops):
        f.write(mystring)
    f.close()

############## 

def diskspeedmeasure(dirname):
    # returns writing speed to dirname in MB/s
    # method: keep writing a file, until 0.5 seconds is passed. Then divide bytes written by time passed
    filesize = 1	# in MB
    maxtime = 0.5 	# in sec
    filename = os.path.join(dirname,'outputTESTING.txt')
    start = time.time()
    loopcounter = 0
    while True:
        try:
            writetofile(filename, filesize)
        except:
            # I have no better idea than:
            raise
        loopcounter += 1
        diff = time.time() - start
        if diff > maxtime: break
    wspeed = (loopcounter*filesize)/diff
    start = time.time()
    loopcounter1=0
    while True:
        try:
            f=open(filename,'r')
            f.read()
        except:
            raise
        loopcounter1 +=1
        diff = time.time() - start
        if diff > maxtime: break
    rspeed= ((loopcounter1*filesize)/diff)/10
    f.close()
    os.remove(filename)
    return wspeed,rspeed

# Start of main



def main():
    # baseURL = 'https://api.thingspeak.com/update?api_key=7GS3YNIKYFTVJKWT'
    print(str(sys.argv))
    tgt = sys.argv[1]

    print(tgt)

    if len(sys.argv) >= 3:
        dirname = sys.argv[1]
        if not os.path.isdir(dirname):
            print ("Specified argument is not a directory. Bailing out \n")
            sys.exit(1)
    else:
        # no argument, so use current working directory
        dirname = os.getcwd()
        print ("Measuring Disk Speed now \n")
        print ("Using current working directory \n")

    try:
        (wspeed, rspeed) = diskspeedmeasure(dirname)
        print("Read speed is " + str(rspeed))
        print("Write speed is " + str(wspeed))
        # print("Disk writing speed: %.2f Mbytes per second" % speed)
    except IOError as e:
        # print "IOError:", e
        if e.errno == 13:
            print ("Could not create test file. Check that you have write rights to directory \n", dirname)
    except:
        print ("Something else went wrong \n")
        raise

    file1 = open("csv1.csv", "w")
    file1.truncate()
    file1.close()
    file1 = open("csv1.csv", "a")
    csvWriter = csv.writer(file1, lineterminator= '\t')
    csvWriter.writerow([rspeed])
    csvWriter.writerow([wspeed])
    file1.close()


    print ("Moving data from into DB \n")


    mydb = pymysql.connect(host="192.168.1.166", user = "rpi3", passwd='', db= "test")
    cursor = mydb.cursor()

    if tgt == 'sdcard':
        print('SDCARD selected')
        cursor.execute("INSERT into log1(read_speed, write_speed) values (%s, %s)" %(rspeed, wspeed))
        mydb.commit()
    elif tgt == 'pendrive':
        print('PENDRIVE selected')
        cursor.execute("INSERT into log2(read_speed, write_speed) values (%s, %s)" % (rspeed, wspeed))
        mydb.commit()
    elif tgt == 'android':
        print('Android Smartphone selected')
        cursor.execute("INSERT into log3(read_speed, write_speed) values (%s, %s)" % (rspeed, wspeed))
        mydb.commit()
        cursor.close()

    # f1 = urlopen(baseURL +
    #                         "&field1=%s&field2=%s" % (wspeed, rspeed))
    print ("Done \n")

    return tgt

if __name__ == '__main__':
    main()