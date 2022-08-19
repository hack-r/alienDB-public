# I started with an R-based search scraper for text mining,
#   but the free trial of SERP Api seems easier and more
#   sustainable.
# Let them worry about keeping fresh proxy IPs. They also provide
#   a "legal shield" so that you don't have to worry about
#   staying compliant.
curl --get https://serpapi.com/search \
 -d api_key=$MY_KEY \
 -d engine="youtube" \
 -d search_query="UAP" > ../data/youtube/uap.json
