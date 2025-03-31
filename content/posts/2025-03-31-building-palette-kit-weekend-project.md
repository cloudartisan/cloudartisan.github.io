---
title: "Building Palette Kit: From Zero to Production in a Weekend"
date: 2025-03-31
draft: false
slug: building-palette-kit-weekend-project
tags: ["project", "development", "art", "coloured pencils", "lovable", "OpenAI", "Cloudflare"]
description: "How a phone call with my sister led to building Palette Kit, a tool for coloured pencil artists, in a single weekend using modern development tools and AI assistance."
---

So I built [Palette Kit](https://palettekit.com) over the weekend. The whole thing, start to finish: from zero lines of code to a published site.

## The Spark

It began with a phone call with my sister. She runs [My Colourful Country Life](https://www.mycolourfulcountrylife.com/), a site for adult colouring enthusiasts. As my sister explained the value of her PDFs for artists, I realised it'd translate VERY well into an application with search and other features.

My sister spends ages testing different pencil combinations for her artwork. There are tons of brands and colours out there, and finding good combinations for blending and creating depth takes a lot of time and expertise. Her hard work could save a lot of time for a lot of people.

## The Weekend Challenge

So I thought, what if I build this thing in a weekend? Just to see if I could. I grabbed my toolbox of modern dev tools--Lovable, OpenAI, Cursor, GitHub, and Cloudflare--and got to work.

## The Data Layer

First up: data. I poked around with my sister's PDFs to see if I could extract colour info from them. Turns out, yep! I whipped up some Python scripts to generate JSON files with all the pencil brands, names, and their hex/RGB codes.

I kept it dead simple--no fancy database, just some JSON files. Quick and dirty, but it did the job for a weekend project.

## The User Interface

For the UI, I took the lazy (ahem, "efficient") approach:
1. Browsed Figma for designs I liked
2. Found some nice Shadcn components that would work
3. Had OpenAI help me write a PRD because I couldn't be bothered to write all the details

Then I just dumped the PRD, Figma designs, and component picks into Lovable (an AI dev platform). First try, it spit out a working landing page with search. Not too shabby!

## Fine-Tuning

The workflow was actually pretty sweet:
1. Hooked Lovable to my GitHub account
2. Made tweaks in Cursor/GitHub and they showed up in Lovable instantly
3. Could see changes in real-time without any deploy nonsense

For the pretty pictures, I just asked OpenAI to generate the pencil image for the hero section and the logo. Way faster than hiring a designer!

## Deployment

Getting it online was ridiculously easy:
1. Bought palettekit.com from Cloudflare for ten bucks
2. Hit "Publish" in Lovable and typed in my domain
3. Lovable detected Cloudflare and set up all the DNS stuff automatically

Boom. Live website.

## The Result

Right now, Palette Kit does three things:
- **Colour Combination Database**: Find combos that actually work
- **Favourites**: Save your go-to combinations
- **Wishlist**: Keep track of pencils you want to buy

### Search by Colour Family
![Search by Colour Family](/images/projects/palettekit/search-colour-family.png)

### Colour Details
![Colour Details](/images/projects/palettekit/colour-details.png)

### Favourites
![Favourites](/images/projects/palettekit/favourites.png)

## What's Next

I've got some ideas brewing for future stuff:
- User accounts so you can save your stuff
- Sharing combos with other artists
- Visual examples of what combinations look like in real artwork
- Finding equivalent colours across different pencil brands
- Custom palettes for specific projects

## The Takeaway

This whole experience was a reminder of how fast you can build stuff these days with AI tools. What would've taken weeks or months? Knocked it out in a weekend.

But the coolest part was taking my sister's specialised knowledge and turning it into something useful. Artists can spend more time creating and less time testing endless colour combinations.

Give [Palette Kit](https://palettekit.com) a try and let me know if it's useful!