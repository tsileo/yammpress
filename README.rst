=========
YammPress
=========

YammPress is a **Ya**ml, **M**ongoDB, **M**arkdown powered blogging engine written in Python aimed for developers who want to quickly add a minimal blog to any web project.

Here is the concept:

* A command line utility to create/update/insert posts
* Posts are written in Markdown, with a Yaml header
* Developer friendly (github flavored markdown like codeblocks and syntax highligt with pygments)
* Markdown files as database, parsed and cached in MongoDB
* No template, just a helper class, but you can retrieve posts directly in MongoDB with any language


Overview
========

You can check out a simpe flask demo app in the demo folder.

::

    $ yammpress new_post "My Awesome Title"
    $ yammpress generate
    $ yammpress status
    $ yammpress drop


Requirements
============

* `Markdown2 <https://github.com/trentm/python-markdown2>`_

Installation
============

::

    $ pip install yammpress


Usage
=====

Basic usage, "yammpress -h" or "yammpress <command> -h" to show the help.

Create a new post
-----------------

::

    $ yampress new_post "My Awesome Blog Post"

Generate posts
--------------

Generate take care of creating/updating posts (with MongoDB upsert).

::

    $ yammpress generate


Status
------

::

    $ yampress status


Drop
----

::

    $ yampress status



License (MIT)
=============

Copyright (c) 2013 Thomas Sileo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
