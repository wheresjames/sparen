#!/usr/bin/env python3

import json
import argparse
import numpy as np

import sparen
Log = sparen.Log

def fun2():
    something = nogood

def fun1():
    fun2()

def main():

    Log("sparen version: %s" % sparen.__version__)
    Log(dir(sparen))

    ap = argparse.ArgumentParser(description='Test')
    ap.add_argument('--format', '-f', default='error:red,warning:yellow,except:red', type=str, help='Log format')
    ap.add_argument('--logfile', '-l', default='', type=str, help='Log file')
    _p = vars(ap.parse_args())

    if _p['logfile']:
        Log.setLogFile(_p['logfile'])

    Log("Parameters: " + json.dumps(_p, indent=4, sort_keys=True))

    if _p['format']:
        Log.addLogFilters(_p['format'])

    Log('a', 'b', 'c', 'ok')

    Log("WARNING: Don't do that again")

    Log("ERROR: Bad thing happened")

    try:
        fun1()
    except Exception as e:
        Log('Something went really wrong\n', e)

    Log('PLOT\r\n', sparen.plotArray(np.sin(np.linspace(-np.pi * 3, np.pi * 3, 200)) * 10))

if __name__ == '__main__':
    main()

