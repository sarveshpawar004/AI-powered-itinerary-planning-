import requests
import os

UNSPLASH_ACCESS_KEY = "4gmnyeW0VSiCEjoWYyxa-Dbte92FUXIRpfbk8yzL5Ho"

def get_destination_images(query):
    """
    Fetches multiple high-quality image URLs for a destination from Unsplash.
    """
    if not UNSPLASH_ACCESS_KEY:
        print("Unsplash API Key missing.")
        # Return empty list or raise error - user wanted "no dummy images"
        # Returning empty list will likely cause frontend to show no images or broken images, 
        # but user specifically said "do not use dummy images".
        # However, to avoid total breakage, let's just return an empty list and let the frontend handle it or loop.
        return []

    url = f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id={UNSPLASH_ACCESS_KEY}&per_page=5&orientation=landscape"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data.get('results'):
            return [img['urls']['regular'] for img in data['results']]
        else:
            print(f"No Unsplash results for {query}")
            return []
    except Exception as e:
        print(f"Error fetching Unsplash images: {e}")
        return []
