
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
## Install

    $ pip3 install sparen

&nbsp;


---------------------------------------------------------------------
## Examples

``` Python

    #----------------------------------------------------------------
    # The simple

    import sparen
    sparen.Log("Hello world!")

```

``` Python

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

``` Python

    #----------------------------------------------------------------
    # Canvas drawing example

    import sparen
    Log = sparen.Log

    def main():

        # First example
        canv = sparen.Canvas(width=80, height=25, charset=0)

        canv.line(2, 2, 40, 2, '.')
        canv.line(77, 2, 77, 12, '.')

        canv.rect(4, 4, 20, 10, '.')
        canv.line(4, 4, 20, 10, '.')

        canv.fillRect(25, 6, 45, 14, '.')

        canv.circle(60, 6, 5, '.')
        canv.arc(60, 6, 5, 0, 180, '*')

        canv.text(60, 6, "2")

        canv.rect(10, 15, 50, 23, '.')
        canv.textBox(11, 15, 49, 23, 'This is a lot of text just to see how well it fits in to the'
                                    +' specified box, I could go on and on, and I will, because the'
                                    +' point here is to make a really long string and not to not'
                                    +' freak out people that do not like to see a lot of text.')

        canv.rect(55, 15, 79, 23, '.')
        canv.textBox(55, 15, 79, 23, 'ThisWordIsJustTooLongToFitOnOneLineAndMustBeForcefullySplit.\n'
                                    +' So \n be \n it.')

        Log("First Example\n", canv)


        # Second example
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

        Log("Second Example\n", canv)


    if __name__ == '__main__':
        main()

```

Output

```
[21:48:26] test.py:test_2(59): First Example
                                                            .
  ......................................               ... . . ...           .
                                                     .             .         .
    .................                               .               .        .
    .  ...          .                              .                 .       .
    .     ...       .    ....................     .*        2        **      .
    .        ..     .    ....................      *                 *       .
    .          ...  .    ....................       *               *        .
    .             ...    ....................        *             *         .
    .................    ....................          *** * * ***           .
                         ....................               *                .
                         ....................
                         ....................

          .........................................    .........................
          . This is a lot of text just to see how .    .ThisWordIsJustTooLongTo.
          . well it fits in to the specified box, .    .FitOnOneLineAndMustBeFo.
          .   I could go on and on, and I will,   .    .    rcefullySplit.     .
          .  because the point here is to make a  .    .          So           .
          .   really long string and not to not   .    .          be           .
          . freak out people that do not like to  .    .          it.          .
          .          see a lot of text.           .    .                       .
          .........................................    .........................


[21:48:26] test.py:test_2(59): First Example (character set 2)
                                                            ·
  ═══════════════════════════════════════              ··· · · ···           ║
                                                     ·             ·         ║
    ╔═══════════════╗                               ·               ·        ║
    ║····           ║                              ·                 ·       ║
    ║    ····       ║    ████████████████████     ·*        2        **      ║
    ║        ···    ║    ████████████████████      *                 *       ║
    ║           ····║    ████████████████████       *               *        ║
    ║              ·║    ████████████████████        *             *         ║
    ╚═══════════════╝    ████████████████████          *** * * ***           ║
                         ████████████████████               *                ║
                         ████████████████████                                ║
                         ████████████████████

          ╔═══════════════════════════════════════╗    ╔═══════════════════════╗
          ║ This is a lot of text just to see how ║    ║ThisWordIsJustTooLongTo║
          ║ well it fits in to the specified box, ║    ║FitOnOneLineAndMustBeFo║
          ║   I could go on and on, and I will,   ║    ║    rcefullySplit.     ║
          ║  because the point here is to make a  ║    ║          So           ║
          ║   really long string and not to not   ║    ║          be           ║
          ║ freak out people that do not like to  ║    ║          it.          ║
          ║          see a lot of text.           ║    ║                       ║
          ╚═══════════════════════════════════════╝    ╚═══════════════════════╝


[21:48:26] test.py:test_3(86): Second Example

          │
          │
    ┌─────┼─────┬───┐                     ──┬───────────────┬─────
    │     │     │   │                       │               │
  ──┼─────┼─────┼───┼─────                  │               │
    │     │     │   │                       │               │
    ├─────┼─────┼───┤                       │               │
    │     │     │   │                       │               │
    └─────┼─────┴───┘                     ──┴───────────────┴────────
          │
          │             │               │
                        │               │
  ┌───────┬───────┐     ├───────────────┤    ┌───────────────────┐
  │       │       │     │               │    │                   │
  │       │       │     │               │    │    ┌──────────────┼────┐
  │       │       │     │               │    │    │              │    │
  ├───────┼───────┤     │               │    │    │    ┌─────────┼────┼────┐
  │       │       │     │               │    │    │    │         │    │    │
  │       │       │     ├───────────────┤    └────┼────┼─────────┘    │    │
  │       │       │     │               │         │    │              │    │
  └───────┴───────┘     │               │         └────┼──────────────┘    │
                                        │              │                   │
                                        │              └───────────────────┘

```

&nbsp;


---------------------------------------------------------------------
## References

- Python
    - https://www.python.org/

- pip
    - https://pip.pypa.io/en/stable/

