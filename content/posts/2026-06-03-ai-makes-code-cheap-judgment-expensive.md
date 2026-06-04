---
title: "AI Makes Code Cheap. Judgment Stays Expensive."
date: 2026-06-04T13:07:37+10:00
draft: false
description: "Why the benefits of AI coding tools in corporate environments are often local to the producer, while the hidden costs are pushed onto reviewers, senior engineers, and the future hiring pipeline."
tags: ["AI", "LLMs", "Software Engineering", "Engineering Management", "Code Review", "DevOps", "Governance"]
categories: ["Development"]
author: "david-taylor"
---

There is a version of the AI coding story that absolutely kills in a boardroom.

Engineers can produce code faster. Boilerplate gets cheaper. Ticket throughput goes up. Junior engineers can supposedly do more with less support. Maybe leadership even convinces itself that fewer engineers are needed overall.

I think that story is wrong. Or at least wrong enough to make expensive decisions with false confidence.

The part that interests me is the asymmetry.

AI coding tools create real local gains for the person producing the draft. They can absolutely help with blank-page friction, repetitive edits, rough scaffolding, and bounded implementation work. But the costs do not land in the same place as the benefits. In a corporate environment, a surprising amount of that cost gets pushed downstream onto reviewers, senior engineers, maintainers, and whoever is still on the hook when something breaks in production.

That is the bit I think many companies are still getting badly wrong.

## The upside is real

I don't think it's useful to pretend these tools have no value.

GitHub's own [Copilot research](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) reported faster completion on a bounded task, along with less frustration and better flow.

![GitHub Copilot bounded-task study: task time and completion rate](/images/2026/06/chart_github_copilot_bounded_task.svg)
*Source: [GitHub research blog](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/). A constrained coding task: Copilot users averaged 71 minutes versus 161 minutes for the control group. GitHub summarises this as 55% faster. The real question is what happens when the task isn't constrained.*

[Stack Overflow's 2024 developer survey](https://survey.stackoverflow.co/2024/ai/) showed that most developers still see productivity as the main hoped-for benefit of AI tooling.

None of that is hard to believe.

![Why developers use AI tools: Stack Overflow Developer Survey 2024](/images/2026/06/chart_stackoverflow_2024_ai_benefits.svg)
*Source: [Stack Overflow Developer Survey 2024, AI section](https://survey.stackoverflow.co/2024/ai/)*

Modern coding assistants can be genuinely useful for:

- reducing boilerplate
- sketching first drafts
- filling in repetitive test cases
- translating intent into rough implementation quickly
- helping people get unstuck when the problem is narrow enough

That is why adoption keeps happening. The gains are visible, immediate, and easy to show on a slide.

The problem is that those are not the only costs that matter.

## Draft code is cheap. Trusted judgment is not.

This is the strongest way I can put it.

AI lowers the cost of producing draft code. It does not lower the cost of being responsible for code in production.

That distinction matters more in large organisations than it does in toy demos of vibe-coded Electron slop.

In a real corporate environment, code does not become valuable because it exists. It becomes valuable because someone has to decide that it is safe enough, coherent enough, compliant enough, maintainable enough, and understandable enough to merge, deploy, and own.

That work does not disappear just because the first draft arrived faster.

If anything, it becomes more important.

Because once code generation gets cheap, the bottleneck shifts.

Not to writing.

To judgment.

## The hidden tax is review

This is where I think the asymmetry becomes obvious.

If one engineer can now generate three times as many plausible pull requests, the organisation does not magically get three times as much review capacity, architectural attention, operational understanding, or incident response maturity.

What it gets is more stuff that *looks* finished.

And that is not the same thing.

GitHub has been unusually direct about this in its own recent writing. It has acknowledged that the [agentic shift brings more context switching and too much time spent reviewing agent-generated code](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/). It has also warned that [agent-generated pull requests can be easy to approve for exactly the wrong reasons](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/): they often look clean, pass basic checks, and feel oddly frictionless.

That ease is exactly the trap.

The hardest review work is rarely syntax, formatting, or whether the code compiles. It's whether the change actually makes sense in the local system. Whether it duplicates something that already exists. Whether it introduces subtle operational risk. Whether the migration path is sane. Whether the rollback story is clear. Whether the engineer who raised the PR understands the failure mode well enough to own it later.

I don't have to imagine this in the abstract. I've watched colleagues raise huge AI-assisted pull requests that were obviously generated faster than they were understood. In one case, a coworker spent more than half a day trying to review an AI-generated PR of well over a thousand lines before giving up and rewriting the thing properly. That's review debt, billed directly to the person with enough judgment to recognise the mess.

I've also noticed that AI slop has a recognisable smell now. Long-winded paragraphs. Mixed formatting. Strange fragments that don't quite connect. Links pasted in as "evidence" that don't actually support the claim. After enough exposure, a ticket stops reading like a good-faith technical summary and starts reading like forensic cleanup.

AI can help generate the code, but it can't take legal, operational, or professional responsibility for it.

So the burden moves uphill.

## Why senior engineers end up carrying the cost

This is where the labour side of the story matters.

When companies adopt AI coding tools aggressively, they often talk as if they are reducing effort. In reality, they may just be changing whose effort counts.

The more generated code a team can produce, the more it needs people who can:

- assess architecture fit
- spot false confidence in plausible-looking output
- validate security and compliance implications
- evaluate production blast radius
- debug failures when the generated code is subtly wrong
- keep the codebase coherent over time
- decide what should never have been merged in the first place

Those duties are not evenly distributed. They concentrate on senior engineers, staff engineers, leads, principals, maintainers, and on-call operators.

A lot of this extra labour arrives disguised as "findings". I've worked incidents where the investigation got materially slower because an AI-generated summary had hallucinated a link between unrelated systems, and then I had to unwind that false premise across code, logs, and service boundaries. I can think of one investigation that sent me digging across roughly a dozen repositories and their logs partly because the original AI-assisted diagnosis had pointed blame in the wrong direction. Again: the model got to be fast. The humans got to be careful.

There is also a more corrosive version of the same problem: technical conversations with people get replaced by technical conversations with model output, relayed by a human proxy who doesn't properly understand it. If I see "Sent using @Slack MCP App" on a message from you to me, I will *not* read it. That is a miserable way to run an engineering organisation.

This is why I don't buy the simplistic "AI means fewer engineers" line.

The more interesting question is not whether companies need fewer people typing code. It's whether they are about to need even more of the people whose judgment they already can't scale easily.

That is a very different kind of scarcity.

## Faster generation != faster engineering

This is another place where the public conversation gets sloppy.

There is a big difference between measuring speed on a constrained task and measuring throughput inside a real system with real context, legacy constraints, and production responsibility.

One of the most interesting counterweights to the hype is [METR's 2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) of experienced open-source developers working on real issues in their own repositories. In that study, the developers using AI tools took longer, not less time. They still believed the tools had made them faster.

![AI felt faster. It was slower. METR study of experienced open-source developers (2025)](/images/2026/06/chart_metr_2025_perception_vs_reality.svg)
*Source: [METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Developers expected AI to speed them up by 24%. It slowed them down by 19%. Afterwards, they still believed it had sped them up by 20%.*

That finding should make a few leadership decks much harder to write.

It also lines up uncomfortably well with what I've seen inside large engineering organisations. The pattern is familiar: AI usage and spend rise quickly, overall delivery metrics barely move, and pull request cycle time can even get worse. The consequence is not mysterious. If AI increases PR volume, review capacity has to increase with it. For a lot of senior engineers, that's already the day job.

It suggests that AI can feel productive while still increasing hidden work elsewhere. You can save time on draft generation and lose it again in review, rework, debugging, integration, and clean-up.

That would explain a lot about the current mood in engineering teams.

People feel busier. More code is moving around. More things look nearly done. Yet the overall experience does not always feel cleaner, calmer, or more trustworthy.

## The outage angle is really a governance angle

This is where the recent reporting gets interesting.

AI-assisted development appears to be making it easier to create production risk faster than organisations can improve the guard rails around review, rollback, blast radius, risk ownership, and governance.

Take the recent Amazon reporting. The public coverage around AWS outages and internal follow-up has been messy, and Amazon has pushed back on simple claims that AI coding tools directly caused the incidents. GeekWire covered that pushback directly, while Tom's Hardware reported the internal response in more operational terms. Fair enough.

But even with that caveat, the reporting still shows that if AI-assisted changes are implicated often enough to trigger internal meetings, tighter approvals, and more senior attention, then the story is not really about magical productivity. It is about governance strain.

I've seen the smaller-scale version of that problem up close. In one review cycle, an AI-assisted security finding was filed with enough authority to block release, despite describing a scenario that should have been ruled out immediately by the underlying system model. It was later acknowledged as reviewer oversight. But by then the damage was already done: time lost, confidence shaken, and accurate documentation treated as suspect because the false claim arrived wrapped in synthetic certainty.

I also caught a release candidate carrying an AI-generated change that would have disabled a live production service, complete with a confident but fabricated rationale in the commit message. That is the part many of the optimistic AI narratives skip over. The outage often does not happen because the model is clever. It nearly happens because the explanation sounds tidy enough to slide through.

The same pattern shows up in smaller, more vivid incidents as well.

The PocketOS incident involving Cursor and Claude is a good example. The reporting in The New Stack and The Register describes an agent deleting production data with customer impact. What matters is how quickly plausible autonomous action can outrun review, rollback discipline, and basic blast-radius control.

These stories are not all equal. Some are stronger than others. Some rely more heavily on founder accounts than formal postmortems. Some involve disputed causation.

But they all point in a similar direction.

The risk is not just that AI can write bad code confidently.

The risk is that AI makes it cheap to create changes that look good enough to move forward before the organisation has really solved the questions that matter:

- who reviewed this properly?
- who understands the blast radius?
- who validates the rollback path?
- who signs off on the risk?
- who gets paged if it goes wrong?

That's a governance problem.

## The pricing model reinforces the same asymmetry

In the current published pricing for the major providers, output is generally more expensive than input.

But the asymmetry is still there. It shows up somewhere else.

Vendors get paid for generated work, model-side processing, premium latency, search grounding, cache storage, long context, and other metered services around the model. Buyers are then pushed to manage those costs through batching, caching, prompt reuse, shorter outputs, and tighter controls around usage.

But the pricing asymmetry is...

The vendor gets paid once when the model generates the work. The buyer pays a second time when human beings have to validate it, integrate it, operate it, and take responsibility for it.

That second bill never shows up on the pricing page. It's often the more expensive one.

## Layoffs: the most visible form of the same asymmetry

This is where the argument stops being abstract.

Klarna's CEO publicly stated that the company's AI tools had replaced the equivalent of 700 customer service workers, and later [reportedly said he wanted some of those people back](https://news.google.com/rss/articles/CBMihgFBVV95cUxOU3h4SzFLWC1wcDlGTkZxajFTYUMtVEdFRnN0LWRaUzZVVnhuLVBFbFFmZ21ULUxjbzdlQWpuOUlnbGI0X3Q4RjREQUZCcC1BWnZvR1hpUzJIaVA4dDNNV1RUZGp2Q2xfaHlRQ1lSZWh2a0FYSzBOZ0pkNUxzTmx6VUt2MUJCdw?oc=5) because the quality of customer interactions had slipped. In early 2025, [Duolingo announced an "AI-first" policy](https://news.google.com/rss/articles/CBMimAFBVV95cUxNU21xSjgyMXNWUm1acklMajYxOWxZaE51SF9aUzltVXdpNmtxaFlyd0NQUloxc05hTWtxYnRLNHVBMHM5bjRhbU10Q082eURJeFNhUW5mRHBEamxCTHVVYkZxUmN4T01rSmdWRndKdEF3U2dhQncyNTJneFh2ZW9nR0s1RWZHZEhiOWhSTTZVOExwb2NUS3QwRw?oc=5), stating that contractor roles would no longer be renewed where AI could do the work instead. CNBC reported that AI was [cited in more than 50,000 layoffs in 2025 alone](https://news.google.com/rss/articles/CBMioAFBVV95cUxNUjZpVUFOVmJ4UllaQ2h6YXlHRzVzdlRGd0paUXFrWms4alBmTlpuN3BfbmduUUphSC1SMjR1aVB3T0FaWE9yZGN6WjRVZFBRdWZPZUVvVnJwYURpMk12Z1lVeDViWkZGWWU1UjhjdldISFNSSEVJWk45VTBQVXdmTE5zaDhwc2g3YkZiU0pVTF94MEpmT2N1ZlhRUktjaWpw0gGmAUFVX3lxTE5vNjZwczBfbi1scnNRb2VVODlTOHRWUV9rSHlRSGpnLWlIUVdzODVva0dOSW5HbzhuZHBhRWhYVHVCck1VUXNYODZYQ1pxSkJyaEJOQjIybmZONHIwXzJYMGFocWcwWlB1Z2l6aTYyZHBJWlpFUWxlWGh5UTlDcDRhYVpsVTVxRnBZNHZuYmF5V2EwOWJ0TVlIcEFjV29yaU1ZRVBtV0E?oc=5).

These are not all software engineering roles, and the attribution is not always clean. But the pattern is consistent enough to take seriously.

The asymmetry is on full display. The savings land on this quarter's headcount report. The costs are deferred into a future that is harder to point to in an earnings call.

For software engineering specifically, the most consequential version of this is not the headline layoff. It is the slower, quieter decision not to backfill junior roles.

## The junior engineer problem may be the most serious long-term cost

There is another asymmetry here that plays out even more slowly.

If companies decide that AI lets them skip a generation of junior hires, they may save money in the short term while quietly damaging the system that produces future seniors.

That worries me more than most of the productivity claims do.

A lot of engineering judgment is not learned by consuming explanations. It is learned by doing real work, making manageable mistakes, being reviewed by more experienced engineers, and gradually taking on more responsibility.

If entry-level work becomes "cheap to automate" before junior engineers have had a chance to learn from doing it, the organisation may be liquidating its own apprenticeship model.

The Klarna story is instructive here. Replacing a customer service workforce with AI and then discovering the quality has slipped is not a story about AI failing. It is a story about losing the institutional capacity to do the work at all, and then realising the cost of rebuilding it.

Engineering organisations run that same risk on a slower timescale.

Again, the asymmetry is clear.

The savings are immediate.

The capability loss shows up later.

## What companies should be asking instead

If I were framing this for an engineering leadership team, I would not start with "How much faster can AI help us ship?"

I'd start with harder questions.

- Do we have enough review capacity for the amount of code these tools let people generate?
- Are our senior engineers now carrying a larger invisible tax in validation and clean-up?
- Are we measuring throughput while ignoring rework, code churn, and incident risk?
- Have we improved rollback and blast-radius controls at the same pace as generation speed?
- Are we shrinking the junior funnel because the spreadsheet says we can?
- Who still owns the consequences when the generated change is wrong?

Those questions are less fun than a vibe-coded demo, but *much* more useful.

They are also much closer to the real organisational problem.

## My take

I don't think AI coding tools are a fad, and I don't think the answer is to ban them.

I also don't think the problem is AI per se. On my own projects, where I understand the domain, verify the output, and bear the consequences directly, these tools can be genuinely useful. They help me move faster.

What I object to is the collaborative version where one person gets the local speed boost and someone else inherits the verification burden, the incident risk, the review fatigue, and the operational consequences.

I do think a lot of organisations are mistaking cheaper code generation for cheaper engineering.

They are not the same thing.

The immediate gains are often private to the author. The downstream risks are socialised to reviewers, maintainers, on-call engineers, and future hiring plans.

That is the asymmetry.

And until companies get serious about review capacity, operational guard rails, risk ownership, governance, and the junior-to-senior pipeline, I think they will keep discovering the same thing the hard way:

AI makes code cheap.

Judgment stays expensive.

## References

- GitHub, [Research: quantifying GitHub Copilot's impact on developer productivity and happiness](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
- Stack Overflow, [2024 Developer Survey: AI](https://survey.stackoverflow.co/2024/ai/)
- METR, [Early 2025 AI experienced open-source developer study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- GitHub, [GitHub Copilot app: The agent-native desktop experience](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/)
- GitHub, [Agent pull requests are everywhere. Here's how to review them.](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/)
- GeekWire, [Amazon pushes back on Financial Times report blaming AI coding tools for AWS outages](https://www.geekwire.com/2026/amazon-pushes-back-on-financial-times-report-blaming-ai-coding-tools-for-aws-outages/)
- Tom's Hardware, [In wake of outage, Amazon calls upon senior engineers to address issues created by 'Gen-AI assisted changes,' report claims](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-calls-engineers-to-address-issues-caused-by-use-of-ai-tools-report-claims-company-says-recent-incidents-had-high-blast-radius-and-were-allegedly-related-to-gen-ai-assisted-changes)
- The New Stack, [How a Cursor AI agent wiped PocketOS’s production database in under 10 seconds](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9YN0xsRU9CcnVOb3hINkZyYUpVcTB5UDZkYzdFQ29XNi1USGoxSElxei1DdjFYbWlVaWxuRDg1OFZlbDJGOV9DTVk2Q2JLTHFRNmR2UUI4WlQ1aUpTOXZkNw?oc=5)
- The Register, [Cursor-Opus agent snuffs out startup’s production database](https://news.google.com/rss/articles/CBMiswFBVV95cUxPbE9vN3RMeC1TeUFHR1VEbkd3SVRpYVVBcUtJMlVjNUpVR2xaQzlkQVBDRHBHeExobU1WcF9MYzNod25tZmNZN3lXUnZwbW55R1p5WnhpWlN5NU53bVhlX0NvNW1KX19IU0NmenZVWUJISnlNQkdqUXZkUFNvZ09IXy12Y2c4VGtqTmtfX0tUNElnb0xweUZuSWlhSWVJNDNFbUFzbTBpZHdPMlNlYjNlTUFEbw?oc=5)
