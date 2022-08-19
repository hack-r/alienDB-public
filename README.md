# alienDB-public
Code repository of the https://alienDB.org website.


## Overview

alienDB.org ("AlienDB") is a data and ML-centric website about ET life, UAPs, SETI, METI and the human beings behind the search. The site is only a few weeks old (as of mid August, 2022) so it's incomplete, rapidly evolving, and fairly messy. 

For now I think it will be best if I just include a few of the most useful snippets and perhaps the source of the homepage. Once the site and its data tables are more mature and stable I will see about posting the full, reproducible code.

## Contents

I picked out the following code snippets as being the most interesting:

  1. News data scrapers (moved from R to SerpAPI-based CURL commands)
  2. Text Mining
  3. Gantt-style Interative Timeline
  4. Vertical timeline plot (which is static, for now)

## Comments on Streamlit

This is the first site I've written using Streamlit, asides from a "Hello World" and reproducing some examples from their gallery. I've written webapps and portals using Python's Django framework and compared to that I would say that Streamlit ertainly caters more to data scientists, although Django provides a closer mapping to the underlying HTML, CSS & JS (and Model-View-Whatever) which is advantageous for writing and maintaining multiuser platforms / portals. 

My choice was primarily based on what I believed to be syngery with my (real) job. Overall Streamlit has been easy to use and performs adequately.  

*Pro's of Using Streamlit*

 - It makes it easy to work with Python-based data
 - The employees of the company are pretty good about replying to the questions they can at https://discuss.streamlit.cio
 - No need to make a purchase
 - Simplifies making a website while still allowing the flexibility of writing code
 
*Con's of Using Streamlit*

 - Relative to Shiny, it's less flexible, has far fewer examples, and a smaller community - but I expect this to be a temporary situation as Streamlit expands and its users gain more experience (and publish more of their code)
 - Although it claims to be fast even with Big Data, on the small scale it can be slower than expected 
 - Each page is an app which must be reloaded and run on every page load
 - Streamlit uses your website as free advertising ("Made with Streamlit") and even if you hide this with CSS it will still show up while things are loading and on errors
 
 *Conclusion*
 
 I think Streamlit is a great tool and I expect it to keep getting better. If this site were not in part a Streamlit-learning excercise I think a better approach might be to write non-data-centric components of the website using native web technologies and limit Streamlit to serving just 1 or 2 pages of data products. Bear in mind that I'm still a Streamlit noob, so my perceptions may be shaped by my limited experience and expertise.
