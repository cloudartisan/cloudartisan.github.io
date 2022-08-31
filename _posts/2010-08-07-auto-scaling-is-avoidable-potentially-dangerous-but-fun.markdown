public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['autoscaling', 'capacity', 'cloud management', 'iaas', 'load balancing', 'monitoring', 'rightscale']
published: 2010-08-07
title: Auto-Scaling Is Avoidable, Potentially Dangerous... But Fun
slug: auto-scaling-is-avoidable-potentially-dangerous-but-fun
summary: If you're blindly auto-scaling, you're doing it wrong... but probably having a fun time doing it...

RightScale have some tutorials on using their service to set up auto-scaling.  Recently I played around with it, configuring auto-scaling in response to increases and decreases in server load. Honestly, it was fun. But it was essentially a folly, an exercise in dealing unnecessarily with dangerous corner cases.

Here's why...

## Unconstrained Scaling

Unconstrained scaling is bad, mmkay. If you allow your systems to scale without constraint, you're risking a surprise credit card bill. Worse yet, if you're not paying any attention to your systems (shame!) then you could be in for a _jaw-dropping_ credit card bill.

Launching 20 on-demand `m1.small` Linux instances for a month will set you back approximately $1,200 USD. That, of course, is assuming they run continuously after launch. It gets _worse_ if you're launching them multiple times per hour.

Imagine your load is fluctuating up and down (or you've simply picked very poor thresholds to auto-scale). So let's say you're automatically launching and terminating instances several times per hour... let's say 3 times per hour... that's now $3,600.

Now, let's imagine half of those are `m2.2xlarge` Linux instances. We're now talking approximately $9,250.

Note, none of these rough calculations have taken traffic into account, or EBS usage, or S3 usage, or other sundry costs. And I'm not even going to do the maths for `m2.4xlarge` Windows instances!

## What About My ROI?

You might say, _So what? Doesn't that mean I have more customers? Doesn't that mean I have more income?_

Probably not. I doubt you have a direct correlation between demand and income.  I also doubt your charging is streamlined enough to protect your wallet.  Especially if you're a small, bootstrapped startup. Try explaining to your partner that some crazy ephemeral stuff happened somewhere on the Internet and now you can't afford the mortgage payment.

If you do manage to directly tie your income to server load...  congratulations! If you do manage to charge customers up-front for that server load before Amazon bills you... double congratulations! If you also have no bugs and will never ever _ever_ suffer a denial of service attack... I will bear your man-babies!

## Isn't Cloud All About Auto-Scaling?

No. It's about delivering compute power as a utility. You use what you need.  You use it when you need it. You pay for what you use. Like electricity.

## How Do I Cope With Demand?

Plan. Prepare. Monitor. React.

You need monitoring.

You need to know your trends.

You need to know what the business is doing.

If you have a product launch, a new ad, a new article, a new pricing plan, an election, seasonal load, etc and you expect increased demand, simply launch additional instances to cope. After you've weathered the storm, terminate them.

For the moments you can't predict, allow for a small amount of auto-scaling, with heavily-tested constraints and monitoring to alert you _before_ it starts. The limited auto-scaling covers for your response time. The monitoring alerts get you involved early on so you can make the call whether to launch additional servers or not.

## What About Those RightScale Tutorials?

Note, RightScale makes no mention of the risks of auto-scaling in their documentation. I think they should. I wonder if they've had any support requests along the lines of _"I followed your tutorials, scaled, and now I have to sell my car. Is this covered by your SLA?"_

Knowing what you know now, check out the main tutorial: [How do I set up Autoscaling?](http://support.rightscale.com/03-Tutorials/02-AWS/02-Website_Edition/How_do_I_set_up_Autoscaling%3f) It has links to all the necessary bits and bobs.

## And The Fun Stuff?

Here's a screenshot showing RightScale automatically launching web servers to cope with increased demand.

[![RightScale Auto-scaling](/media/img/2010/08/RightScale-Auto-scaling-1024x575.png)](/media/img/2010/08/RightScale-Auto-scaling.png)

Here's a screenshot showing one of my HAProxy load balancers backed by auto-scaled web servers.

[![Auto-scaling load balancing](/media/img/2010/08/Auto-scaling-load-balancing-1024x575.png)](/media/img/2010/08/Auto-scaling-load-balancing.png)

Now, go have some responsible, careful, constrained fun of your own!

_* Currently, a single on-demand m1.small Linux instance costs roughly $0.085 USD per hour_
_** Currently, a single on-demand m2.2xlarge Linux instance costs roughly $1.20 USD per hour_
