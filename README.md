# CS7IS4-Group-7

## Dependencies
This project has the following python dependecies:
- `pypdf`

## Archive structure
- `data`: This directory contains raw data and processed data
	- `data/raw-txt`: This directory contains .txt files containing the raw text data extracted from strategic plans
	- `data/tokenized-txt`: This directory contains .txt files containing the tokens from each document after pre-processing (stopword removal, lemmatization)
	- `data/university-lists`: This directory contains the manually created CSV files with data about the universities (country, continent, year of establishment, ranking, etc.)
- `pre-processing`: This directory contains the python scripts for pre-processing the data
- `analysis`: This directory contains the .ipynb notebooks used to perform the data analysis
- `admin`: This directory contains the project management documents (meeting agendas and minutes, time sheets etc.)