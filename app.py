from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
from config import Config
from services.ai_service import generate_itinerary
from services.image_service import get_destination_images

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'super_secret_key_change_in_production' 

# Database removed as requested

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_trip', methods=['POST'])
def generate_trip():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        destination = data.get('destination')
        start_date = data.get('start_date')
        duration = data.get('duration')
        budget = data.get('budget')
        style = data.get('style')
        transport = data.get('transport')
        
        # Validation
        if not all([destination, start_date, duration, budget, style, transport]):
             return jsonify({'error': 'Missing required fields'}), 400
             
        try:
            duration = int(duration)
        except ValueError:
             return jsonify({'error': 'Duration must be a number'}), 400
    
        # AI Generation
        trip_data = generate_itinerary(destination, start_date, duration, budget, style, transport)
        
        if trip_data:
            # Fetch Images
            image_urls = get_destination_images(destination)
            trip_data['image_urls'] = image_urls
            trip_data['image_url'] = image_urls[0] if image_urls else ""
            
            # Store in Session (No DB)
            session['current_trip'] = trip_data
            
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Failed to generate itinerary'}), 500
            
    except Exception as e:
        print(f"Error in generate_trip: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/result')
def result():
    trip_data = session.get('current_trip')
    if not trip_data:
        return redirect(url_for('index'))
    return render_template('result.html', trip=trip_data)

@app.route('/dashboard')
def dashboard():
    # Featured Destinations for Discovery
    featured_destinations = [
        {
            "name": "Kyoto, Japan",
            "description": "Ancient temples, traditional tea houses, and stunning cherry blossoms.",
            "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=1080&auto=format&fit=crop"
        },
        {
            "name": "Santorini, Greece",
            "description": "Whitewashed houses, blue domes, and breathtaking sunsets over the Aegean.",
            "image": "https://images.unsplash.com/photo-1613395877344-13d4c79e4284?q=80&w=1080&auto=format&fit=crop"
        },
        {
            "name": "Banff, Canada",
            "description": "Turquoise lakes, majestic mountains, and endless outdoor adventures.",
            "image": "https://images.unsplash.com/photo-1561134643-6630099e58bd?q=80&w=1080&auto=format&fit=crop"
        },
         {
            "name": "New York City, USA",
            "description": "The city that never sleeps, full of energy, culture, and iconic landmarks.",
            "image": "https://images.unsplash.com/photo-1496442226666-8d4a0e62e6e9?q=80&w=1080&auto=format&fit=crop"
        },
        {
            "name": "Cape Town, South Africa",
            "description": "A stunning blend of mountains, beaches, and vibrant city life.",
            "image": "https://images.unsplash.com/photo-1580060839134-75a5edca2e99?q=80&w=1080&auto=format&fit=crop"
        },
         {
            "name": "Bali, Indonesia",
            "description": "A tropical paradise with lush jungles, spiritual temples, and beautiful beaches.",
            "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?q=80&w=1080&auto=format&fit=crop"
        }
    ]
    return render_template('dashboard.html', destinations=featured_destinations)

if __name__ == '__main__':
    app.run(debug=True)
