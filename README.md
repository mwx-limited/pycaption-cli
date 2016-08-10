pycaption-cli
=============

A command line interface for the pycaption module.

Setup
=====

    python setup.py install

Usage
=====

From your command line:

    pycaption <path to caption file> [--sami --dfxp --srt --vtt --use_styling --transcript --scc_lang --scc_offset]
    
e.g.

    pycaption ../jnorton-caption.scc --dfxp --transcript

Output is written to the screen. To write to a file, use something like this:

    pycaption ../jnorton-caption.scc --dfxp > jnorton.xml

Arguments
=========

 - --use_styling - use webvtt caption positioning styling or not (True by default)
 - --scc_offset - offset for SCC file in seconds. Positive value will be subtracted from the time stamp, negative - added

Supported Formats
=================

 - SCC (read)
 - SRT (read/write)
 - SAMI (read/write)
 - DFXP (read/write)
 - Transcript (write)
 
License
=======

This module is Copyright 2012 Joe Norton and is available under the [Apache License, Version 2.0][1].

[1]: http://www.apache.org/licenses/LICENSE-2.0
