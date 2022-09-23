# Indetifying Product opportunities for National Instrument company 
Obejectives of this project are:

1. Creating dataset by scraping national instrument forum to make a dataset containing comments mentioned in their forum. ( I did make this dataset using beautifulsoup library in python
2. Classification of comments mentioned in the forum to two categories of IMPROVEMENT IDEAS and NON-IMPROVEMNT IDEAS. Since all the comments in the forum may not contain ideas that we could utilize them as a source to analyze them and extract improvement ideas from them, I classify those non-relavent ones and disregard the other comments.
3. Train our model to automate classification 
4. Extract product opportunities using chance discovery algorithm. 

# Scraping national instrument website forum
This code builds the dataset containing questions asked by users along with their reputation of users.

This code used Beautifulsoup library and can scrape multiple pages to achieve not only the questions of users but also their reputation of them. The number of offered solutions and Kudos rate of each users are extracted. 
                                                              
Besides, numbers of replies that each question got are scraped to give us insight about how much each single comment is important for the forum.
