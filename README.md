pycaption-cli-wmx
=============

This is a fork of [pycaption-cli](https://github.com/jnorton001/pycaption-cli) a command line interface for the `pycaption` module.

Setup
=====

    python setup.py install

This installation has dependency of [pycaption-mwx](https://github.com/mwx-limited/pycaption-mwx) (modified version of [pycaption](https://github.com/pbs/pycaption)) which will be installed automatically as long as other `pycaption` dependencies

Usage
=====

From your command line:

    pycaption <path to caption file> [--sami --dfxp --srt --vtt --use_styling --transcript --lang --time_offset]
    
e.g.

    pycaption ../captions.scc --dfxp --transcript

Output is written to the screen. To write to a file, use something like this:

    pycaption ../captions.scc --vtt --use_styling=no > captions.vtt

Arguments
=========

 - --use_styling - use webvtt caption positioning styling or not (True/yes by default)
 - --time_offset - offset time in seconds. Positive value will be added to the time stamp, negative - subtracted. Supported for SCC and SRT input files only.

Supported Formats
=================

 - SCC (read)
 - SRT (read/write)
 - [SAMI](https://en.wikipedia.org/wiki/SAMI) (read/write)
 - [DFXP](https://www.w3.org/TR/ttaf1-dfxp/) (read/write)
 - [WebVTT](https://w3c.github.io/webvtt/)(.vtt) (read/write)
 - Transcript (write)

Documentation
=============
Documentation for original `pycaption`: http://pycaption.readthedocs.io
 
License
=======

Copyright 2016 MWX Limited derived from [pycaption-cli](https://github.com/jnorton001/pycaption-cli)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at [Apache License, Version 2.0][1].

[1]: http://www.apache.org/licenses/LICENSE-2.0
