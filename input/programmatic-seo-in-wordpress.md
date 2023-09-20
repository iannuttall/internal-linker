---
h1: "Programmatic SEO in WordPress"
title: "Programmatic SEO in WordPress"
date: "2023-07-19"
description: "Learn how to get started with programmatic SEO in WordPress using the WP All Import or Multi Page Generator plugins."
---
        
With over 43% of websites on the internet using it, there are a lot of people that want to do programmatic SEO in WordPress. In this guide, I’ll show you how to get started and the different tools available.

Some of my very first programmatic SEO websites were built using WordPress and, fun fact, __I used to work for Automattic__ - the parent company of WordPress.com.

It’s very easy to scale your blog programmatically to create 100, 1000, or in my case 10000+, SEO-optimized blog posts in WordPress.

You can also do it without any coding skills or without being a WordPress expert.

So, how do you build a pSEO site in WordPress? Well, typically you will be using one of two plugins to do this:

1.   WP All Import
2.   Multi Page Generator

Both of these plugins have free versions available so I would recommend testing both to see which you prefer and then purchase the premium version of the plugin you’ll use for your programmatic SEO projects.

[toc]

## Preparing the Data

Before we can create a programmatic SEO site in WordPress, we need a data source to use. This can be an Excel CSV or Google Sheets as both plugins allow you to import from either.

The headings in your sheet will be variables that we can use in the page template later to create the actual content of the posts.

For this example, I’ll be using this database of foods and the calories in them.

The more data you have available in your template, the better you’ll be able to create a useful and helpful page for searchers and the more traffic you’ll be able to get. So make sure to pick datasets that have enough to build something good.

## Building a Programmatic SEO Website with WP All Import

### 1. Install and Activate the WP All Import Plugin

If you’re installing this from your WordPress dashboard you should be able to search WP All Import, or you can download it here. The name it shows up as though is actually Import any XML or CSV File to WordPress (nicely optimized SEO title for WordPress search!).

![](/img/blog/programmatic-seo-in-wordpress-1.png)

Once the plugin is installed and activated we can start the import process.

### 2. Create a New Import

![](/img/blog/programmatic-seo-in-wordpress-2.png)

Under the All Import menu, click the New Import option and you’ll have a few choices:

1.   __Upload a file.__ If you have a CSV file on your computer, you can use this option to import it.
2.   __Download a file.__ If you have a Google Sheets spreadsheet, this is the option you can use (but make sure the document is shared so anyone with the link can view it).
3.   __Use existing file.__ This option will use a file you have previously imported to the plugin.

I have the Pro version of WP All Import, so I can use option 2 here to download my data directly from Google Sheets.

Once downloaded you’ll be given the option of a post type to create. Generally, you’ll want to pick Posts or Pages for now. I’ll pick Posts in this example.

![](/img/blog/programmatic-seo-in-wordpress-3.png)

When you click Continue to Step 2, WP All Import is going to show you examples of the data from the sheet. These can be used when we create the programmatic SEO page template in the next step.

![](/img/blog/programmatic-seo-in-wordpress-4.png)

#### Add Filtering Options

You might want to filter your data to only include records that fit a specific run. So for example, if you wanted to only have high-calorie foods that are 500 calories or more, you can do that before proceeding to step 3.

![](/img/blog/programmatic-seo-in-wordpress-5.png)

### 3. Write Your Page Template

The next screen is a drag-and-drop interface that lets you set up your programmatic SEO variables in the title and content.

Make sure you really spend the time to make this template as good as it can be. Include variables for as many of the columns in your data as you can and make sure to add content by writing about them.

One of the downsides to WordPress is you cannot easily do dynamic things in this editor, so any conditional content you want to add will be done in your Sheet beforehand.

For example, if you wanted to add a paragraph about a particular food behind high or low calorie, you could add a column to your Sheet and use a formula to produce the text you want based on the calorie value.

![](/img/blog/programmatic-seo-in-wordpress-6.png)

#### Handling Images

Images are always difficult with programmatic SEO, especially so with programmatic SEO in WordPress.

![](/img/blog/programmatic-seo-in-wordpress-7.png)

The general options you have for doing this would be:

*   Use an external service like Imgur and include the image link directly in your data source. Then with the plugin options above, you can choose the Download images hosted elsewhere option and paste your variable into the text box.
*   Upload your images using the Media Library in WordPress. With the method, you can then use just the image filename/
*   Manually upload images to the wp-content/uploads/wpallimport/files/ folder and add the filenames to the text box.

These image options are only available in the paid version of the plugin, so keep that in mind when building your pSEO site with WP All Import.

#### Categories and Tags

You also have the option to assign posts to categories based on the variables in your data. For example, we could use the food group in each row to assign posts to that category. In this example, it would be Baked Goods:

![](/img/blog/programmatic-seo-in-wordpress-8.png)

Once imported, you would have a category called Baked Goods which contains all of the foods in that group.

#### Other Post Options

Before you move to the publishing page, make sure to review these options and set up your posts the way you want them to be. There are lots of options here that are useful when bulk importing a lot of content.

![](/img/blog/programmatic-seo-in-wordpress-9.png)

*   __Post Status.__ I usually import directly to Published, but if you have editors or writes that want to fine-tune the content, you might import them as a Draft first.
*   __Post Dates.__ If you have a lot of rows of content, I would recommend the Random dates option here so that it makes your content appear as if it has been published over a longer period of time.
*   __Comments.__ Personally I disable comments (and trackbacks and pingbacks) on all sites but if you have a community you might want to keep these options open.
*   __Post Slug.__ This lets you create an SEO-friendly URL for the posts. Often I will specify the slug myself in the data but if you leave it blank, WP All Import will slugify the post title for you.

### 4. Saving the Template and Creating Content

The final step is to pick a Unique Identifier for your import.

![](/img/blog/programmatic-seo-in-wordpress-10.png)

This is very important because it’s what WP All Import will use if you ever run the import again so that it knows which posts to update, add, or remove.

In my data I have an ID field, but you can use multiple values in here if you like to make it unique to the specific row.

You can also click Auto-detect to have the plugin set one up for you.

Once that is done, you can now import your content and, in this case, create 1371 new posts in WordPress!

(this might take a while)

![](/img/blog/programmatic-seo-in-wordpress-11.png)

When the import is complete, you will have a blog with 1300 posts, all properly categorized in WordPress and created programmatically by WP All Import.

![](/img/blog/programmatic-seo-in-wordpress-12.png)

I created a quick video of this process and it was pretty popular on Twitter. There is no audio, but I'm planning to record a new version soon. 

Here's how I set up this dataset in WP All Import in about 6 minutes:

<iframe class="video" src="https://www.youtube.com/embed/6BvR7mUIWYo" title="Programmatic SEO in WordPress with WP All Import" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Building a Programmatic SEO Website with Multi Page Generator

![](/img/blog/programmatic-seo-in-wordpress-13.png)

The Multi Page Generator plugin is a little bit different to WP All Import.

Where WP All Import creates the posts physically in the database (which means they appear under Posts in your dashboard menu), MPG is more “programmatic”.

It’s a lot faster to create pages because it doesn’t need to run an import process in the same way as WP All Import.

You can also use the WordPress block editor with this plugin which means you have much more control of the design and layout of your posts vs WP All Import that uses the Classic Editor style.

I use this plugin when I need to add much larger sections of content to my site and I don’t need or want them to be imported to the WordPress database (which can slow WP down).

Here is a complete step-by-step video guide to building the same site we made above, but using the paid version of Multi Page Generator:

<iframe class="video" src="https://www.youtube.com/embed/TCleV_OP-48" title="Building a Programmatic SEO Site in WordPress" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

I also published this on Twitter where it was seen 75,000 times!

## Summary

WordPress is a great choice for doing programmatic SEO if you are a beginner or don’t want to deal with code. Most people know and use WordPress, so setting up pSEO sites is much easier.

To make your templates more dynamic and varied based on the data, you would do all of that inside your data source spreadsheet instead.

One of the courses in Practical Programmatic is an hour-long tutorial on exactly how to do this in Google Sheets!

Both plugins (in the paid version) let you set it up so that your data can be updated automatically on a schedule. This means if you add, remove, or modify rows in your dataset, the plugins will make that change on your site as well.

So if you had formulas in your sheet that get the daily exchange rate, and convert currency amounts, for example, your website data would be up-to-date as long as the plugin is set to update it daily.

If you have any questions about programmatic SEO in WordPress, hit me up on Twitter and I’ll try to answer them for you.