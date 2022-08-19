# Run after scrape_links_events.R 
# Exract scraped links and add to Events.csv then run clean_events.R

if(!require(pacman)) install.packges("pacman"); require(pacman)
require(pacman)
p_load(qdapRegex,rvest,xml2)


data <- read.csv("../data/Events.csv")

data$Scraped_Links    <- NA
data$Top_Scraped_Link <- NA

for(n in data$Name){ #[1]
	print(n)
	n  <- gsub("\\(", " ", n)
	n  <- gsub("\\)", " ", n)
	fn <- paste0(n,"_results.txt")
	fn <- gsub(" ", "_", fn)
	print(fn)
	if(file.exists(fn)){
		links <- readLines(fn)
		links <- ex_url(links, trim=T)
		links <- unlist(links[!is.na(links)])
		#print(links[1])
		#print(data$Top_Scraped_Link[data$Name==n])
		if(length(links)>0){
			data$Top_Scraped_Link[data$Name==n] <- links[1]
			data$Scraped_Links[data$Name==n]    <- paste0(links,collapse=",")   			
		}
	}
}    

write.csv(data, "../data/Events.csv")

