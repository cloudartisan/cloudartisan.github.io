---
title: "Why Change Moratoriums Don't Work"
date: 2025-08-04T21:30:00+10:00
draft: false
description: "A critical examination of why freezing deployments during incidents creates more problems than it solves, and what actually works instead."
tags: ["DevOps", "Software Development", "Release Management", "Incident Response", "Continuous Delivery"]
categories: ["Development"]
---

I've been in this situation more times than I'd care to count: production is unstable, customers are unhappy, and leadership decides the solution is to freeze all changes until further notice. On the surface, it makes perfect sense – if changes are causing problems, stop making changes, right?

I understand the logic. I even understand why executives make this call – they're in the best position to assess the business impact of continuing with potentially risky changes versus grinding everything to a halt.

But I've learned from experience that change moratoriums, while well-intentioned, often create more problems than they solve.

## The Backlog Problem

Here's what actually happens when you freeze deployments: all those changes that were ready to go don't just disappear. They pile up, waiting for the moratorium to lift. Instead of deploying incremental changes in isolation, you end up with massive, unwieldy releases that combine weeks or months of work.

I witnessed this firsthand during my time at Amazon. We used to do release freezes for about six weeks over the holidays – only critical bugs could go out, and only after extensive review. Two things consistently happened:

1. **We still broke production.** Even with minimal changes and extra scrutiny, incidents still occurred. The freeze didn't eliminate the fundamental issues.

2. **Post-freeze releases were disasters.** I remember one year we had nearly 400 changes in a single release (we were used to about 15). That release was attempted and rolled back three times before it finally succeeded.

Amazon eventually moved away from release freezes entirely, adopting continuous delivery instead. When I left, changes were flowing to production roughly 10 times per day, and production defects were trending downward.

## Stability Through Stagnation Doesn't Work

The common justification for moratoriums is that customers need stability. But here's the thing: stability isn't achieved through lack of change. In fact, the opposite might be true.

By freezing releases, you're not just delaying new features – you're also delaying security patches, performance improvements, and bug fixes. You might actually be increasing the risk of known issues impacting customers.

## The Math Tells a Different Story

In my experience, most changes do more good than harm. Yes, occasionally you'll have a bad release that causes major customer impact – those stick in everyone's memory. But what about the previous 1,000 changes?

I've seen environments where the actual failure rate of changes was around 2%, and the customer-impacting failure rate was closer to 0.2%. Those are actually pretty respectable numbers. The real issue isn't the frequency of failures – it's how quickly you can detect and recover from them.

If you can recover from incidents faster, potentially before customers even notice, you're in a much better position than if you slow everything down to a crawl.

## Moratoriums Don't Address Root Causes

Here's the fundamental problem: deciding to freeze changes doesn't actually fix anything. The underlying issues that caused the incidents are still there. After the moratorium period ends, you're right back where you started – unless you've used that time to fundamentally change how you operate.

But in my experience, that rarely happens. Teams spend the moratorium period in a holding pattern, and when it lifts, they go back to the same processes that created the problems in the first place.

## Executive Bottlenecks

I've seen moratoriums where every change had to be personally approved by the CEO or CTO. This creates an unnecessary bottleneck – if the executive is travelling or unavailable, critical work stops entirely.

More importantly, it suggests a fundamental breakdown in trust. If you can't trust your engineering teams and managers to make good decisions about changes, you have bigger problems than a moratorium can solve.

## What Actually Works

Instead of freezing everything, here are approaches I've seen work better:

### 1. Fix the Release Process

If your release process is so broken that people skip reviews or can't follow it properly, that's your real problem. Build a lean process that enables engineers to deploy their own code safely, without armies of spreadsheets and manual gates.

### 2. Improve Observability and Understanding

Engineers need to understand the potential side effects of their changes. If your team doesn't have a solid understanding of your infrastructure, they can't fully assess the impact of their changes.

### 3. Implement Real Accountability

Make engineers responsible for their changes in production. If someone deploys code that breaks at 3 AM, they should be the one getting woken up to fix it. This creates natural incentives for more careful development and testing.

### 4. Address Cultural Issues

I've seen environments where people become complacent or believe that speaking up won't make a difference. When basic requests like read-only production access or proper test environments go unfulfilled for years, it creates a culture where people stop caring about excellence.

### 5. Focus on Effectiveness, Not Just Productivity

Don't just measure how many features you ship – measure whether you're shipping the right features and whether they're working correctly in production.

### 6. Be Transparent

Engineers want to do good work, but if they're left in the dark about what's happening or why decisions are made, it becomes demoralising.

## Moving Forward

The cloud-native world demands a different approach to change management. You can't achieve the reliability and agility modern businesses need through periodic freezes and heavyweight processes.

Instead, invest in the practices that actually improve stability: better testing, faster feedback loops, improved observability, and a culture that values both velocity and reliability.

I've been through enough incident-driven moratoriums to know they feel like the right response in the moment. But if you want to build truly reliable systems, you need to resist the urge to freeze and instead focus on the fundamentals that actually prevent problems from occurring in the first place.

*Have you experienced change moratoriums in your organisation? I'd love to hear about your experiences – both the good and the frustrating.*