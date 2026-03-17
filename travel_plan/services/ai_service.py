from google import genai
import json


client = genai.Client(api_key="AIzaSyDhI5J7QasoRd-93bBTkZ8Hzh9M5nfTIJg")

def generate_itinerary(destination, start_date, duration, budget, style, transport_pref):
    """
    Generates a travel itinerary using Gemini.
    Returns a Python dictionary parsed from the JSON response.
    """
    
    prompt = f"""
    Act as a high-end, personalized travel consultant. Create a detailed, authentic {duration}-day trip itinerary for {destination}.
    Budget Context: {budget} (Total). Provide specific approximate cost amounts for all estimates in the same currency.
    Travel Style: {style}.
    Preferred Transport: {transport_pref}.
    Start Date: {start_date}.

    CRITICAL INSTRUCTIONS:
    - BE SPECIFIC: Do NOT use generic phrases like "Explore the city" or "Visit local landmarks". 
    - REAL PLACES: Mention specific, real-world names of neighborhoods, streets, cafes, hidden gems, and iconic attractions in {destination}.
    - AUTHENTIC VIBE: Tailor the descriptions to the {style} travel style.
    - NUMERIC BUDGET: In the breakdown, provide specific currency amounts (e.g., "$500" or "₹40000"), NOT percentages.

    Return strictly valid JSON with this structure:
    {{
      "trip_name": "Authentic [Destination] Experience",
      "summary": "A high-level overview of the trip's highlights.",
      "estimated_cost": {{
        "total": "Total Amount with Currency Symbol",
        "breakdown": {{
          "accommodation": "Currency Amount",
          "transport": "Currency Amount",
          "food": "Currency Amount",
          "activities": "Currency Amount"
        }}
      }},
      "days": [
        {{
          "day": 1,
          "date": "YYYY-MM-DD",
          "theme": "Theme of the day",
          "activities": [
             {{ 
               "time": "Morning", 
               "activity": "Specific Activity Name (e.g., Breakfast at Cafe de Flore)", 
               "description": "One concise, engaging sentence about what to do/see there." 
             }},
             {{ "time": "Afternoon", "activity": "...", "description": "..." }},
             {{ "time": "Evening", "activity": "...", "description": "..." }}
          ],
          "accommodation_suggestion": {{ "name": "Real Hotel/Hostel Name", "approx_price": "Price/Night" }}
        }}
      ],
      "transport_suggestions": {{
        "flight": {{ "airline": "Typical Airline", "approx_price": "Approx Price" }},
        "train": {{ "name": "Common Train Type/Service", "approx_price": "Approx Price" }}
      }},
      "packing_tips": ["Specific item for this season/destination", "Another item"],
      "weather_forecast": "Succinct weather expectation (e.g., Sunny with cool breezes)"
    }}
    
    Ensure the JSON is raw and valid. Do not use markdown backticks or any explanations outside the JSON.
    """

    try:
        # Using the requested model and client method
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=prompt
        )
        
        # Clean up if markdown backticks are present
        cleaned_text = response.text.replace('```json', '').replace('```', '').strip()
        data = json.loads(cleaned_text)
        return data
    except Exception as e:
        print(f"Error generating itinerary: {e}")
        # mocking is removed as requested
        raise e
