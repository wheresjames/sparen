
# sparen

Create richer more helpful logs using terminal coloring, file saving,
graph plotting, and ascii drawing.

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
    sparen.log("Hello world!")

    '''
        [21:24:31] demo.py:main(189): Hello world!
    '''

```

``` Python

    #----------------------------------------------------------------
    # Save to log file
    sparen.log.setLogFile("application.log")


    #----------------------------------------------------------------
    # Color output
    #   Note: Color filters are only applied if the output device is a console

    sparen.log.addLogFilters("error:red,warning:yellow,except:red:blink")
    sparen.log("Error: This will be red")
    sparen.log("Warning: This will be yellow")

    try:
        thisisanerror
    except Exception as e:
        sparen.log("Exception: This will be red and flashing\n", e)

    '''
        [21:24:31] demo.py:main(202): Error: This will be red
        [21:24:31] demo.py:main(203): Warning: This will be yellow
        [21:24:31] demo.py:main(208): Exception: This will be red and flashing
         [EXCEPTION] name 'thisisanerror' is not defined
          > demo.py(206)::main() thisisanerror
    '''

    #----------------------------------------------------------------
    # Format interval
    #       $s  - Seconds
    #       $S  - Seconds with leading zero
    #       $m  - Minutes
    #       $M  - Minutes with leading zero
    #       $h  - Hours
    #       $H  - Hours with leading zero
    #       $d  - Days
    #       $D  - Days with leading zero
    #       $y  - Years
    #       $Y  - Years with leading zero
    #       $f  - Decimal
    #       $F  - Decimal with trailing zeros
    #       $+_ - Show full value

    seconds = 1234567

    sparen.log(sparen.formatInterval(seconds, "$+H:$M:$S"))
    '''
        [21:24:31] demo.py:main(65): 342:56:07
    '''

    sparen.log(sparen.formatInterval(seconds, "$d days, $h hours, $m minutes, $s seconds"))
    '''
        [21:24:31] demo.py:main(64): 14 days, 6 hours, 56 minutes, 7 seconds
    '''

    #----------------------------------------------------------------
    # Graph plotting

    data = np.sin(np.linspace(-np.pi * 3, np.pi * 3, 200)) * 10
    sparen.log('PLOT\r\n', sparen.plotArray(data))

    '''
        [21:24:31] demo.py:main(215): PLOT
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
    '''

    #----------------------------------------------------------------
    # Canvas drawing 1

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

    sparen.log("Canvas drawing 1\n", canv)

    '''
        [21:24:31] demo.py:main(330): Canvas drawing 1
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
    '''

    #----------------------------------------------------------------
    # Canvas drawing 2

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

    sparen.log("Canvas drawing 2\n", canv)

    '''
        [21:24:31] demo.py:main(330): Canvas drawing 2

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
    '''

```

&nbsp;


---------------------------------------------------------------------
## References

- Python
    - https://www.python.org/

- pip
    - https://pip.pypa.io/en/stable/

