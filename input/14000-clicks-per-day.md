---
h1: "14,000 Clicks per Day, Thanks to Programmatic SEO"
title: "14,000 Clicks per Day, Thanks to Programmatic SEO"
description: Learn how we scaled a content website to more than 14,000 visitors per day, all thanks to programmatic SEO.
date: "2023-03-18"
---

We have successfully scaled a content website to more than 14,000 visitors per day, all thanks to programmatic SEO. We started implementing the pSEO strategy on the site from August 2022, and you can see the results below.

![GSC Screenshot Growth](/img/blog/GSC-Screenshot-Growth.png)

A GSC screenshot showing 14,000 clicks in a day

I have been sharing the progress on Twitter and LinkedIn, but it’s time for a blog post with all the details (except for the domain name 😅).

Let’s take a look…

## The backstory

I started the website back in November 2018 and then manually wrote around 150 high-quality articles for the next 1–1.5 years. After that, I didn’t add or update even a single page on the site until August 2022 (when I implemented programmatic SEO on the site).

And without being consistently updated, the website was receiving around 40,000 monthly visitors before we started working on it again.

For your information, the website is in the education niche and high school & college students are the target audience.

## How we implemented programmatic SEO

If you are reading this post, then I would assume that you have a basic understanding of what programmatic SEO is and how it works. And now I will get directly to the point…

### Keywords research

I went through the existing Google Search Console data and tried finding some queries that people are searching for and that can be suitable for programmatic SEO. Of course, it was a manual task, but I ended up getting 2 solid keywords from there.

And I did use SEMrush, Lowfruits, ChatGPT, and some students’ books to find out all the possible combinations of the keywords. There is no fixed process though, I just kept looking and found numerous possible combinations.

For example, let’s say I got the keyword “can dogs eat banana?” then you can see that “banana” here can be easily replaced by other food items. And it’s a solid programmatic SEO-friendly keyword “can dogs eat {food}?” where food items can be bread, apple, honey, chicken, etc.

### Tech-stack used

I used the WP All Import WordPress plugin for this (check the Programmatic SEO with WordPress guide) and here’s the complete tech stack of the programmatic setup:

- WP All Import Pro (WordPress plugin)

- WP All Import - Rank Math SEO Add-On (WordPress plugin for SEO of programmatically generated pages)

- Google Sheets (for collecting, organizing, and using as the database for the programmatic setup)

And some custom Google Apps Script for handling images (I uploaded all images to Imgur via their API, and then they easily get imported into WordPress while running the import).

### The setup

All the required data points, formula to create slugs, related posts, etc. are being managed and organized in Google Sheets. I can’t share the actual document, but here’s an example of Google Sheets being used to create the programmatic SEO example section.

![Sample Google Sheets Example](/img/blog/Sample-Google-Sheets-Example.png)

Click here to see the Google Sheets.

Super detailed and insightful, isn’t it? I am sure you’ll get a lot of ideas from here.

On the actual Google Sheets of the site, there are more than 60 columns that I and Bikash add manually and have more than 500 rows of data. It does look tiring to manually collect that many rows of data, but it’s much better than manually publishing 500 posts.

And then creating the template was a complicated process, it took a lot of time. Again, I can’t show this site’s template, but here’s a screenshot of the page template that I used for pSEOos (before it was merged).

![pSEOos Page Template](/img/blog/pSEOos-Page-Template.png)

pSEO template from the examples section.

And this site’s page template looks mostly the same, just a bit longer and more detailed.

## Final words

I’d say that for a solid implementation of programmatic SEO on your website, you need to fully understand the core SEO principles. Programmatic SEO is not just about creating 100s of dynamic pages, but making those pages SEO-friendly and user-friendly as well.

For the site in question, I put extra effort to make sure all generated pages are of high quality and provide value to the readers.
