public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['drupal', 'rightscale', 'servertemplate']
published: 2010-10-21
title: "RightScale ServerTemplate: Bitnami Drupal Stack"
slug: rightscale-servertemplate-bitnami-drupal-stack
summary: I've published a [RightScale](http://www.rightscale.com) ServerTemplate for installing [Bitnami's Drupal stack](http://bitnami.org/stack/drupal) on Amazon EC2...

I've published a [RightScale](http://www.rightscale.com) ServerTemplate for installing [Bitnami's Drupal stack](http://bitnami.org/stack/drupal) on Amazon EC2.

> Drupal is an open source content management platform powering millions of websites and applications. It’s built, used, and supported by an active and diverse community of people around the world.

  
My ServerTemplate is based on an existing ServerTemplate by Bitnami. It differs from Bitnami's existing Drupal ServerTemplate in a few ways:

  1. it uses an Ubuntu RightScale MultiCloud Image as its base
  2. it has some of RightScale's RightScripts for logging and monitoring added
  3. it installs the Drupal stack from a supplied URL, meaning you can trial different versions of the Drupal stack easily
  
Using this ServerTemplate you can easily fire up a Drupal instance to either:

  1. build and run a site, or
  2. trial/compare different versions of Bitnami's Drupal stack
  
I've used it for the latter.

To try it out, simply [grab a free RightScale account](http://www.rightscale.com/products/free_edition.php), then [import my ServerTemplate](http://www.rightscale.com/library/server_templates/Bitnami-Drupal-Stack/14481).

[![Bitnami Drupal Stack](/media/img/2010/10/Bitnami-Drupal-Stack-ServerTemplate.png)](/media/img/2010/10/Bitnami-Drupal-Stack-ServerTemplate.png)

Then add it to a deployment and fire it up. Once it's running you'll see something like:

[![Bitnami Drupal Welcome Page](/media/img/2010/10/Bitnami-Drupal-Welcome-Page-1024x575.png)](/media/img/2010/10/Bitnami-Drupal-Welcome-Page.png)

and:

[![Bitnami Drupal Login Page](/media/img/2010/10/Bitnami-Drupal-Login-Page-1024x575.png)](/media/img/2010/10/Bitnami-Drupal-Login-Page.png)

I've published this as part of RightScale's ServerTemplate Showdown. It's nothing spectacular, but I found it useful and hopefully it will be of some use to someone else. I have a draft version that has some basic support for preparing and installing on an EBS volume, which would add persistence, although I haven't released that version yet.

[Follow me on twitter](http://twitter.com/davidltaylor) and if you use it, please let me know, if you have any questions or suggestions, fire away.
