import requests

# Base URLs for mock APIs
DATABASES = {
    "WHO": "https://www.who.int/api/v1/search?q={query}",
    "CDC": "https://data.cdc.gov/resource/example.json?q={query}",
    "PubMed": "https://pubmed.ncbi.nlm.nih.gov/api/v1/search?term={query}",
    # Add 7 more database APIs
}

def search_health_databases(query):
    results = {}
    for db_name, base_url in DATABASES.items():
        try:
            response = requests.get(base_url.format(query=query))
            if response.status_code == 200:
                results[db_name] = response.json()  # Assuming JSON response
            else:
                results[db_name] = f"Error {response.status_code}"
        except Exception as e:
            results[db_name] = f"Error: {str(e)}"
    return results

def display_results(results):
    for db, data in results.items():
        print(f"\nResults from {db}:\n")
