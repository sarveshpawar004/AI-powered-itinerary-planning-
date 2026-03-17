# 🌍 AI-Powered Smart Travel Planner

## 🚀 Project Overview
The AI-Powered Smart Travel Planner is a sophisticated web application that generates personalized travel itineraries based on user preferences.

It leverages Google’s Gemini LLM for intelligent itinerary creation and integrates the Unsplash API for dynamic, visually rich travel experiences — all wrapped in a modern Glassmorphism UI.

---

## 🧠 Key Features

### ✨ Generative AI Integration (Gemini)
- Advanced prompt engineering using `gemini-3-flash-preview`
- Enforces structured JSON responses for reliable parsing
- Generates:
  - Day-by-day itineraries
  - Budget estimates
  - Activity suggestions
- Context-aware planning based on:
  - Travel style (Luxury, Backpacking, etc.)
  - Budget constraints
  - Transportation preferences

---

### 🖼️ Dynamic Visual Content Pipeline
- Custom Image Service (`services/image_service.py`)
- Fetches location-specific images using Unsplash API
- Includes:
  - Error handling
  - Fallback mechanisms (API rate limits)
- Dynamically maps images to itinerary content

---

### 🎨 Modern UI/UX (Glassmorphism)
- Custom Glassmorphism design:
  - Translucent UI elements
  - Background blur effects
  - Subtle borders
- Animations:
  - fadeInUp
  - zoomDrift
  - fadeSlide
- Fully responsive using:
  - CSS Grid
  - Flexbox
- Dynamic slideshow header for immersive experience

---

### 🏗️ Architecture & State Management
- Modular Flask architecture:
  - Services → Business Logic
  - Routes → Controllers
  - Templates → Views
- Server-side session management for multi-step flows
- Strong input validation for stability

---

### ⚡ Performance & Optimization
- Optimized API calls to reduce latency
- Lightweight frontend using vanilla JavaScript (ES6+)
- Efficient semantic HTML and optimized CSS

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### AI / ML
- Google Gemini (Pro / Flash)

### APIs
- Unsplash API
- RESTful API Design

### Frontend
- HTML5
- CSS3 (Glassmorphism)
- JavaScript (ES6+)
- Jinja2

### Deployment / Environment
- Gunicorn
- Python-dotenv

---

## 📁 Project Structure

```text
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
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
UNSPLASH_ACCESS_KEY=your_access_key
SECRET_KEY=your_secret_key
```

### 5. Run Application
```bash
python app.py
```

---

## 🌐 Deployment
Use Gunicorn for production:

```bash
gunicorn app:app
```

---

## 🔮 Future Enhancements
- User authentication & saved trips
- Integration with booking APIs (flights/hotels)
- Real-time weather data
- Multi-language support
- Mobile app version
---

## 👨‍💻 Author
Sarvesh
