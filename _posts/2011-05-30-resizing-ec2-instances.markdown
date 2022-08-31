public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['aws', 'ec2', 'iaas', 'instance', 'instances', 'resize', 'system administration']
published: 2011-05-30
title: Resizing EC2 Instances
slug: resizing-ec2-instances

An EC2 instance needs to be stopped before it can be resized. Also, it can only be resized to a "compatible" type (ie, one with a compatible kernel, 32 bit or 64 bit). So, if you started with a 32 bit `t1.micro` you can only resize up to a 32 bit `m1.small`. If you started with a 64 bit `t1.micro` you could resize up to a 64 bit `m1.large`.


    :::text
    wintermute:~ $ ec2-stop-instances i-3e15ff51
    INSTANCE        i-3e15ff51      running stopping
    wintermute:~ $ ec2-modify-instance-attribute -t m2.2xlarge i-3e15ff51
    Client.IncorrectInstanceState: The instance 'i-3e15ff51' is not in the 'stopped' state.
    wintermute:~ $ ec2-modify-instance-attribute -t m2.2xlarge i-3e15ff51
    instanceType    i-3e15ff51      m2.2xlarge
    wintermute:~ $ ec2-start-instances i-3e15ff51
    INSTANCE        i-3e15ff51      stopped pending

  
By the way, these short posts are essentially notes to myself while working (I keep forgetting the syntax!). I've got some Cherokee-related posts in the pipeline, I just need to find some extra spare time at night.

In the meantime, [follow me on Twitter](http://twitter.com/davidltaylor), it's free.
