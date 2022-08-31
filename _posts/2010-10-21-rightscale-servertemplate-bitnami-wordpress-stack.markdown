public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['rightscale', 'servertemplate', 'wordpress']
published: 2010-10-21
title: "RightScale ServerTemplate: Bitnami WordPress Stack"
slug: rightscale-servertemplate-bitnami-wordpress-stack
summary: I've published a [RightScale](http://www.rightscale.com) ServerTemplate for installing [Bitnami's WordPress stack](http://bitnami.org/stack/wordpress) on Amazon EC2...

I've published a [RightScale](http://www.rightscale.com) ServerTemplate for installing [Bitnami's WordPress stack](http://bitnami.org/stack/wordpress) on Amazon EC2.

> WordPress is web software you can use to create a beautiful website or blog.

It is based on an existing ServerTemplate by Bitnami. It differs from Bitnami's existing WordPress ServerTemplate in a few ways:

  1. it uses an Ubuntu RightScale MultiCloud Image as its base
  2. it has some of RightScale's RightScripts for logging and monitoring added
  3. it installs the WordPress stack from a supplied URL, meaning you can trial different versions of the WordPress stack easily
  
Using this ServerTemplate you can easily fire up a WordPress instance to:

  1. build and run a blog, or
  2. trial/compare different versions of Bitnami's WordPress stack
  
I've used it for the latter.

To try it out, simply [grab a free RightScale account](http://www.rightscale.com/products/free_edition.php), then [import my ServerTemplate](http://www.rightscale.com/library/server_templates/Bitnami-WordPress-Stack/14485).

[![Bitnami WordPress Stack](/media/img/2010/10/Bitnami-WordPress-Stack-ServerTemplate.png)](/media/img/2010/10/Bitnami-WordPress-Stack-ServerTemplate.png)

Next, add it to a deployment and fire it up. Once it's running you'll see something like:

[![Bitnami WordPress Welcome Page](/media/img/2010/10/Bitnami-WordPress-Welcome-Page-1024x575.png)](/media/img/2010/10/Bitnami-WordPress-Welcome-Page.png)

I've published this as part of RightScale's ServerTemplate Showdown. It's nothing spectacular, but I found it useful and hopefully it will be of some use to someone else. I have a draft version that has some basic support for preparing and installing on an EBS volume, which would add persistence. I haven't released that version yet.

[Follow me on twitter](http://twitter.com/davidltaylor) and if you use it, please let me know, if you have any questions or suggestions, fire away.
