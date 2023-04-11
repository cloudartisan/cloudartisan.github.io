---
title: "Resizing an RDS database instance"
excerpt: "Notes on resizing an RDS instance."
tags:
  - database
  - iaas
  - rds
  - resize
---

I keep forgetting how to do this, so...

~~~ console
  wintermute:~ $ rds-modify-db-instance mydb --region us-east-1 --db-instance-class db.m2.2xlarge --apply-immediately
  DBINSTANCE  mydb  2011-05-20T01:24:19.131Z  db.m1.large  mysql  250  master  available  mydb.abcdefghijk.us-east-1.rds.amazonaws.com  3306  us-east-1b  0  db.m2.2xlarge  n  5.5.8
        SECGROUP  default  active
        PARAMGRP  mydb-params  in-sync
~~~

Yup, that involves an immediate outage for that database.

Yup, that's the really expensive one...
