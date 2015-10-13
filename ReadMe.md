% Encoding
# Version 1.2  
# October 12, 2015

Copyright 2010 - 2015 by Jamal Mazrui  
GNU Lesser General Public License (LGPL)  
----------
# Contents

-   [Description](#A1)
-   [Installation](#A2)
-   [Operation](#A3)
-   [Development Notes](#A4)

# Description

Encoding is a free, open source, command-line utility for
performing encoding-related operations on files. It can show the
encoding of files, and convert between different encodings. Batch
operations are supported if wildcard characters are used in the
file specification. The executable, Encoding.exe, should run on any
version of Windows. The source code, Encoding.py, should run on
other platforms as well.

An encoding is an agreement about how to represent textual
characters with computer bytes. Characters are encoded as byte
sequences that may be stored in disk files or computer memory. A
byte stream is decoded to produce characters in a human language.
If a text file is not readable, the reason may be that it has an
encoding that was either not recognized or not decoded properly.
This utility may help with such issues, benefiting software
developers or end users. It works with over a hundred character
encodings.

# Installation

Unarchive Encoding.zip into a directory, e.g., into  
C:\\Encoding

Run Encoding.exe at a command prompt, e.g., one created by
entering  
cmd.exe

at the Windows Start/Run prompt.

Since Encoding is developed in a cross-platform language, Python,
it should also be possible to run the source code, Encoding.py, on
other platforms that have a Python interpreter.

# Operation

The complete command-line syntax of Encoding is as follows:

Encoding.exe TaskName FileSpec SourceEncoding TargetEncoding

Some parameters are optional or not applicable depending on the
name of the task. Typing the .exe extension is optional.
Capitalization does not matter in task or encoding names . The
following tasks are supported, illustrated with example parameter
values:

encoding help

provides a help summary. The help parameter is assumed if no other
valid task name is entered.

encoding default

provides the default language and encoding of the computer, e.g.,  
en-us cp1252

which means U.S. English using code page 1252.

The word 'default' may be used as an easier way of specifying the
default source or target encoding in other commands.

encoding list

provides a list of available encodings -- about 95 in all.

encoding show \*.txt

provides the encoding of all files meeting the \*.txt
specification. If a file has a Unicode byte order mark (BOM), the
encoding can be exactly determined. Otherwise, the encoding is
huristically detected by analyzing various factors. This is the
same algorithm used by the Mozilla Firefox web browser to detect
the encoding of text. It is usually correct, but not always.

encoding convert \*.txt utf-8b

converts all \*.txt files to UTF-8 encoding with a BOM. Use utf-8n
to get utf-8 without a BOM, which is the norm on Linux and the Mac.
For ease of typing, the dash character (-) is optional, so utf8b or
utf8n may be used instead. Note that these are not official
encoding names, but conventions to help clarify whether utf-8 is
being encoded with or without a BOM. Some Windows programs prefer
one, while others do not.

encoding convert \*.txt utf8n utf8b

converts \*.txt files to UTF8 with a BOM. In this case, both a
source and target encoding are specified. Rather than detecting the
source encoding, it is treated as UTF-8 without a BOM.

encoding convert \*.txt asciify

converts \*.txt files to ASCII, keeping only characters with
ordinal values less than 128, which may be represented with 7
rather than 8 bits. 'asciify' is an unofficial encoding that is
similar to the 'ascii' encoding, except that if a character with a
value above the ASCII range has an equivalent character or word
meaning in that range, it will be substituted. See the example of
the ellipses character below.

If the word 'backup' rather than 'convert' is used for the task,
the original files will be backed up with the same names except for
the addition of a .bak extension.

encoding url http://python.org

provides encoding information about the web page at that address.
Encoding references are sought in the server response headers and
meta data of the page. A conflict between encoding references is
reported.

encoding bytes \*.txt

provides a list of numeric byte values, one per line, for all files
matching the pattern. The first line is the file name. This is
probably most useful when analyzing a single source file, and when
redirecting standard output to another file that may be examined in
an editor, e.g.,  
encoding bytes test.txt \>temp.txt

encoding chars temp.txt \>test.txt

provides output in a similar form except that each line shows
information about a character rather than a byte (Unicode can
represent a character with multiple bytes). Each line has the
Unicode name of the character, its numeric code point, and an ASCII
equivalent of the character if available and different from the
original character. For example, the ellipses symbol has the code
point U2026, and an ASCII equivalent of three consecutive periods
(...), so it would appear as  
HORIZONTAL ELLIPSIS 8230 ...

Add a SourceEncoding parameter to specify the file's encoding
directly, rather than auto-detect it.

# Development Notes

The Encoding utility is developed with the Python 2.5 language
from  
[http://python.org](http://python.org)

The following built-in packages are used: codecs, glob, locale, os,
shutil, sys, and unicodedata.

The following third-party packages are used:

chardet -- Universal encoding detector  
[http://chardet.feedparser.org](http://chardet.feedparser.org)

encutils -- Encoding detection collection for Python  
[http://cthedot.de/encutils/](http://cthedot.de/encutils/)

py2exe -- Build standalone executables for Windows  
[http://py2exe.org](http://py2exe.org)

unidecode -- Unicode transliteration in Python  
[http://www.tablix.org/\~avian/blog/archives/2009/01/unicode\_transliteration\_in\_python/](http://www.tablix.org/~avian/blog/archives/2009/01/unicode_transliteration_in_python/)

The batch file, RunSetup.bat, runs the py2exe script, setup.py, to
create the stand-alone executable, Encoding.exe.

I welcome feedback, suggestions, and code contributions, which will
help this project improve over time. The latest version is
available at  
[http://EmpowermentZone.com/Encoding.zip](http://EmpowermentZone.com/Encoding.zip)

Jamal Mazrui  
[jamal@EmpowermentZone.com](mailto:jamal@EmpowermentZone.com)
