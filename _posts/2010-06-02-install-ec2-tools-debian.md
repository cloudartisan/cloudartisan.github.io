title: Install EC2 AMI & API Tools in Debian
author: David Taylor
published: 2010-06-02
tags: [aws, ec2, debian, iaas]
slug: install-ec2-tools-debian
status: publish
public: yes
chronological: yes
kind: post
summary: A quick run-down on installing EC2 AMI & API Tools in Debian...

Download the zip files for the tools:

    :::bash
    $ wget http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip
    $ wget http://s3.amazonaws.com/ec2-downloads/ec2-ami-tools.zip

Unzip the tools:

    :::bash
    $ unzip ec2-api-tools.zip
    $ unzip ec2-ami-tools.zip

This will give you some directories with version numbers appended.
Put them in a safe place:

    :::bash
    $ mkdir /usr/local/ec2
    $ cp -r ec2-ami-tools-1.3-34544/* /usr/local/ec2/
    $ cp -r ec2-api-tools-1.3-42584/* /usr/local/ec2/

Install Java:

    :::bash
    $ apt-get install sun-java6-jre

Edit the system-wide profile:

    :::bash
    $ vi /etc/profile

Add the following to the file:

    :::bash
    # EC2 Tools
    export EC2_HOME=/usr/local/ec2
    export PATH=$PATH:$EC2_HOME/bin
    export JAVA_HOME=/usr

When someone logs in, their environment will be ready and raring
to go. Users can then issue commands such as:

    :::bash
    $ ec2-describe-instances -K pk-HZF5F4JFK4ZCKLU6FCVW25DQSEHQQ4LH.pem -C cert-HZF5F4JFK4ZCKLU6FCVW25DQSEHQQ4LH.pem
