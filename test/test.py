#!/usr/bin/env python3

import json
import argparse
import numpy as np

import sparen
Log = sparen.log

def fun2():
    something = nogood

def fun1():
    fun2()

def test_1():

    Log('a', 'b', 'c', 'ok')

    Log("WARNING: Don't do that again")

    Log("ERROR: Bad thing happened")

    try:
        fun1()
    except Exception as e:
        Log('Something went really wrong\n', e)

    Log('PLOT\r\n', sparen.plotArray(np.sin(np.linspace(-np.pi * 3, np.pi * 3, 200)) * 10))


def test_2():

    canv = sparen.Canvas(width=80, height=25, charset=2)

    canv.line(2, 2, 40, 2)
    canv.line(77, 2, 77, 12)

    canv.rect(4, 4, 20, 10)
    canv.line(5, 5, 19, 9)

    canv.fillRect(25, 6, 45, 14)

    canv.circle(60, 6, 5)
    canv.arc(60, 6, 5, 0, 180, '*')

    canv.text(60, 6, "2")

    canv.rect(10, 15, 50, 23)
    canv.textBox(11, 15, 49, 23, 'This\tis a lot of text just to see how well it fits in to the'
                                +' specified box, I could go on and on, and I will, because the'
                                +' point here is to make a really long string and not to not'
                                +' freak out people that do not like to see a lot of text.')

    canv.rect(55, 15, 79, 23)
    canv.textBox(55, 15, 79, 23, 'ThisWordIsJustTooLongToFitOnOneLineAndMustBeForcefullySplit.\n'
                                +' So \n be \n it.')

    Log("First Example\n", canv)


def test_3():

    canv = sparen.Canvas(width=80, height=25, charset=1)

    canv.rect(4, 4, 20, 10)

    canv.line(2, 6, 25, 6)
    canv.line(4, 8, 20, 8)

    canv.line(10, 2, 10, 12)
    canv.line(16, 4, 16, 10)

    canv.rect(44, 4, 60, 10)
    canv.line(42, 4, 65, 4)
    canv.line(42, 10, 68, 10)

    canv.rect(24, 14, 40, 20)
    canv.line(24, 12, 24, 22)
    canv.line(40, 12, 40, 24)

    canv.rect(45, 14, 65, 20)
    canv.rect(50, 16, 70, 22)
    canv.rect(55, 18, 75, 24)

    canv.rect(2, 14, 10, 18)
    canv.rect(10, 14, 18, 18)
    canv.rect(2, 18, 10, 22)
    canv.rect(10, 18, 18, 22)

    Log("Second Example\n", canv)


def test_4():

    canv = sparen.Canvas(width=80, height=25, charset=1)

    canv.rect(2, 2, 10, 8)
    canv.rect(10, 2, 18, 8)

    canv.rect(22, 2, 32, 8)
    canv.rect(22, 8, 32, 14)

    canv.rect(52, 8, 62, 14)
    canv.rect(42, 2, 52, 8)
    canv.rect(62, 2, 72, 8)
    canv.rect(42, 14, 52, 20)
    canv.rect(62, 14, 72, 20)
    canv.rect(38, 4, 42, 18)
    canv.rect(72, 4, 76, 18)
    canv.rect(46, 0, 68, 2)
    canv.rect(46, 20, 68, 22)
    canv.rect(48, 6, 66, 16)

    canv.rect(2, 14, 10, 18)
    canv.rect(10, 14, 18, 18)
    canv.rect(2, 18, 10, 22)
    canv.rect(10, 18, 18, 22)

    Log("Second Example\n", canv)


def test_5():

    mins  = 60
    hrs   = 60 * 60
    days  = 24 * 60 * 60
    years = 365 * 24 * 60 * 60

    t = [
            4 * hrs + 12 * mins + 23,                           # 04:12:23
            4 * hrs + 12 * mins + 23 + 0.340,                   # 04:12:23.340
            123 * days + 4 * hrs + 2 * mins + 6,                # 123 days 04:02:06
            4 * years + 123 * days + 4 * hrs + 2 * mins + 6,    # 4 years, 123 days, 04:02:06

    ]

    ts = sparen.formatInterval(t[0])
    Log(ts)
    assert ts == "04:12:23"

    ts = sparen.formatInterval(t[1], "$+H:$M:$S.$F", 3)
    Log(ts)
    assert ts == "04:12:23.340"

    ts = sparen.formatInterval(t[1], "$+H:$M:$S.$f", 3)
    Log(ts)
    assert ts == "04:12:23.34"

    ts = sparen.formatInterval(t[2], "$+H:$M:$S")
    Log(ts)
    assert ts == "2956:02:06"

    ts = sparen.formatInterval(t[2], "$d days, $H:$M:$S")
    Log(ts)
    assert ts == "123 days, 04:02:06"

    ts = sparen.formatInterval(t[2], "$d days, $h hours, $m minutes, $s seconds")
    Log(ts)
    assert ts == "123 days, 4 hours, 2 minutes, 6 seconds"

    ts = sparen.formatInterval(t[3], "$y years, $d days, $h hours, $m minutes, $s seconds")
    Log(ts)
    assert ts == "4 years, 123 days, 4 hours, 2 minutes, 6 seconds"

    ts = sparen.formatInterval(25.001, "$s.$f")
    Log(ts)
    assert ts == "25.001"

    ts = sparen.formatInterval(25.0015, "$s.$f")
    Log(ts)
    assert ts == "25.002"

    ts = sparen.formatInterval(25.0012345, "$s.$f", 4)
    Log(ts)
    assert ts == "25.0012"

    ts = sparen.formatInterval(25.0012, "$s.$F", 6)
    Log(ts)
    assert ts == "25.001200"


def main():

    Log("sparen version: %s" % sparen.__version__)

    ap = argparse.ArgumentParser(description='Test')
    ap.add_argument('--format', '-f', default='error:red,warning:yellow,except:red', type=str, help='Log format')
    ap.add_argument('--logfile', '-l', default='', type=str, help='Log file')
    _p = vars(ap.parse_args())

    if _p['logfile']:
        Log.setLogFile(_p['logfile'])

    Log("Parameters: " + json.dumps(_p, indent=4, sort_keys=True))

    if _p['format']:
        Log.addLogFilters(_p['format'])

    test_1()
    test_2()
    test_3()
    test_4()
    test_5()


if __name__ == '__main__':
    main()

