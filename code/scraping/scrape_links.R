# Note:
#      This is a simple R script to scrape DuckDuckGo for links
# related to table entries. 
#
#      It needs some extra logic to ensure all scraped links are
# sufficiently relavent, unique and high quality. Right now
# I have not yet used the results of the scraping.

data <- read.csv("../data/Events.csv")

for(n in data$Name){
	n  <- gsub("\\(", " ", n)
	n  <- gsub("\\)", " ", n)
	fn <- paste0(n,"_results.txt")
	fn <- gsub(" ", "_", fn)
	x <- paste0("ddgr -x --np -n 25 ",n, " > ",fn)
	try(system(x))
	system("sleep 2")
}

#writeLines(y,"scrape_events.sh")
print("Scrape complete. Check the filesystem for txt's")

saveRDS(data$Name, "event_link_index.RDS")

