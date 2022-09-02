status: publish
public: yes
kind: post
chronological: yes
author: David Taylor
tags: ['paas', 'rails', 'sqlazure', 'windows azure']
published: 2010-09-08
title: IronRuby on Rails on Azure (Part 2 of 3) – Connecting your Rails app to SQLAzure
slug: ironruby-on-rails-on-azure-part-2-of-3-%e2%80%93-connecting-your-rails-app-to-sqlazure
summary: Ameer builds an eclectic proof of concept on top of Windows Azure (part 2 of 3)...

This is the continuation of my bungling around with IronRuby, Rails and getting it running on SLQAzure. In part 1, we installed a basic rails application using IronRuby with SQL Server as it's backend. We'll now examine how we can connect this application to a SQLAzure backend as opposed to a SQL Server hosted on your development machine.

I’m assuming you have the vanilla rails application from Part 1 up and running and have verified that the rails application can communicate with your SQL server database by clicking on the “About your application’s environment” link as described in the previous article. I’m also assuming you’ve already signed up for a SQLAzure account and know how to connect to it.

Connecting your rails app has two main gotchas:

## Gotcha #1: SQL Server active record adapter does not work with SQL Azure

The SQL Server active record gem we installed in part 1 does not work out of the box with SQL Azure and needs to be modified slightly before it can be made to work. The SQL server active record adapter identifies the version of SQL Server using the following SQL transact-sql query:


    select @@version


A non-Azure SQL Server would normally respond with something like:


    Microsoft SQL Server 2008 (SP1) - 10.0.2531.0 (Intel X86)   Mar 29 2009 10:27:29   Copyright (c) 1988-2008 Microsoft Corporation  Express Edition on Windows NT 6.1  (Build 7600: )


The active record adapter then picks up the year from the four digits following the words “Micrsoft SQL Server”. In the case above, it would pick up “2008” SQLAzure, however, responds to the same query above with the following:


    Microsoft SQL Azure (RTM) - 10.25.9386.0   Jul 21 2010 12:47:47   Copyright (c) 1988-2009 Microsoft Corporation


The active record adapter attempts to pick up the year from the four digits following the words “Microsoft SQL server”, find none and errors out.

All of this logic happens in “sqlserver_adapter.rb”. If you’ve followed the same directory structure in Part 1, this file can be found in


    C:\Sample\IronRuby\lib\ironruby\gems\1.8\gems\activerecord-sqlserver-adapter-2.3.8\lib\active_record\connection_adapters\sqlserver_adapter.rb


I modified the following function:


    :::ruby
    def database_year
        DATABASE_VERSION_REGEXP.match(database_version)[1].to_i
    end


To my uglier but SQLAzure friendly:


    :::ruby
    def database_year
        #Ameer's horrible hack for SQL Azure  
        # Find the numbers following the first ') -'
        REGEXP = /\)\s\-\s[0-9]+(?:\.[0-9]*)?/
        version = REGEXP.match(database_version)[0]
        version.gsub!(") - ","")
        version = (version.to_i).to_s  
        #Map the number to a SQL Server version
        VERSION_MAP = {"8"=>2000, "9" => 2005, "10" => 2008}
        VERSION_MAP[version]  
    end


I'd love to hear from someone who can help me improve the Ruby above. I’m essentially attempting to extract the SQL Server version number (9,10 etc) that appears after the first “) -“ character sequence and use that to determine the SQL server release year (2000, 2005 or 2008).


## Gotcha #2: Migrations do not work with SQL Azure

Everytime I tried to do a rails migration I’m met with an error that SQL Azure does not support tables without clustered indexes. It turns out, the table SQLAzure was complaining about was the schema_migrations table.

So...I just added one :)


    :::sql
    CREATE UNIQUE CLUSTERED INDEX Idx1 ON schema_migrations(version)


Given the above to fixes, all we need to do is point our database.yml to our SQLAzure instance in the cloud:


    development:
      mode: ADONET
      adapter: sqlserver
      host: <your SQLAzure server>.database.windows.net
      database: <database name>
      username: <username>
      password: <password>


The download bundle in part one already had the updated “sqlserver_adapter.rb” file. If you’ve downloaded the bundle from part 1 and already have a SQL Azure account, all you need to do is update your database.yml and you’re ready to go.

In part 3 we'll see how we deploy a rails application on Windows Azure and have it use SQL Azure as its backend.
