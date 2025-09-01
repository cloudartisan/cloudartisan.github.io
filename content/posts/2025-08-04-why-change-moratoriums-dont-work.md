---
title: "Why Change Moratoriums Don't Work"
date: 2025-08-04T21:30:00+10:00
draft: false
description: "An examination of why freezing deployments during incidents creates more problems than it solves, and what actually works instead."
tags: ["DevOps", "Software Development", "Release Management", "Incident Response", "Continuous Delivery"]
categories: ["Development"]
---

I've been in this situation more times than I'd care to count: production is unstable, customers are unhappy, and leadership decides the solution is to freeze all changes until further notice. On the surface, it makes perfect sense. If changes are causing problems, stop making changes, right?

Wrong!

I understand the logic. I understand why executives think they should make this call. They assess the business impact of continuing with potentially risky changes versus grinding everything to a halt.

But I've learned from experience that change moratoriums, while well-intentioned, often create more problems than they solve.

## The Backlog Problem

When deployments freeze, all those changes that were ready don't just disappear, they pile up. Instead of incremental changes in isolation, you eventually end up with massive, unwieldy releases combining weeks or months of work. This creates a dangerous situation where:

1. **Production still breaks.** Even with minimal changes and extra scrutiny, incidents still occur. The freeze doesn't eliminate fundamental issues.

2. **Post-freeze releases become disasters.** Accumulated changes create complexity, they're difficult to test, risky to deploy, and impossible to tease apart.

## Stability Through Stagnation Doesn't Work

The common justification for moratoriums is that customers need stability. But here's the thing: stability isn't achieved through lack of change. In fact, the opposite. There's a reason why any DevOps team worth their salt prioritises a rapid CI and CD feedback loop...

By freezing releases, you're not just delaying new features, you're also delaying security patches, performance improvements, and bug fixes. You might actually be increasing the risk of known issues impacting customers. You're also increasing the difficulty of pulling forward a high priority change that has been made following but based on a sequence of other, lesser priority changes.

## The Maths Tells a Different Story

In my experience, most changes do more good than harm. Yes, occasionally you'll have a bad release that causes major customer impact. Those tend to stick in everyone's memory. But what about the previous 1,000 changes? When a bad enough release occurs (or a few cluster near enough together) everyone tends to fall into the Recency Bias hole.

I've seen environments where the actual failure rate of changes was around 2%, and the customer-impacting failure rate was closer to 0.2%. Those are actually pretty respectable numbers. The real issue isn't the frequency of failures, it's how quickly you can detect and recover from them.

If you can recover from incidents faster, potentially before customers even notice, you're in a much better position than if you slow everything down to a crawl. And that, my friends, requires moving in the opposite direction of a change moratorium.

## Moratoriums Don't Address Root Causes

Here's the fundamental problem: deciding to freeze changes doesn't actually fix anything. The underlying issues that caused the incidents are still there. After the moratorium period ends, you're right back where you started, unless you've used that time to fundamentally change how you operate.

But in my experience, that rarely happens. Teams spend the moratorium period in a holding pattern, increasing the backlog of changes that need to go out, and when the moratorium lifts, they go back to the same processes that created the problems in the first place. Just with less customer and executive scrutiny.

## Executive Bottlenecks

I've seen moratoriums where every change had to be personally approved by an EVP. This creates an unnecessary bottleneck. If the executive is travelling or unavailable, critical work stops entirely.

More importantly, it suggests a fundamental breakdown in trust. If you can't trust your engineering teams and managers to make good decisions about changes, you have bigger problems than a moratorium can solve. You have a lack of trust in your engineers and your engineers are highly aware of it.

## What Actually Works

Instead of freezing everything, here are approaches I've seen work better:

### 1. Fix the Release Process

If your release process is so broken that people skip reviews or can't follow it properly, that's your real problem. Build a lean process that enables engineers to deploy their own code safely, without armies of spreadsheets and manual gates. Continuous integration testing should be comprehensive, it shouldn't require any manual involvement, and it should seamlessly gate the release process.

### 2. Improve Observability and Understanding

Engineers need to understand the potential side effects of their changes. If your team doesn't have a solid understanding of your infrastructure, they can't fully assess the impact of their changes. If they're just throwing changes over the deployment wall, but those changes are impacting performance, scale, etc there's a disconnect that needs to be addressed.

### 3. Implement Real Accountability

Make engineers responsible for their changes in production. If someone deploys code that breaks at 3 AM, they should be the one getting woken up to fix it. This creates natural incentives for more careful development and testing. This requires making the unit of release far smaller and making it clear what change and where (e.g., logging the Git SHA) led to the breakage.

### 4. Address Cultural Issues

I've seen environments where people become complacent or believe that speaking up won't make a difference. When basic requests for access or proper test environments go unfulfilled, when code reviews become a demand for a "stamp of approval," when changes are by mandate or authority and not by consensus, this creates a culture where people stop caring about excellence.

### 5. Focus on Effectiveness, Not Just Productivity

Don't just measure how many PRs get merged, how many issues get closed, measure whether you're shipping the _right_ features and whether they're working correctly in production, measure time-to-market for features from a customer PoV, measure customer satisfaction. And, if you're going to measure productivity, do it with the involvement of engineers; management, more often than not, picks the wrong measures for productivity and risks incentivising the very thing that may have led to the last moratorium (e.g., rate of PR closure, lines of code, etc).

### 6. Be Transparent

Engineers want to do good work, but if they're left in the dark about what's happening or why decisions are made, it becomes demoralising.

## Moving Forward

The cloud-native world of SaaS, PaaS, etc demands a different approach to change management. You can't achieve the reliability and agility modern businesses need through periodic freezes and heavyweight processes.

Instead, invest in the practices that actually improve stability: better testing, faster feedback loops, improved observability, and a culture that values both velocity _and_ reliability.

I've been through enough incident-driven moratoriums to know they feel like the right response in the moment. But if you want to build truly reliable systems, you need to resist the urge to freeze and instead focus on the fundamentals that actually prevent such problems from occurring in the first place.
