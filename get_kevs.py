import requests
import json
from datetime import datetime

def download_cisa_kev_catalog(output_path=None):
    """
    Download the CISA Known Exploited Vulnerabilities (KEV) Catalog in JSON format.
    
    :param output_path: Optional custom file path to save the JSON. 
                        If None, generates a filename with current timestamp.
    :return: Path to the saved JSON file
    """
    # CISA KEV Catalog JSON URL
    kev_url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    
    try:
        # Send GET request to download the JSON
        response = requests.get(kev_url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON data
        kev_data = response.json()
        
        # Generate output filename if not provided
        if output_path is None:
            output_path = f"known_exploited_vulnerabilities.json"
        
        # Save the JSON to a local file
        with open(output_path, 'w') as f:
            json.dump(kev_data, f, indent=2)
        
        print(f"CISA KEV Catalog downloaded successfully to {output_path}")
        print(f"Total vulnerabilities in catalog: {len(kev_data.get('vulnerabilities', []))}")
        
        return output_path
    
    except requests.RequestException as e:
        print(f"Error downloading CISA KEV Catalog: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None


if __name__ == "__main__":
    download_cisa_kev_catalog()