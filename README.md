# Indetifying Product opportunities for National Instrument company 

The pdf file of project is 
<a href="https://www.researchgate.net/publication/363767154_Identifying_product_development_opportunities_using_topic_modeling_and_chance_discovery"> here. </a>

Obejectives of this project are:

1. Creating dataset by scraping national instrument forum to make a dataset containing comments mentioned in their forum. ( I did make this dataset using beautifulsoup library in python.
2. Classification of comments mentioned in the forum to two categories of IMPROVEMENT IDEAS and NON-IMPROVEMNT IDEAS. Since all the comments in the forum may not contain ideas that we could utilize them as a source to analyze them and extract improvement ideas from them, I classify those non-relavent ones and disregard the other comments.
3. Train our model to automate classification. 
4. Extract product opportunities using chance discovery algorithm. 

# Scraping national instrument website forum
This code builds the dataset containing questions asked by users along with their reputation of users.

This code used Beautifulsoup library and can scrape multiple pages to achieve not only the questions of users but also their reputation of them. The number of offered solutions and Kudos rate of each users are extracted. 
                                                              
Besides, numbers of replies that each question got are scraped to give us insight about how much each single comment is important for the forum.



# Reference:

1.<a href="https://www.semanticscholar.org/paper/IdeaGraph%3A-Turning-Data-into-Human-Insights-for-Wang-Ohsawa/445e8ea60969c50a9738012c09922efde443f2b5"> Wang, H., Ohsawa, Y., Lv, P., Hu, X., & Xu, F. 2014. IdeaGraph: Turning Data into Human Insights for Collective Intelligence. In F. Sun, T. Li, & H. Li (Eds.), Foundations and Applications of Intelligent Systems, 213: 33–44.</a>

2.<a href= "https://researchportal.port.ac.uk/en/publications/social-media-mining-for-ideation-identification-of-sustainable-so"> Ozcan, S., Suloglu, M., Okan, S. 2021. Social media mining for ideation: Identiﬁcation of sustainable solutions and opinion. Technovation  102322.</a>
