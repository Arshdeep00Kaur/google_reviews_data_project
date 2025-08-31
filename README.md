# Google Reviews Data Mining Project

## 📋 Project Overview

This project is a comprehensive data mining solution that scrapes Google reviews for top IT companies across multiple Indian cities, performs sentiment analysis, and creates interactive dashboards for business intelligence insights.

## 🎯 Key Features

- **Automated Web Scraping**: Dynamically fetches top IT companies and their Google reviews using SerpAPI
- **Multi-City Coverage**: Supports major Indian cities including Delhi, Mumbai, Bangalore, Hyderabad, Pune, Ahmedabad, and more
- **Sentiment Analysis**: Uses NLTK's VADER sentiment analyzer to analyze review sentiments
- **Data Processing Pipeline**: Complete ETL pipeline from raw data to analysis-ready datasets
- **Business Intelligence**: Power BI dashboards for visual insights and analytics
- **Scheduled Automation**: Built-in scheduling capabilities for regular data updates

## 🏗️ Project Structure

```
google_reviews_data/
├── scrap.py                              # Main scraping script
├── scrap.log                            # Logging file for scraping activities
├── README.md                            # Project documentation
├── Data Mining Event Final Dashboard Final.pbix  # Final Power BI dashboard
├── dataminingevent.pbix                 # Power BI dashboard (draft)
├── Scrapped Data.zip                    # Archived raw data
├── join_csv/                            # Data processing and analysis
│   ├── main.ipynb                       # Data merging notebook
│   ├── EDA.ipynb                        # Exploratory Data Analysis
│   ├── sentiment_analysis.ipynb         # Sentiment analysis pipeline
│   ├── merged_output.csv               # Combined raw data
│   ├── modified_dataset.csv            # Cleaned and processed data
│   ├── processed_dataset.csv           # Final dataset with sentiment scores
│   └── company_stats.csv               # Aggregated company statistics
├── Scrapped Data/                       # Raw scraped data (batch 1)
│   └── Scrapped Data/
│       ├── google_reviews_batch_2025_Batch_*.csv
│       └── ...
└── Scrapped_Data/                       # Raw scraped data (batch 2)
    ├── google_reviews_*_2025-*.csv
    └── ...
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- SerpAPI account and API key
- Power BI Desktop (for dashboard visualization)

### Required Python Libraries

```bash
pip install pandas requests nltk schedule
```

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd google_reviews_data
   ```

2. **Configure API Key**
   - Sign up for SerpAPI at https://serpapi.com/
   - Replace the `SERPAPI_KEY` in `scrap.py` with your actual API key

3. **Install Dependencies**
   ```bash
   pip install pandas requests nltk schedule
   ```

4. **Download NLTK Data**
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## 📊 Data Pipeline

### 1. Data Scraping (`scrap.py`)

- **Functionality**: Automatically discovers top IT companies in specified cities and scrapes their Google reviews
- **Data Sources**: Google Maps via SerpAPI
- **Features**:
  - Dynamic company discovery
  - Rate limit handling
  - Error logging
  - Scheduled execution support
  - Multi-city support

**Cities Covered**:
- Delhi
- Mumbai
- Bangalore (Bengaluru)
- Hyderabad
- Pune
- Ahmedabad
- Noida
- Chandigarh
- Kochi

### 2. Data Merging (`main.ipynb`)

- Combines CSV files from multiple scraping sessions
- Merges data from different folders and batches
- Creates a unified dataset for analysis

### 3. Data Preprocessing (`EDA.ipynb`)

- **Data Cleaning**: Handles missing values and data type conversions
- **Feature Engineering**: Extracts user information from nested dictionaries
- **Data Transformation**: Prepares data for sentiment analysis
- **Output**: `modified_dataset.csv`

### 4. Sentiment Analysis (`sentiment_analysis.ipynb`)

- **VADER Sentiment Analysis**: Analyzes review text sentiment
- **Sentiment Scoring**: Generates compound sentiment scores (-1 to +1)
- **Classification**: Categorizes reviews as positive, negative, or neutral
- **Company Analytics**: Calculates average ratings and sentiment scores per company
- **Discrepancy Analysis**: Identifies gaps between ratings and sentiment scores
- **Output**: `processed_dataset.csv` and `company_stats.csv`

## 📈 Key Metrics and Insights

### Generated Datasets

1. **`processed_dataset.csv`**: Individual review-level data with sentiment scores
   - Company name
   - Rating (1-5 stars)
   - Review text
   - Date
   - City
   - Contributor ID
   - Number of reviews by user
   - Sentiment score (-1 to +1)
   - Sentiment label (positive/negative/neutral)

2. **`company_stats.csv`**: Company-level aggregated statistics
   - Average rating
   - Average sentiment score
   - Total review count
   - Rating-sentiment discrepancy metric

### Business Intelligence Features

- **Performance Benchmarking**: Compare companies across cities
- **Sentiment vs Rating Analysis**: Identify authentic vs inflated ratings
- **Geographic Insights**: City-wise company performance analysis
- **Trend Analysis**: Time-series review patterns
- **Reputation Monitoring**: Track company reputation over time

## 🔧 Usage

### Running the Scraper

```python
python scrap.py
```

### Processing the Data

1. **Merge Data**: Run `main.ipynb` to combine all CSV files
2. **Clean Data**: Execute `EDA.ipynb` for data preprocessing
3. **Analyze Sentiment**: Run `sentiment_analysis.ipynb` for sentiment scoring

### Automated Scheduling

Uncomment the scheduling section in `scrap.py` to enable daily automated scraping:

```python
schedule.every().day.at("10:00").do(scrape_reviews_for_top_companies)
```

## 📊 Power BI Dashboard

The project includes two Power BI dashboard files:
- `Data Mining Event Final Dashboard Final.pbix` - Complete dashboard with all visualizations
- `dataminingevent.pbix` - Draft version

### Dashboard Features
- Company performance comparison
- Sentiment analysis visualizations
- Geographic distribution of reviews
- Rating vs sentiment discrepancy analysis
- Review volume trends

## 🔍 Data Quality Features

- **Automated Error Handling**: Comprehensive logging and error management
- **Rate Limiting**: Built-in delays to respect API limits
- **Data Validation**: Null value handling and data type verification
- **Duplicate Prevention**: Intelligent data merging to avoid duplicates

## 📝 Logging

All scraping activities are logged in `scrap.log` with timestamps and detailed error information for debugging and monitoring purposes.

## 🔄 Workflow

1. **Data Collection**: `scrap.py` automatically discovers and scrapes company reviews
2. **Data Integration**: `main.ipynb` merges multiple data sources
3. **Data Cleaning**: `EDA.ipynb` preprocesses and cleans the dataset
4. **Sentiment Analysis**: `sentiment_analysis.ipynb` adds sentiment insights
5. **Visualization**: Power BI dashboards provide interactive analytics

## 🎯 Use Cases

- **Market Research**: Understand customer sentiment across IT companies
- **Competitive Analysis**: Compare company reputations and performance
- **Location Strategy**: Analyze geographic trends for business expansion
- **Reputation Management**: Monitor and track company reputation metrics
- **Investment Decisions**: Data-driven insights for business investments

## 🔧 Configuration

### Customizing Cities
Edit the `city` variable in `scrap.py`:
```python
city = "YourCityName"  # Change this to scrape different cities
```

### Adjusting Review Limits
Modify the `num_reviews` parameter in the scraping functions:
```python
reviews = get_google_reviews(place_id, num_reviews=200)  # Increase for more reviews
```

## 📋 Requirements

- **Python**: 3.7 or higher
- **SerpAPI Key**: Required for Google Maps and Reviews data
- **Storage**: Sufficient disk space for CSV files (varies by data volume)
- **Internet**: Stable connection for API calls

## 🛠️ Troubleshooting

### Common Issues

1. **API Rate Limits**: Increase sleep intervals in `scrap.py`
2. **Missing Data**: Check API key validity and internet connection
3. **Memory Issues**: Process data in smaller batches for large datasets
4. **File Path Errors**: Ensure all paths use forward slashes or raw strings

### Logs and Debugging

- Check `scrap.log` for detailed scraping logs
- Monitor console output during execution
- Verify API responses in debug mode

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational and research purposes. Please ensure compliance with Google's Terms of Service and SerpAPI's usage policies.

## 🔗 Dependencies

- **pandas**: Data manipulation and analysis
- **requests**: HTTP library for API calls
- **nltk**: Natural Language Processing toolkit
- **schedule**: Job scheduling library
- **SerpAPI**: Google search results API

## 📞 Support

For issues or questions:
1. Check the `scrap.log` file for error details
2. Verify API key and internet connectivity
3. Review data file paths and permissions
4. Consult the troubleshooting section above

---

**Note**: This project requires a valid SerpAPI key for data collection. Ensure you comply with all terms of service and rate limiting guidelines.
