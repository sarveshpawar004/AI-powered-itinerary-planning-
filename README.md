🌍 AI-Powered Smart Travel Planner
🚀 Project Overview

The AI-Powered Smart Travel Planner is a sophisticated web application that generates personalized travel itineraries based on user preferences.

It leverages Google’s Gemini LLM for intelligent itinerary creation and integrates the Unsplash API for dynamic, visually rich travel experiences — all wrapped in a modern Glassmorphism UI.

🧠 Key Features
1. ✨ Generative AI Integration (Gemini)

Advanced prompt engineering to interact with gemini-3-flash-preview

Enforces structured JSON responses for reliable parsing

Generates:

Day-by-day itineraries

Budget estimates

Activity suggestions

Fully context-aware:

Travel style (Luxury, Backpacking, etc.)

Budget constraints

Transportation preferences

2. 🖼️ Dynamic Visual Content Pipeline

Custom Image Service (services/image_service.py)

Fetches location-specific images using Unsplash API

Includes:

Error handling

Fallback mechanisms (API rate limits)

Dynamically maps images to itinerary content for better UX

3. 🎨 Modern UI/UX (Glassmorphism Design)

Custom Glassmorphism UI

Translucent cards

Background blur effects

Subtle borders

Smooth animations:

fadeInUp

zoomDrift

fadeSlide

Fully responsive using:

CSS Grid

Flexbox

Dynamic slideshow header for immersive experience

4. 🏗️ Architecture & State Management

Clean modular Flask architecture:

Services → Business logic

Routes → Controllers

Templates → Views

Uses server-side sessions:

Handles multi-step flows

No heavy database required

Strong input validation for stability and security

5. ⚡ Performance & Optimization

Optimized API calls to reduce latency

Lightweight frontend:

Vanilla JavaScript (ES6+)

No heavy frameworks

Efficient:

Semantic HTML

Optimized CSS selectors

🛠️ Tech Stack
Backend

Python

Flask

AI / ML

Google Gemini (Pro / Flash)

APIs

Unsplash API

RESTful API Design

Frontend

HTML5

CSS3 (Glassmorphism)

JavaScript (ES6+)

Jinja2

Deployment / Environment

Gunicorn

Python-dotenv

📁 Project Structure (Example)
project-root/
│
├── app.py
├── routes/
│   └── main_routes.py
├── services/
│   ├── ai_service.py
│   └── image_service.py
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   ├── css/
│   └── js/
├── .env
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key
UNSPLASH_ACCESS_KEY=your_access_key
SECRET_KEY=your_secret_key
5. Run the Application
python app.py
🌐 Deployment

Use Gunicorn for production:

gunicorn app:app

Can be deployed on:

Render

Railway

AWS / GCP / Azure

🔮 Future Enhancements

User authentication & saved trips

Integration with booking APIs (flights/hotels)

Real-time weather data

Multi-language support

Mobile app version

🤝 Contributing
Contributions are welcome!
Feel free to fork the repo and submit a pull request.


👨‍💻 Author
Sarvesh
