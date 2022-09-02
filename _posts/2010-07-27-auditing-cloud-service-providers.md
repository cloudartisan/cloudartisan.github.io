public: yes
status: publish
kind: post
chronological: yes
author: David Taylor
tags: ['auditing', 'cloud', 'process', 'processes', 'questionnaire', 'security', 'survey']
published: 2010-07-27
title: Auditing Cloud Service Providers
slug: auditing-cloud-service-providers
summary: Asked to audit our cloud service provider, I decide to see what's out there...

## What's Up?  

I want to find existing documented best practice processes and questionnaires for auditing cloud service providers.

I was hoping to find existing surveys/questionnaires that can be reused to perform audits on cloud service providers. I was also hoping those audits could be performed without introducing much additional load for the auditor or the cloud service providers. _Especially_ for the auditor... because, no doubt, that will be me.

Let's face it, no one enjoys an auditing. No cloud service provider thinks _"Oh, goody, another small prospect that wants me to respond to yet-another- time-consuming audit!"_ And I certainly do not want to write a lengthy document of intrusive questions about services I'm already using.

## Early Research  

Unfortunately, so far I've found that cloud computing hasn't reached that stage... yet.

I came across articles on how standardised surveys/questionnaires do not exist, how the myriad different audit efforts are stifling cloud service providers, bogging them down, inhibiting innovation. Here are a couple of examples:

  * [Stop the Madness! Cloud Onboarding Audits - An Open Question](http://cloudsecurity.org/blog/2009/06/16/stop-the-madness-cloud-onboarding-audits-an-open-question.html)
  * [Incomplete Thought: The Crushing Costs of Complying With Cloud Customer “Right To Audit” Clauses](http://www.rationalsurvivability.com/blog/?p=877)
  
Those articles make for a very good read (_wait_, don't do that, stay here, keep reading). Those articles were a realistic slap in the face that brought me down to earth. No one was going to solve this for me.

But, those articles were approximately one year old. A lot can happen in one year, especially in cloud computing. Perhaps I would find a flicker of light at the end of the tunnel...

I then came across some promising initiatives. _Happy days!_

## Cloud Security Alliance

The [Cloud Security Alliance](http://www.cloudsecurityalliance.org/About.html) are a non-profit organisation that document issues, best practices, and guides for cloud security. They have some very handy [research](http://www.cloudsecurityalliance.org/Research.html). The most relevant appears to be their [Security Guidance](http://www.cloudsecurityalliance.org/guidance.html) document and their [Controls Matrix](http://www.cloudsecurityalliance.org/cm.html) spreadsheet.

Be warned: _the CSA's Security Guidance document definitely does not make for light reading!_

After reading it I realised there was more to consider than I originally thought I needed to consider. Unfortunately, that left me with the strange sense that I had somehow taken a step backward, albeit a much more enlightened, informed step backward.

The CSA's Security Guidance document was clearly aimed at me (and a bunch of other people that I'm hoping will read my blog). At the end, though, I wasn't sure where to tread next.

I took a look at their Controls Matrix spreadsheet. _Ooh, a questionnaire!_ 100 rows. 13 columns. I spotted PCI DSS and ISO 27002 and got very excited!  _This was more like it!_

My only concern...

Is any cloud service provider going to take the time to respond to a prospect that shoves this hefty questionnaire under their nose? Surely the large guys wouldn't care? Surely the small guys are so busy innovating and evolving they wouldn't dare pin down a staff member to fill it out? Perhaps someone else, someone bigger, someone with more clout has already questioned cloud service providers and collated the results?

I went back to the CSA's research page. Bottom-left corner.  [CloudAudit](http://cloudaudit.org/). Promising name.

## Cloud Audit (A6)

The blurb for [CloudAudit](http://cloudaudit.org/) states:

> The goal [...] is to [...] automate the Audit, Assertion, Assessment, and Assurance (A6) of their infrastructure (IaaS), platform (PaaS), and application (SaaS) environments

Nice. Promising.

CloudAudit appears to be relatively young. It was started in January 2010.

The site is light on content at the moment. Based on their [about page](http://cloudaudit.org/page3/page3.html), their [FAQ](http://cloudaudit.org/page4/page4.html), and their [Google Group](http://groups.google.com/group/cloudaudit) it seems like they're at the stage of being a working group, "ratifying namespaces", and contributing to the CSA's Compliance Controls Matrix (see above).

I did notice that the [latest post](http://groups.google.com/group/cloudaudit/browse_thread/thread/a82bd2ff785aab67) in the Google Group mentions that they are getting ready to announce their "assembled v1.0 package". I'm not sure what that is, but it sounds good!

My guess is that this namespace ("which essentially looks like a directory structure") might be something like an LDAP directory that refers to relevant PCI DSS, NIST, COBIT, etc compliance. So a cloud service provider might have attributes that refer to DSNs in PCI DSS and ISO 27002 but not in NIST 800-53.  If that turns out to be the case and the "assembled v1.0 package" is a first cut of that structure, I assume it will then need to be populated with data, and then someone will need to mine that data to turn it into information.

Yes, it sounds promising, but it also sounds a bit further into the future than I can wait right now.

## Summary... for now

So far my research paints the following picture:

  * everyone is eager to audit their cloud service providers (more so than ye olde data centres)
  * there isn't (yet) an industry accepted standard for this
  * the large cloud service providers are going nuts with certification
  * the small guys are reusing the services of the large guys, citing their certifications, and claiming kudos by association
  * CloudAudit might be the beginning of the answer...
  
I can't leave it at that. _I don't want to be the guy who has to write these damn questionnaires!_ So I've sent off some e-mail queries and will hopefully follow up with some awesome news in a future post.

Stay tuned...
