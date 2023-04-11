---
title: "Installing mr.awsome on Mac OS X"
excerpt: "Once you know the correct incantation, installing is easy."
tags:
  - iaas
  - python
---

To quote the [mr.awsome](https://github.com/fschulze/mr.awsome) documentation "mr.awsome is a commandline-tool (aws) to manage and control Amazon Webservice's EC2 instances."

Once you know the correct incantation, installing it is easy.

~~~ shell
curl -o setuptools-0.6c11-py2.6.egg http://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg#md5=bfa92100bd772d5a213eedd356d64086
sudo sh setuptools-0.6c11-py2.6.egg
rm setuptools-0.6c11-py2.6.egg
export ARCHFLAGS="-arch i386 -arch x86_64"
easy_install mr.awsome
~~~

Simple as that.

[Follow me](http://twitter.com/davidltaylor) on Twitter. If you don't, kittens and fairies will die.
