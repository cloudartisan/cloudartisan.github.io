public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['general', 'hudson', 'system administration']
published: 2010-10-11
title: "Hudson: pam_authenticate failed"
slug: hudson-pam-authenticate-failed
summary: Ugh!!!

If you're getting login failures after enabling _Unix user/group database_ security check the log: `/var/log/hudson/hudson.log`.

If you see:

    :::text
    Oct 11, 2010 9:41:08 PM hudson.security.AuthenticationProcessingFilter2 onUnsuccessfulAuthentication
    INFO: Login attempt failed
    org.acegisecurity.BadCredentialsException: pam_authenticate failed : Authentication failure; nested exception is org.jvnet.libpam.PAMException: pam_authenticate failed : Authentication failure
      at hudson.security.PAMSecurityRealm$PAMAuthenticationProvider.authenticate(PAMSecurityRealm.java:100)
      at org.acegisecurity.providers.ProviderManager.doAuthentication(ProviderManager.java:195)
      at org.acegisecurity.AbstractAuthenticationManager.authenticate(AbstractAuthenticationManager.java:45)
      at org.acegisecurity.ui.webapp.AuthenticationProcessingFilter.attemptAuthentication(AuthenticationProcessingFilter.java:71)
      at org.acegisecurity.ui.AbstractProcessingFilter.doFilter(AbstractProcessingFilter.java:252)
      at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
      at org.acegisecurity.ui.basicauth.BasicProcessingFilter.doFilter(BasicProcessingFilter.java:173)
      at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
      at org.acegisecurity.context.HttpSessionContextIntegrationFilter.doFilter(HttpSessionContextIntegrationFilter.java:249)
      at hudson.security.HttpSessionContextIntegrationFilter2.doFilter(HttpSessionContextIntegrationFilter2.java:66)
      at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:87)
      at hudson.security.ChainedServletFilter.doFilter(ChainedServletFilter.java:76)
      at hudson.security.HudsonFilter.doFilter(HudsonFilter.java:164)
      at winstone.FilterConfiguration.execute(FilterConfiguration.java:195)
      at winstone.RequestDispatcher.doFilter(RequestDispatcher.java:368)
      at winstone.RequestDispatcher.forward(RequestDispatcher.java:333)
      at winstone.RequestHandlerThread.processRequest(RequestHandlerThread.java:244)
      at winstone.RequestHandlerThread.run(RequestHandlerThread.java:150)
      at java.lang.Thread.run(Thread.java:619) Caused by: org.jvnet.libpam.PAMException: pam_authenticate failed : Authentication failure
      at org.jvnet.libpam.PAM.check(PAM.java:105)
      at org.jvnet.libpam.PAM.authenticate(PAM.java:123)
      at hudson.security.PAMSecurityRealm$PAMAuthenticationProvider.authenticate(PAMSecurityRealm.java:90)
      ... 18 more
  
... the problem is likely caused by Hudson being unable to read your `/etc/shadow` file.

The simplest fix (note: I did not say "most secure") is to add the `hudson` user to the `shadow` group:

    :::text
    # usermod -a -G shadow hudson

After which, you'll need to stop then start Hudson (note: Hudson doesn't seem to handle an immediate restart very well):

    :::text
    # /etc/init.d/hudson restart
    Restarting Hudson Continuous Integration Server: hudson
    The selected http port (8080) seems to be in use by another program
    Please select another port to use for hudson failed!
    # /etc/init.d/hudson stop
    Stopping Hudson Continuous Integration Server: hudson.
    # /etc/init.d/hudson start
    Starting Hudson Continuous Integration Server: hudson
    Setting up max open files limit to 8192 .

You should now be able to log in. That's it.

You should [follow me on twitter](http://twitter.com/davidltaylor).
