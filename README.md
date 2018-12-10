# Identifying and removing bias from Neural Nets

The files in this code base can be used to replicate the experiments and results in report.pdf

## Joint-Learning-Unlearning.ipynb
This python notebook contains the implementation of the JLU training algorithm. 

## tSNE.ipynb
This python notebook contains the implementation to load model variable and prepare tsv file for t-SNE embeddings.

## test-networks-on-specific-datasets.ipynb
This python notebook contains the implementation to load a model and test it on specific datasets.

#Data Scraping
The final data and CSV files can be directly used from SportsDataScraper/SportsDataScraper/img_download/FinalData/. 
If you wish to replay the scraping, run the individual spiders and pipe it to the appropriate files. Next, run the image cleaners and resizers for each data source followed by the face_prediction scripts. 
You will need to have a microsoft account and change the APItoken with your generated token.

run the merging data notebook and use sampler in FinalData to generate the required samples for experimenting.
