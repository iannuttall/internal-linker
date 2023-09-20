---
h1: " Find Programmatic SEO Datasets"
title: " Find Programmatic SEO Datasets"
date: "2022-08-27"
description: Find interesting data to use for programmatic builds by learning to look at keywords differently.
---
        


Data will make or break your programmatic SEO site. Bad data in = bad content out. I spend as long sourcing and compiling my data as I do writing the templates to display the data.

The three main sources of data for my projects are:

1. Publicly available data sets or APIs (e.g. government data, weather data, etc)

2. Scrape the data from a public website (either myself or hire a dev)

3. For smaller projects, you can manually collate data (or outsource to a Virtual Assistant)

[toc]

### Looking to learn programmatic SEO from scratch?

Check out the full course, that teaches you everything you need to get started building programmatic SEO projects - with code, no-code, or AI content.

View the programmatic SEO course &rarr;

## How I scrape public data

If I’m scraping the data myself, it typically takes me about 2 weeks to properly write the scraper scripts I need to get the data into a format I can import to a SQL database.

I don’t wanna get too technical in this post so I’m not going to deep dive into the actual process behind those scrapes. Maybe in a future blog post, I’ll show some examples of how I do this in Python.

Lately, I’ve been hiring developers on Upwork to scrape the data for me. The cost is typically $100-300 to scrape some pretty huge datasets (50k+ rows, multiple tables).

$100-300 is a no-brainer vs the time I waste trying to write my own. If you do outsource it, and you need the data updated from time to time, make sure they give you the code so you can automate it.

I have cron jobs running PHP and Python scripts that update my database automatically.

The TLDR is: scrape the data from public sites, APIs, or downloadable files **if you have the skills to do it**. If not, **it can be outsourced** very cheaply.

The bonus of hiring a scraper on Upwork is they often have the frameworks set up to scrape quickly, with access to proxies and ways to avoid detection, and can get you the data much quicker in a format that is ready to go.

## Outsourcing your data scraping

Upwork is full of quality scrapers in a variety of languages. Mostly, you’ll find Python and Java scrapers, but if you prefer PHP or JS, there are plenty of options and a lot of competition for scraping jobs.

My process for hiring a scraper is simple and pretty much the same kind of thought process as hiring a content writer for a blog post:

1.   Explain the brief clearly (i.e “I need the median US house price data by zip code from this URL/API. Each row should include the columns: zip.code, city, city.slug, state, state.slug, median.price, year.”)
2.   Provide an example CSV file with 2-3 rows of completed example data to show them the expected output.
3.   Explain what to do with missing or unexpected data. For example, if there is no median US house price estimate for a zip code (or the value is something weird like X), set it to -1. This way you can exclude those zips from the front end, or explain the reason for no data in the post.
4.   Iterate on the scrape by giving them feedback after reviewing the provided output.

For one-off data scrapes, I just ask for a CSV file. If the data source changes regularly, I’ll ask them to provide a script that will update a SQL database with any new or updated rows.

I can then use that script as a cron job on my server to continually check for new data. Again, you can hire a dev for that relatively cheaply.

Once I have the data, I can import the CSV to a MySQL database, and then start to build the URL routes and write the templates that will make the data useful to a site visitor.

But, you can only hire a scraper if you have an idea of the data you already want to scrape. So let’s look at some ways you can find data that works for programmatic SEO.

## Thinking about programmatic keywords

To find data that works well for programmatic SEO, you need to think outside the box and look at keywords differently.

Remember that with programmatic SEO we're looking for a way to create repeatable search queries. For example:

- What is the weather in `{place}`?

- What is the weather in `{place}` in `{month}`?

- What was the weather in `{place}` in `{month}` `{year}`?

This is where you need to get creative and think of keywords that have this repeatable format. Once you start seeing keywords through the repeatable lens, you’ll get lots of ideas for the type of data you want.

Governments often have a lot of readily available data and, because they are governments, the data is rarely in a format that is easily used. __This is a good thing__ because easy data sources are usually more competitive.

Here's a quick example. I wondered if the US gov had an open dataset on crime. A quick Google search shows that they do and there are programmatic sites using this data.

According to ahrefs there are a bunch of keywords with decent search traffic around `crime in {place}`:

![](/img/blog/find-programmatic-seo-datasets-1.png)

Maybe this will be too hard to rank for with big cities like Chicago, but the top result for “crime in san pedro” is a Facebook page, as is “crime in wilmington” so this tells me there is potential here for a programmatic site that targets crime in long tail locations.

Another interesting dataset from the US government that I planned to use at some point was to build a world climate website using data from the Global Surface Summary of the Day (GSOD). You can also focus purely on the US with U.S Climate Normals data if you prefer.

Weather and climate-based data are perfect for programmatic sites. Obviously, you can do a page for each location, i.e .average temperature in LA for August. but, once you have the database, you can do more interesting things like `hottest city in {location}`:

![](/img/blog/find-programmatic-seo-datasets-2.png)

These types of keywords work well for blog-style content where you can combine data, compare it with tables and charts, and internally link to your location pages as well.

For this example, you can find the hottest locations in a country, continent, city, or state. That’s a lot of pages targeting (and answering) specific search queries.

You’re not limited to one dataset either. In fact, it’s even better and more useful for visitors to combine multiple sources.

For example, what if you could find a database of average internet speeds by location? You could then create articles like `hottest city in {location} with fast internet` The possibilities are endless.

Pieter Levels does this like a boss with his filters on NomadList:

<https://nomadlist.com/mild-affordable-safe-places-in-united-states-with-fast-internet>

There is no magic trick for this, you just have to start looking at keywords on a bigger scale. Location-based keywords are obviously an easy one, but there are plenty of other ideas:

*   Vehicles (make, model, year, trim, etc)
*   Products (name, category, price, etc)
*   Animals (name, habitat, diet, lifespan, etc)
*   Units (convert cm -> km etc)
*   Puzzles (clues, answers, etc)

## 17 places to find data for your programmatic SEO sites

If you’re still struggling to find an idea for a programmatic SEO data source. Here’s a list of ways and places you might find some inspiration:

1.   Data.gov - a huge library of 335k+ open data sets from the US government. There’s a lot to browse through, but some really great and interesting options.
2.   Awesome Public Datasets - covers a huge variety of topics like agriculture, climate, education, finance, sport and transportation.
3.   ProgrammableWeb - 500+ different categories of API. For example, Statistics APIs.
4.   r/datasets - Reddit community with 163k members that find, share, request, and discuss datasets. A great example is a dataset of 10k book reviews from Goodreads.
5.   Kaggle - a very popular directory to explore, analyze and share top quality data.
6.   Github - There is a lot of data published on GitHub, which you can find using `site:github.com “{search.term}” + csv/database` For example: site:github.com "cruise ship" + csv finds this small list of cruise ship information
7.   Google Sheets - find datasets published in Google sheets using `site:docs.google.com/spreadsheets {search.term}`. For example: site:docs.google.com/spreadsheets "finance" turns up this list of car makers by market cap
8.   DoltHub - kinda like GitHub for SQL databases. Dolt offer bounties to crowd source large data sets that are made available through their platform. Like SHAQ, their open source database of basketball player and teams from leagues across the world.
9.   World Bank Open Data - 3000+ datasets covering topics like agriculture, climate, economy, energy, gender, health and more!
10.   data.world - claims to be the world’s largest collection of open data and has a lot of very interesting topics like this one which compares the size and intelligence of dogs to find out if there is a link between them. My personal favourite is the Bigfoot sightings database!
11.   Opendatasoft - A directory of 28k datasets that might help you find something new. I’ve had this Shark attack dataset in my “to-do” pile for some time!
12.   data.gov.uk - The UK government has a lot of data available across business, crime, government, society, transport and more. I know people building very nice and data-rich programmatic sites with these!
13.   Canada Open Data - what about Canada, eh? Like the US and UK, they have a huge library of open data covering most of the same categories.
14.   Datahub - another directory with some interesting sites like gas prices, airport codes and stock market data.
15.   USDA - the US Dept. of Agriculture have over 6k datasets, including the primary source of the WordPress programmatic SEO example I posted on Twitter.
16.   DataSN - There are some absolutely huge datasets here if you wanna go crazy with your programmatic SEO site. For example, this one has 7.2m rows of restaurant, bar, and pub data. Note, you'll need to pay a subscription for this data!
17.    Google - Sometimes browsing these huge directories is painful. If you have specific topics in mind, you can search `best {topic} datasets` to try and narrow things down. 

I could go on and list many more places to find data, but there is plenty in the above list to keep you going for a long time.

Once you get an idea of what is out there, you can start to think about _what might be out there_ and you can search for specific datasets around topics you’re interested in.

For example, let’s say you build a site about animals and have pages for each animal that cover habitat, diet, lifespan etc etc.

You can think about new data sets to enrich what you have. How about adding data on whether the animal farts or not, using this Google Sheets dataset.

Whatever data you choose, you need to make sure you’re building something that transforms it into something incredibly useful, dare I say “helpful”, to users.

For me, I pick data that I can weave into long form blog-post content. Build your programmatic SEO sites for users first, follow basic SEO best practices, and iterate over time to make the best programmatic site you can.

For the next post in this series, I’ll explain how I build my programmatic SEO framework in PHP. It’ll be a bit technical, but I’ll try to keep it simple and give examples and options for no-code alternatives as well!

If you RT this article and a lot of people are interested, it’ll encourage me to write that post much quicker. Just saying.