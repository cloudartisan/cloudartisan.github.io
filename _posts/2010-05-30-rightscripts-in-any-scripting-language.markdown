title: RightScripts In Any Scripting Language
author: David Taylor
published: 2010-05-30
tags: [cloud, python, rightscale, rightscript]
slug: rightscripts-in-any-scripting-language
status: publish
public: yes
chronological: yes
kind: post
summary: You can write RightScripts in any scripting language with only a little jiggery-pokery. Break free from Bash, Ruby, or Perl and maybe write a Lua or Python RightScript instead. Here's how...

[RightScale's](http://www.rightscale.com/) cloud management platform can be used to deploy and manage solutions on cloud infrastructure with some degree of automation, control, and scaling.

Users create [RightScripts](http://support.rightscale.com/12-Guides/01-RightScale_Dashboard_User_Guide/03-Design/02-RightScripts) to automate actions on their servers. Think of them the same way you would any other script for managing a server. The differences are that they are managed inside RightScale's management platform, with version control, easy reuse, and access to handy environment variables. A RightScript is typically written in Bash, Ruby, or Perl, and has variables that are initialised using input parameters.

Input parameters are essentially environment variables for RightScripts.  RightScale's user interface attempts to identify these input parameters by analysing your script. And here is where our problem arises... RightScale only identifies input parameters for uninitialised global variables preceded by the '$' character. That's why RightScripts are typically written in Bash, Ruby, or Perl - so that input parameters will work.

## Bash, Ruby, Perl BEGONE!

What if we don't want to use Bash, Ruby, or Perl?  What if we think Bash isn't up to the job, Ruby is Python's cross-dressing uncle, and Perl is evil? Could we use Python? What about Groovy? Lua?

Absolutely.

We can use any scripting language we want (except the evil ones).  We just need to make RightScale identify the input parameters we want. To do that, we need to trick RightScale into seeing uninitialised global variables that look like Bash, Ruby, or Perl.  The simplest way is by 'declaring' the input parameters we want in comments. The input parameters can then be accessed by our RightScript as environment variables.

## Specifying Input Parameters
  
To specify the input parameters our script will require, we place them in comments, preceded by the '$' character.  RightScale will identify these as uninitialised global variables and create corresponding input parameters.

For example:

    :::bash
    # $WELL_NAMED_VAR_1
    # $WELL_NAMED_VAR_2

## Writing The RightScript Right

There are two ways we can write our non-Bash, non-Ruby, non-Perl script:

1. as an attachment to a Bash, Ruby, or Perl RightScript
2. directly as _the_ RightScript
  
The second option is better for the following reasons:

* we can view our code without needing to open a separate attachment
* we get the benefit of RightScale's revision control
* we don't have to deal with Bash, Ruby, or Perl if we don't want to
  
## Python Example

Here's an example in Python that has two input parameters, LOG_IDENT and LOG_MESSAGE:

    :::python
    #!/bin/env python
    #
    # Writes a log message using syslog.
    #
    # Inputs:
    # $LOG_IDENT
    # $LOG_MESSAGE  
    import os
    from syslog import openlog, syslog  
    openlog(os.environ["LOG_IDENT"])
    syslog(os.environ["LOG_MESSAGE"])

In RightScale this looks like:

[![Screenshot of a Python RightScript](/media/img/2010/05/Screenshot-1024x583.png)](/media/img/2010/05/Screenshot.png)

## Simple

All we needed was some comments and '$' characters.

Try it yourself with your favourite scripting language. Break free of Bash, Ruby, or Perl.
