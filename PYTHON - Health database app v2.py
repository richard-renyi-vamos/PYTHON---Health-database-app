import requests
import json
import datetime

# Base URLs for mock APIs
DATABASES = {
    "WHO": "https://www.who.int/api/v1/search?q={query}",
    "CDC": "https://data.cdc.gov/resource/example.json?q={query}",
    "PubMed": "https://pubmed.ncbi.nlm.nih.gov/api/v1/search?term={query}",
    "NIH": "https://api.nih.gov/search?query={query}",
    "ECDC": "https://www.ecdc.europa.eu/api/search?q={query}",
    "MedlinePlus": "https://medlineplus.gov/api/v1/search?q={query}",
    "EMA": "https://www.ema.europa.eu/en/search-api?q={query}",
    "BMJ": "https://www.bmj.com/search-api?q={query}",
    "JAMA": "https://jamanetwork.com/api/v1/search?q={query}",
    "Healthline": "https://www.healthline.com/api/v1/search?q={query}",
}

def search_health_databases(query):
    results = {}
    for db_name, base_url in DATABASES.items():
        try:
            response = requests.get(base_url.format(query=query))
            if response.status_code == 200:
                results[db_name] = response.json()
            else:
                error_message = f"Error {response.status_code}"
                results[db_name] = error_message
                log_error(db_name, error_message)
        except Exception as e:
            error_message = f"Exception: {str(e)}"
            results[db_name] = error_message
            log_error(db_name, error_message)
    return results

def display_results(results):
    for db, data in results.items():
        print(f"\n🔍 Results from {db}:")
        if isinstance(data, dict) or isinstance(data, list):
            print(json.dumps(data, indent=2))
        else:
            print(data)

def filter_results(results, keyword):
    filtered = {}
    for db, data in results.items():
        if isinstance(data, (dict, list)):
            json_data = json.dumps(data).lower()
            if keyword.lower() in json_data:
                filtered[db] = data
    return filtered

def export_results_to_json(results, filename="health_search_results.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"✅ Results exported to {filename}")

def log_error(database_name, message):
    with open("error_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().isoformat()
        log_file.write(f"{timestamp} - {database_name}: {message}\n")
