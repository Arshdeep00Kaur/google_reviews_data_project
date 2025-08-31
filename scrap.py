import requests
import json
import pandas as pd
import time
import schedule
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='scrap.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Your SerpAPI Key from environment variable
SERPAPI_KEY = os.getenv('SERPAPI_KEY')

# Define the city
city = "Ahmehdabad"  # Change this if needed
query = f"Top IT Companies in {city}"

# Folder to store scraped reviews
folder_path = r"D:/google_reviews_data/Scrapped_Data"

def get_top_companies_in_city(query, num_results=10):
    """Fetch top companies in a city and get their Place IDs dynamically."""
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_maps",
        "q": query,
        "api_key": SERPAPI_KEY,
        "hl": "en",
        "num": num_results
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        print("API Response:", json.dumps(data, indent=4))  # Debugging line

        place_ids = {result.get("title"): result.get("place_id") for result in data.get("local_results", []) if result.get("title") and result.get("place_id")}
        
        if not place_ids:
            logging.error("No company data found in API response.")

        return place_ids
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching company place IDs: {e}")
        return {}

def get_google_reviews(place_id, num_reviews=100):
    """Fetch reviews for a given Place ID."""
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_maps_reviews",
        "place_id": place_id,
        "api_key": SERPAPI_KEY,
        "hl": "en",
        "limit": num_reviews
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        reviews = []
        for review in data.get("reviews", []):
            reviews.append({
                "username": review.get("user"),
                "rating": review.get("rating"),
                "text": review.get("snippet"),
                "date": review.get("date"),
                "ct": city  # Add city column
            })
        return reviews
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data for {place_id}: {e}")
        return []

def scrape_reviews_for_top_companies():
    """Fetch new top companies dynamically and scrape their reviews."""
    today_date = time.strftime("%Y-%m-%d")
    all_reviews = []

    # Get Place IDs for companies in the specified city
    company_place_ids = get_top_companies_in_city(query)
    print("Companies found:", company_place_ids)  # Debugging line

    if not company_place_ids:
        logging.error("No companies found. Exiting...")
        return

    logging.info(f"Found {len(company_place_ids)} top companies. Scraping reviews...")

    for company, place_id in company_place_ids.items():
        logging.info(f"Scraping reviews for {company}...")
        print(f"Scraping reviews for {company}...")  # Debugging line

        try:
            reviews = get_google_reviews(place_id, num_reviews=100)
            for review in reviews:
                review["company"] = company  # Add company name
                all_reviews.append(review)

            # Wait to avoid rate limits
            time.sleep(5)

        except Exception as e:
            logging.error(f"Error scraping {company}: {str(e)}")

    # Ensure folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Save results to CSV
    file_path = os.path.join(folder_path, f"google_reviews_{city}_{today_date}.csv")
    try:
        df = pd.DataFrame(all_reviews)
        df.to_csv(file_path, index=False)
        logging.info(f"Scraping completed! 🚀 Data saved in: {file_path}")
        print(f"Scraping completed! 🚀 Data saved in: {file_path}")  # Debugging line
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")

# Run the function immediately for debugging
scrape_reviews_for_top_companies()

# Uncomment this for scheduling
# schedule.every().day.at("10:00").do(scrape_reviews_for_top_companies)

# Keep the script running continuously
# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(60)  # Check every minute
# except KeyboardInterrupt:
#     logging.info("Script interrupted by user. Exiting...")
