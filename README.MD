# Trial test
Target website: http://www.tabirai.net
## 1.
_What is the best and the fastest way to get all Japan hotels from the target website? Please provide the best way how to achieve that and what tools, frameworks you will use. Provide the total number of hotels per region/prefecture._

Using `scrapy` framework to crawl the paginated search results pages like this one http://www.tabirai.net/hotel/hokkaido/search/result.aspx. 
An actual scraper would then go to the individual hotel details to retrieve the specific information/reviews etc.

The code is in `tabirai.spiders.tabirai`. The counts per region are:
```
{
 'counts/fukuoka': 113,
 'counts/hokkaido': 279,
 'counts/kagoshima': 140,
 'counts/kumamoto': 122,
 'counts/miyazaki': 28,
 'counts/nagasaki': 96,
 'counts/oita': 202,
 'counts/okinawa': 257,
 'counts/saga': 38
}
```

## 2.
_It is needed to perform daily updates of the hotel reviews, storage engine for that is MongoDB, but you need to update only reviews which was actually updated by few fields. What is the best and the fastest method you will use to achieve that?_
1. Crawl all of hotel reviews
2. Make sure to store a key identifying a unique review (ideally a review ID or a hotel+reviewer name+date or something)
3. The next day, go through all the hotel reviews pages again and go through the reviews and either:
- if we want to update the reviews, update specific mongo records based on the key we decided in 2.
- if we want to just get new reviews, scrape reviews until we reach a key we already have in mongo

## 3. 
_While working with the accomodation geo coordinates you found that they are represented in Japenese Geodetic System:_

`x = 503037529`
`y = 128366212`

_Please provide a solution to transform it into WGS 84 usual system (degrees)._

The solution is to convert milliseconds to degrees (by dividing by 3600000). The code example is in `tabirai.pipelines.to_degrees`.
These coordinates translate to:

`x = 139.73264694444444` `y = 35.65728111111111`

## 4.
_What is the best way to bypass any limitations to get publicly available content from the website (URL blocking, errors and etc)?_

in the order of simplicity:

- use different source of data that doesn't block
- use different user agent, add more randomized behaviour into the spider like random delays, less requests per second etc.
- use browser-based scraping tools like Selenium instead of scrapy to mask the scraping behaviour better
- use proxies

## 5.
_What tools you will use for creating REST API in Python?_

Depends on the size and function - if it's a small API, then Flask or FastAPI, if it's something bigger combined with a web app, then Django/Django-Rest-Framework
