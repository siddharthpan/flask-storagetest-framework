import pymysql

mydb = pymysql.connect(host="192.168.1.166", user="rpi3", passwd='', db="test")
cursor = mydb.cursor()

def numoftests():
    testnosql1 = "SELECT count(*) FROM log1"
    cursor.execute(testnosql1)
    resultnum1 = cursor.fetchall()
    for row in resultnum1:
        num1 = row[0]

    testnosql2 = "SELECT count(*) FROM log2"
    cursor.execute((testnosql2))
    resultnum2 = cursor.fetchall()
    for row in resultnum2:
        num2 = row[0]

    testnototal = num1 + num2
    # print("Number of tests run on SDCard is : "+ str(num1))
    # print("Number of tests run on HP Flash Drive is : " + str(num2))
    # print ("Total number of tests run is : "+ str(testnototal))

    return num1, num2, testnototal

def avgspeed():
    testnosql1 = "SELECT count(*) FROM log1"
    cursor.execute(testnosql1)
    resultnum1 = cursor.fetchall()
    for row in resultnum1:
        num1 = row[0]

    testnosql2 = "SELECT count(*) FROM log2"
    cursor.execute((testnosql2))
    resultnum2 = cursor.fetchall()
    for row in resultnum2:
        num2 = row[0]

    fetchrdspd1 = "SELECT read_speed from log1"
    fetchwrspd1 = "SELECT write_speed from log1"

    cursor.execute(fetchrdspd1)
    resultrd1 = cursor.fetchall()
    rdspd1 = 0
    for row in resultrd1:
        rdspdlst1 = row[0]
        rdspd1 += rdspdlst1
    avgrdspd1 = (rdspd1/num1)
    avgrdspd1 = ("%.2f" %avgrdspd1)
    # print ("Total read speed of SDCard : " + str(rdspd1))
    # print ("Average read speed of SDCard :" +str(avgrdspd1) +" Mbps")

    cursor.execute(fetchwrspd1)
    resultwr1 = cursor.fetchall()
    wrspd1 = 0
    for row in resultwr1:
        wrspdlst1 = row[0]
        wrspd1 += wrspdlst1
    avgwrspd1 = (wrspd1 / num2)
    avgwrspd1 = ("%.2f" % avgwrspd1)
    # print ("Total read speed of SDCard : " + str(rdspd1))
    # print("Average write speed of SDCard :" + str(avgwrspd1) + " Mbps")

    testnosql2 = "SELECT count(*) FROM log2"
    cursor.execute(testnosql2)
    resultnum2 = cursor.fetchall()
    for row in resultnum2:
        num3 = row[0]

    testnosql2 = "SELECT count(*) FROM log2"
    cursor.execute((testnosql2))
    resultnum2 = cursor.fetchall()
    for row in resultnum2:
        num4 = row[0]

    fetchrdspd2 = "SELECT read_speed from log2"
    fetchwrspd2 = "SELECT write_speed from log2"

    cursor.execute(fetchrdspd2)
    resultrd2 = cursor.fetchall()
    rdspd2 = 0
    for row in resultrd2:
        rdspdlst2 = row[0]
        rdspd2 += rdspdlst2
    avgrdspd2 = (rdspd2 / num3)
    avgrdspd2 = ("%.2f" % avgrdspd2)
    # print ("Total read speed of SDCard : " + str(rdspd1))
    # print("Average  speed of HP Flash Drive :" + str(avgrdspd2) + " Mbps")

    cursor.execute(fetchwrspd2)
    resultwr2 = cursor.fetchall()
    wrspd2 = 0
    for row in resultwr2:
        wrspdlst2 = row[0]
        wrspd2 += wrspdlst2
    avgwrspd2 = (wrspd2 / num4)
    avgwrspd2 = ("%.2f" % avgwrspd2)
    # print ("Total read speed of SDCard : " + str(rdspd1))
    # print("Average write speed of HP Flash Drive :" + str(avgwrspd2) + " Mbps")
    return avgrdspd1, avgwrspd1, avgrdspd2, avgwrspd2
