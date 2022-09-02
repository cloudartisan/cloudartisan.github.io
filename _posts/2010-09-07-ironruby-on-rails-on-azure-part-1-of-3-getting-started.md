status: publish
public: yes
kind: post
chronological: yes
author: Ameer Deen
tags: ['paas', 'rails', 'sqlazure', 'windows azure']
published: 2010-09-07
title: IronRuby on Rails on Azure (Part 1 of 3) - Getting Started
slug: ironruby-on-rails-on-azure-part-1-of-3-getting-started
summary: Ameer builds an eclectic proof of concept on top of Windows Azure (part 1 of 3)...

This is the first of a three part series on running a rails application on Windows Azure using SQLAzure as your database backend. The Rail Guides website, of course, has a wonderful getting started [article](http://guides.rubyonrails.org/getting_started.html) that I couldn't possibly do justice. This small series is just a very simple demonstration of one possible way of developing a rails application on Microsoft's Azure platform.

In this part, we'll simply be focusing on getting a basic rails application running on your laptop or desktop using IronRuby and SQL Server and links to download bundles that you can try out for yourself. If you already know how to do all that, skip to the end of this article to the download bundles and head over to Part 2: Connecting your rails application to SQLAzure 

## Installing IronRuby 1.1

IronRuby 1.1 runs on either .NET Framework v3.5 or v4. I'll be using the package targeted at .NET v3.5 for our example simply because I wasn't sure if most people would have the newer framework installed on their machines. Ruby normally lives in a self-contained folder. Installing IronRuby, therefore, is as simple as downloading this 4MB zip [file](http://ironruby.codeplex.com/releases/view/43540#DownloadId=133276) and unpacking it.   For the purposes of this article, I've created a root folder called


    :::text
    C:\Sample


and unzipped the contents of the IronRuby zip file to


    :::text
    C:\Sample\ironruby


## Installing Rails

Install IronRuby on Rails by typing:

    
    :::text
    cd C:\Sample\IronRuby\bin
    .\igem install rails --version 2.3.8


You should see output similar to the following:

    
    :::text
    C:\Sample\IronRuby\bin>igem install --version 2.3.8  
    Successfully installed rake-0.8.7
    Successfully installed activesupport-2.3.8
    Successfully installed activeresource-2.3.8
    Successfully installed rails-2.3.8
    8 gems installed


## Installing SQL Server Active Record Adapter

For rails to use the active-record pattern with MS SQL Server, we’ll also need to install the `activerecord-sqlserver-adapter` gem:


    :::text
    c:\Sample\IronRuby\bin>.\igem install activerecord-sqlserver-adapter --version 2.3.8
     Successfully installed activerecord-sqlserver-adapter-2.3.8
     1 gem installed
     Installing ri documentation for activerecord-sqlserver-adapter-2.3.8...
     Installing RDoc documentation for activerecord-sqlserver-adapter-2.3.8...** **


## Configuring SQL Server

SQLAzure is based on SQL Server 2008 and uses SQL Authentication. I’m not going to cover SQL server installation in this article. Please ensure you install SQL Server 2008 (or 2008 Express) on your development machine and enable SQL Server authentication mode.

For our example, let’s ensure we have the following setup on our SQL Server:


    :::text
    Server: localhost
    Database: dev
    Username: myuser
    Password: mypassword

  
Please ensure the ‘myuser’ login has CRUD privileges on the ‘dev’ database.

## Creating a vanilla rails application

Create the canonical rails application in our sample as follows:


    :::text
    cd c:\sample
    Set path=%path;C:\Sample\IronRuby\bin
    .\IronRuby\bin\rails myapp


As you would expect, that should create a host of new files that comprise our new rails application.

## Configuring our rails application to talk to SQL Server**

The database.yml database configuration file under C:\Sample\myapp\config\ tells rails how to connect to the application’s database. Replace the following default connection string in database.yml that was generated:


    :::yaml
    development:
      adapter: sqlite3
      database: db/development.sqlite3
      pool: 5
      timeout: 5000


with the following:


    :::yaml
    development:
      mode: ADONET
      adapter: sqlserver
      host: .
      database: dev
      username: myuser
      password: mypassword


We have now installed IronRuby, Rails and other necessary gems and configured our database.yml with the appropriate connection string to tell rails how to talk to SQL Server.

All that remains is starting up the application:

    
    :::text
    cd c:\Sample
    .\IronRuby\bin\ir myapp\script\server


You should see the webrick web server start up:

    
    :::text
    c:\Sample>.\IronRuby\bin\ir myapp\script\server
    WARNING: YAML.add_builtin_type is not implemented
    => Booting WEBrick
    => Rails 2.3.8 application starting on http://0.0.0.0:3000
    => Call with -d to detach
    => Ctrl-C to shutdown server
    [2010-09-06 20:34:18] INFO  WEBrick 1.3.1
    [2010-09-06 20:34:18] INFO  ruby 1.8.6 (2009-03-31) [i386-mswin32]
    [2010-09-06 20:34:18] INFO  WEBrick::HTTPServer#start: pid=5076 port=3000

  
Browse to http://localhost:3000 and you should see the “Welcome Aboard” rails default home page. Click on the “About your application’s environment” link and you should see “sqlserver” listed next to “Database adapter”. We now have a rails application running on our development station talking to SQL Server.

We’re now just a few steps away from tweaking this setup slightly to get out rails application to talking to your SQLAzure account instead.


## Download bundles**  

The bundle assumes you have an existing SQL Server installed on your machine with the following configuration:

    
    
    :::text
    SQL Server: localhost
    Database: dev
    Username: myuser
    Password: mypassword
    

  
The bundle contains:

 * IronRuby
 * All requisite gems
 * Sample rails app

Unzip this [sample.zip](http://github.com/downloads/writeameer/IronRuby-on-SQLAzure-sample/Sample.zip) file on to your root folder. Double click on `runme.bat` under the c:\sample folder to start your rails app.

In the next part, we'll see how to point your rails application to use SQLAzure as it's backend.
