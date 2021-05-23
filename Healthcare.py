from datetime import datetime as dt
import pygame as pg
import time


def playmusic(name, m, inttim):

    pg.mixer.init()
    pg.mixer.music.load(name+".mp3")
    pg.mixer.music.set_volume(0.7)
    pg.mixer.music.play()

    print("You Should Take atleast 1 min Rest")
    time.sleep(60)
    if name == "water":
        print("NOW ITS TIME FOR WATER !! ")
        k = "Drank"
    elif name == "eyes":
        print("NOW ITS TIME FOR EYES ACTIVITIES !! ")
        k = "Eydone"
    elif name == "physical":
        print("NOW ITS TIME FOR SOME PHYSICAL ACTIVITIES !! ")
        k = "Exdone"

    while True:
        a = input(f"IF DONE TYPE {k} : ")
        if a.lower() == k.lower():
            pg.mixer.music.stop()
            break
    log(name, inttim)


def log(name, inttim):
    name = name.lower()
    dat = dt.now().date()
    tim = dt.now().time()
    #hor = dt.hour.now()
    #min = dt.minute.now()
    fil = open(name+".txt", "a")
    fil.write(f"\n Date :- {dat} -- TIME :- -> {inttim} to ->{tim}")


def timemanage(h, m, z, b):
    a = {"eyes": 30, "water": 50, "physical": 45}

    #print(a , " : a")
    #print(b , " : b ")
    hor = {}
    #print(m ," :  m")
    #acti = len(a.values()) -1
    for i in a:
        if z == 1:
            chktime = a[i]  # finh = h + chktime
            # print(chktime)
            finm = m + chktime
        else:
            chktime = b[i]  # finh = h + chktime
            # print(chktime)
            finm = a[i] + m

        if finm >= 60:
            finh = h + 1
            finm = finm - 60
        else:
            finh = h

        b[i] = finm

        # print(finh)
        if finh in hor:
            hor[finh].append(i)
        else:
            hor[finh] = [i]
    return b, hor


def dicsame(b):
    same = {}
    for i in b.keys():
        # if a[i] in b :
        # print(i)
        if b[i] in same:
            same[b[i]].append(i)
            print(i)
        else:
            same[b[i]] = [i]
            print(i)
        # print(same,":same")
    #print(b , ":b")
   # print(same,":same")
    return same


def optionaltimemage(i, b, hor):
    a = {"eyes": 30, "water": 50, "physical": 45}
    # fixhour dic
    for j in hor:
        if i in hor[j]:
            h = j
            hor[j].remove(i)
           # print(hor)
        if hor[j] == []:
            hor.pop(j)
            # print(hor)
            break

    chktime = b[i]  # finh = h + chktime
    # print(chktime)
    finm = a[i] + chktime
    # finh = hor[] hor setting
    if finm >= 60:
        finh = h + 1
        finm = finm - 60
    else:
        finh = h

    b[i] = finm

   # print(finh)

    """ LAST : set hour list its getting rep."""

    if finh in hor:
        hor[finh].append(i)
    else:
        hor[finh] = [i]

    return b, hor


b = {}
z = 1  # no. of time
h = dt.now().hour
m = dt.now().minute
while True:
    print("NOW hour :", h, " Min : ", m)
    loc = timemanage(h, m, z, b)
    b = loc[0]
    hor = loc[1]
    same = dicsame(b)
    z = z+1

    name = ""
    tlen = len(same)
   # print(tlen)

    while True:

        hnow = dt.now().hour
        mnow = dt.now().minute
        intim = dt.now().time()

        if hnow in hor and mnow in same:

            lent = len(same[mnow])
            # print(lent)
            if lent != 1:
                for i in same[mnow]:
                    # print(i)
                    name = i
                    # print(name)
                    playmusic(name, mnow, intim)
                    loc = optionaltimemage(name, b, hor)
                    b = loc[0]
                    hor = loc[1]
                    same = dicsame(b)
                    print(b, ":b")
                    print(same, ":same")
                    print(hor, ":hor")

            else:
                name = same[mnow][0]
                # print(name)

                playmusic(name, mnow, intim)
                loc = optionaltimemage(name, b, hor)
                b = loc[0]
                hor = loc[1]
                same = dicsame(b)
                print(b, ":b")
                print(same, ":same")
                print(hor, ":hor")
