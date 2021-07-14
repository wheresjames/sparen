
# sparen

Simple logging library supporting terminal coloring, file saving,
and graph plot output.

---------------------------------------------------------------------
## Table of contents

* [Install](#install)
* [Examples](#examples)
* [References](#references)

&nbsp;

---------------------------------------------------------------------
## Examples

    $ pip3 install .

&nbsp;


---------------------------------------------------------------------
## Examples

``` Python


    #----------------------------------------------------------------
    # The simple

    import sparen
    sparen.Log("Hello world!")


    #----------------------------------------------------------------
    # More options

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

```

Output

```
    [21:10:12] test.py:main(18): sparen version: 0.1.1

    [21:10:12] test.py:main(19): ['Log', 'Logging', '__author__', '__builtins__', '__cached__', '__company__', '__description__', '__doc__', '__email__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__url__', '__version__', 'datetime', 'functools', 'getframeinfo', 'inspect', 'loadConfig', 'os', 'plotArray', 'print_function', 'sparen', 'stack', 'sys', 'time', 'traceback']

    [21:10:12] test.py:main(29): Parameters: {
        "format": "error:red,warning:yellow,except:red",
        "logfile": ""
    }

    [21:10:12] test.py:main(34): a b c ok

    [21:10:12] test.py:main(36): WARNING: Don't do that again

    [21:10:12] test.py:main(38): ERROR: Bad thing happened

    [21:10:12] test.py:main(43): Something went really wrong
    [EXCEPTION] name 'nogood' is not defined
     > test.py(11)::fun2() something = nogood
     > test.py(14)::fun1() fun2()
     > test.py(41)::main() fun1()

    [21:10:12] test.py:main(45): PLOT
     10 :                 ...                    ....                   ....
      9 :               ..   .                  .   ..                 ..  ..
      7 :               .     ..               .     ..               .     ..
      5 :              .       .              .       .              .       ..
      3 :             .         .            ..        .            ..        .
      1 :            ..         ..           .         ..           .          .
      0 : .          .           .          .           .          .
     -2 : ..        .             .        .             .        ..
     -4 :  ..      ..             ..      ..             ..       .
     -6 :   .     ..               ..    ..               ..     .
     -8 :    ..  ..                 ..  ..                 ..  ..
    -10 :     ....                   ....                   ....
        ------------------------------------------------------------------------
                10^       20^       30^       40^       50^       60^       70^

```

&nbsp;


---------------------------------------------------------------------
## References

- Python
    - https://www.python.org/

- pip
    - https://pip.pypa.io/en/stable/

