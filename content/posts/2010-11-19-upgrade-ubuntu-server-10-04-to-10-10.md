---
title: How to upgrade Ubuntu Server 10.04 to 10.10
date: 2010-11-19
draft: false
slug: upgrade-ubuntu-server-10-04-to-10-10
tags: ["system administration", "ubuntu"]
description: Blindly follow the commands in this post to update from Ubuntu Server 10.04 (Lucid) to 10.10 (Maverick)...
---

The following commands can be followed blindly to update an Ubuntu Server install from version 10.04 (Lucid) to version 10.10 (Maverick).

    ```bash
    apt-get update
    apt-get install update-manager-core
    sed -i 's/Prompt=lts/Prompt=normal/' /etc/update-manager/release-upgrades
    do-release-upgrade
