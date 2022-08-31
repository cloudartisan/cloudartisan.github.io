public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['rightscale', 'servertemplate', 'virtualmin']
published: 2010-10-20
title: "RightScale ServerTemplate: Virtualmin"
slug: rightscale-servertemplate-virtualmin
summary: I've published a [RightScale](http://www.rightscale.com) ServerTemplate for launching [Virtualmin](http://www.virtualmin.com) on Amazon EC2...

I've published a [RightScale](http://www.rightscale.com) ServerTemplate for launching [Virtualmin](http://www.virtualmin.com) on Amazon EC2.

> Virtualmin is a powerful and flexible web server control panel based on the well-known Open Source web-based systems management GUI, Webmin. Manage your virtual domains, mailboxes, databases, applications, and the entire server, from one comprehensive and friendly interface.

The ServerTemplate I've created makes it easy for anyone to get started providing managed hosting on cloud infrastructure.

[![Virtualmin Server Template](/media/img/2010/10/Virtualmin-Server-Template.png)](/media/img/2010/10/Virtualmin-Server-Template.png)

To try it out, simply [grab a free RightScale account](http://www.rightscale.com/products/free_edition.php), then [import my ServerTemplate](https://my.rightscale.com/library/server_templates/Virtualmin/14506), add it to a deployment and fire it up.

Once it's running you'll see something like:

[![Virtualmin Dashboard](/media/img/2010/10/Virtualmin-Dashboard-1024x575.png)](/media/img/2010/10/Virtualmin-Dashboard.png)

I dusted this ServerTemplate off and published it as part of RightScale's ServerTemplate Showdown. There's still a lot more work I could do on it, such as adding support for persistence between boots, support for reboot, backups to S3, etc.

You should [follow me on twitter](http://twitter.com/davidltaylor). If you use it, please let me know. If you have any questions or suggestions, fire away.
