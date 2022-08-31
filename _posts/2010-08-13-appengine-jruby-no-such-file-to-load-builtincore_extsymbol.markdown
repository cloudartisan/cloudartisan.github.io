public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['google app engine', 'jruby', 'paas']
published: 2010-08-13
title: appengine-jruby "no such file to load -- builtin/core_ext/symbol"
slug: appengine-jruby-no-such-file-to-load-builtincore_extsymbol
summary: Ugh!!!

A while ago I wrote a proof of concept in JRuby on Google App Engine, using the fantastic [appengine-jruby](http://code.google.com/p/appengine-jruby/) project. The code worked (albeit, _very slowly!_).

Satisfied, I put the code to the side, committed to a Subversion repository.

Today I got a chance to dust off the code and do some more work on it... only to find it no longer worked.

When I started my code with `dev_appserver.rb` I saw:

    :::text
    $ dev_appserver.rb .
    => Booting DevAppServer
    => Press Ctrl-C to shutdown server
    . . .
    SEVERE: [1281662003740000] javax.servlet.ServletContext log: Warning: error application could not be initialized
    org.jruby.rack.RackInitializationException: no such file to load -- builtin/core_ext/symbol at org.jruby.rack.DefaultRackApplicationFactory.newRuntime(DefaultRackApplicationFactory.java: 85) at org.jruby.rack.DefaultRackApplicationFactory.createApplication(DefaultRackApplicationFactory.java: 177) at org.jruby.rack.DefaultRackApplicationFactory.newErrorApplication(DefaultRackApplicationFactory.java: 127) at org.jruby.rack.DefaultRackApplicationFactory.init(DefaultRackApplicationFactory.java: 45) at org.jruby.rack.SharedRackApplicationFactory.init(SharedRackApplicationFactory.java: 26) at org.jruby.rack.RackServletContextListener.contextInitialized(RackServletContextListener.java: 40) at org.mortbay.jetty.handler.ContextHandler.startContext(ContextHandler.java: 548) at org.mortbay.jetty.servlet.Context.startContext(Context.java:136) at org.mortbay.jetty.webapp.WebAppContext.startContext(WebAppContext.java: 1250) at org.mortbay.jetty.handler.ContextHandler.doStart(ContextHandler.java: 517) at org.mortbay.jetty.webapp.WebAppContext.doStart(WebAppContext.java: 467) at org.mortbay.component.AbstractLifeCycle.start(AbstractLifeCycle.java: 50) at org.mortbay.jetty.handler.HandlerWrapper.doStart(HandlerWrapper.java: 130) at org.mortbay.component.AbstractLifeCycle.start(AbstractLifeCycle.java: 50) at org.mortbay.jetty.handler.HandlerWrapper.doStart(HandlerWrapper.java: 130) at org.mortbay.jetty.Server.doStart(Server.java:224) at org.mortbay.component.AbstractLifeCycle.start(AbstractLifeCycle.java: 50) at com.google.appengine.tools.development.JettyContainerService.startContainer(JettyContainerService.java: 185) at com.google.appengine.tools.development.AbstractContainerService.startup(AbstractContainerService.java: 147) at com.google.appengine.tools.development.DevAppServerImpl.start(DevAppServerImpl.java: 219) at com.google.appengine.tools.development.DevAppServerMain$StartAction.apply(DevAppServerMain.java:164) at com.google.appengine.tools.util.Parser $ParseResult.applyArgs(Parser.java:48) at com.google.appengine.tools.development.DevAppServerMain.(DevAppServerMain.java: 113) at com.google.appengine.tools.development.DevAppServerMain.main(DevAppServerMain.java: 89) Caused by: org.jruby.exceptions.RaiseException: no such file to load -- builtin/core_ext/symbol at (unknown).new(:1) at (unknown).(unknown)(:1)


_Wonderful!_

After a lot of tedious messing around, I realised the problem was that I had a space in the name of one of the parent directories.

For some more detail, have a look at [this bug report](http://jira.codehaus.org/browse/JRUBY-4774).

My advice to people using `jruby-complete.jar`: you will get an indecipherable exception if you try to run your application under a directory with a space in it... so don't do that.

You should follow me on twitter [here](http://twitter.com/davidltaylor).
