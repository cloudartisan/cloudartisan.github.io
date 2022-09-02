public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['aws', 'ec2', 'iaas', 'iam', 'openssl', 'security', 'system administration']
published: 2011-04-18
title: Getting Started With AWS Identity Access Management
slug: getting-started-with-aws-identity-access-management

AWS Identity Access Management (IAM) is a free feature provided with your AWS
account...

> enabling businesses to create multiple Users with individual security credentials who can use AWS web services, all controlled by and billed to a single AWS Account

For example, you might use it to:

  * restrict your web application to only manage S3
  * give accounts to an operations team, adding them to an operations group that can reboot EC2 instances
  * bring on contractors for short-term work
  * prevent yourself from accidentally stopping or deleting your RDS instance
  * enforce separation of your testing, staging, and production environments
  * and much more
  
How many of you are using the credentials of your AWS 'master' account to do everything? Well... simply put... don't do that!

You do **not** want to risk dropping those credentials into your `bash` history or leaving them littered around on servers or EBS volumes. You want to take the same approach you would with the `root` account on servers. Sure, you might need the `root` account to get started, but one of the first things you would do after that would be to create user credentials and drop privileges.

Using the process I've documented below you can use your existing AWS 'master' credentials to create a new set of credentials for yourself. Afterwards, these credentials will be the default for working with all AWS command-line tools and you can stop using your 'master' credentials. Similarly, you could use the process below to create AWS credentials for other purposes (other users, an application, etc).

First, download the [AWS Identity and Access Management software](http://aws.amazon.com/developertools/AWS-Identity-and-Access-Management/4143), then unzip it somewhere sensible. I unzipped it into `~/AWS`, where I store all the AWS command-line tools. This gave me a `~/AWS/IAMCli-1.2.0` directory, to which I created a symbolic link:


    :::text
    wintermute:~/AWS $ unzip ~/Downloads/IAMCli.zip
    wintermute:~/AWS $ ln -s IAMCli-1.2.0 IAMCli


Now that you have the software, you'll need to setup your shell environment.  Here's an example based on my own Mac OS X configuration (in `.bash_profile`):


    :::bash
    # Paths needed for AWS EC2, AWS IAM, etc
    export JAVA_HOME=/Library/Java/Home
    export EC2_HOME=$HOME/AWS/EC2
    export AWS_IAM_HOME=$HOME/AWS/IAM
    export PATH=$PATH:$EC2_HOME/bin:$AWS_IAM_HOME/bin  
    # EC2 credentials
    export EC2_PRIVATE_KEY=~/.aws/pk.pem
    export EC2_CERT=~/.aws/cert.pem  
    # IAM credentials
    export AWS_CREDENTIAL_FILE=~/.aws/account-key  
    # Default EC2 URL: US West
    export EC2_URL=https://ec2.us-west-1.amazonaws.com


As you can see, I keep my credentials in a directory called `~/.aws`, which I make sure no one else has access to:


    :::text
    wintermute:~/AWS $ mkdir ~/.aws
    wintermute:~/AWS $ chmod 0700 ~/.aws


As we're only starting out with IAM, we don't yet have our own credentials, we only have the credentials for our 'master' AWS account. For now, we'll dump those 'master' credentials into `~/.aws/account-key` and later we'll replace them with our new credentials:


    :::text
    AWSAccessKeyId=EXAMPLEEXAMPLEEXAMPLE
    AWSSecretKey=EXAMPLEKEYEXAMPLEKEYEXAMPLEKEYEXAMPLEKEY


Now, try sourcing your profile and check that you can execute an IAM command- line tool. For example:


    :::text
    wintermute:~ $ source ~/.bash_profile
    wintermute:~ $ iam-usercreate -h  
    Creates a new user in your account. You can also optionally add the user to one or more groups, and create an access key for the user.  
    iam-usercreate [options...] arguments...  
    . . .


There we go, right now we've done enough to be dangerous... and we're now ready to create groups and users.

Now I'll create an `Admin` group:


    :::text
    wintermute:~ $ iam-groupcreate -g Admin
    wintermute:~ $ iam-grouplistbypath
    arn:aws:iam::123456789012:group/Admin


We'll create a policy for an `Admin` group. This group will be allowed to perform any action on any resource. Basically, any user credentials in this group will confer the same power as the 'master' credentials. On a vaguely related now... I like to keep all my policies and credentials in a **private** repository. I recommend you do, too.

You may wish to prevent certain actions, such as using IAM to create additional accounts. I don't. I want administrators to be able to use their individual credentials to do all AWS management tasks.


    :::text
    wintermute:~ $ vi ~/Git/cloudartisan/aws/policies/AdminGroupPolicy.txt
    wintermute:~ $ cat ~/Git/cloudartisan/aws/policies/AdminGroupPolicy.txt
    {
        "Statement":[{
            "Effect":"Allow",
            "Action":"*",
            "Resource":"*"
        }]
    }


The new group policy is applied by uploading it:

    
    :::text
    wintermute:~ $ iam-groupuploadpolicy -g Admin -p AdminGroupPolicy -f ~/Git/cloudartisan/aws/policies/AdminGroupPolicy.txt
    wintermute:~ $ iam-grouplistpolicies -g Admin
    AdminGroupPolicy


Now that we have our `Admin` group we can create a user for our own use. I'm going to create a `david` user:


    :::text
    wintermute:~ $ iam-usercreate -u david -g Admin -k -v
    AKIAIOEXAMPLEEXAMPLE
    wJaEXAMPLEKEYEMI/KEXAMPLEKEYfiCYzEXAMPLEKEY
    arn:aws:iam::123456789012:user/david
    AKIAIOEXAMPLEEXAMPLE


I now have the credentials for my `david` account. And, if you've been playing along, you should now have the credentials for your own account. Now we can backup our existing `~/.aws/account-key` file and update it to use our new access key ID and secret key. I'm feeling brave, so I'm going to replace my old credentials with my new credentials:


    :::text
    wintermute:~ $ vi ~/.aws/account-key
    wintermute:~ $ cat ~/.aws/account-key
    AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE
    AWSSecretKey=wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY


Alternatively, if you're worried and want to be able to switch back with ease, create a new file using your new credentials and change `AWS_CREDENTIAL_FILE` to point to your new file. For example:


    :::bash
    # IAM credentials
    export AWS_CREDENTIAL_FILE=~/.aws/david_cloudartisan_cred.txt


We're not finished yet! Some of the AWS command-line tools require a private key and a certificate. No problem, we can generate those easily enough. We'll need OpenSSL, a hacksaw, and a colostomy bag. Well... maybe just OpenSSL...  but I'm not promising anything.

Here I generate my private key and certificate files:


    :::text
    wintermute:~ $ openssl version
    OpenSSL 0.9.8o 01 Jun 2010
    wintermute:~ $ openssl genrsa 1024 > pk.pem
    wintermute:~ $ openssl req -new -x509 -nodes -sha1 -days 730 -key ~/.aws/pk.pem -out ~/.aws/cert.pem


After generating them I add the certificate to my user credentials:


    :::text
    wintermute:~ $ iam-useraddcert -u david -f cert.pem


AWS command-line tools that require a private key and certificate will look for the `EC2_PRIVATE_KEY` and `EC2_CERT` environment variables if they're not supplied at the command-line. I like the sound of that, so we'll do the following in the shell (and, of course, add the same to our `.bash_profile` or `.bashrc`):


    :::text
    wintermute:~ $ export EC2_PRIVATE_KEY=~/.aws/pk.pem
    wintermute:~ $ export EC2_CERT=~/aws/cert.pem


If everything's working OK we should now be able to run `ec2-describe- instances` without any arguments and using our new credentials. Seriously.  Just like this:


    :::text
    wintermute:~ $ ec2-describe-instances


And that's it, we're using our own credentials. In my case, I'm the user `david` in the `Admin` group.

Where does this leave us? Don't wait for me to write the next blog post. Get cracking! Read up on the policy syntax, create groups for your departments and applications, assign user credentials... but, most of all, **stop using those 'master' credentials!**

[Follow me on Twitter](http://twitter.com/davidltaylor) and harass me to write the next blog post. You won't regret it. Although I might...
