# Frontend Architecture Documentation

## 1. Overview
This document outlines the frontend structure, technology stack, and implementation details for the AI Smart Travel Planner application. The frontend is built using server-rendered HTML templates with Flask, enhanced by vanilla JavaScript for interactivity and custom CSS for styling.

## 2. Technology Stack
- **Backend Framework**: Flask (Python) rendering Jinja2 templates.
- **Frontend Core**: HTML5, CSS3, JavaScript (ES6+).
- **Styling**: Custom CSS with Glassmorphism design system.
- **Icons**: FontAwesome 6.4.0.
- **Fonts**: Google Fonts (Outfit for headings, Space Grotesk for body).
- **Maps**: Leaflet.js (v1.9.4) for interactive maps.
- **External Services**: Unsplash API for dynamic destination images.

## 3. Project Structure
The frontend code is organized within the standard Flask directory structure:

```
├── templates/              # HTML Templates (Jinja2)
│   ├── base.html           # Base layout with common head, nav, footer
│   ├── index.html          # Landing page with input form
│   ├── dashboard.html      # User's travel history dashboard
│   └── result.html         # Detailed itinerary view
├── static/                 # Static Assets
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # Frontend logic and API calls
│   └── img/                # Static images (logos, placeholders) (empty/not used currently)
```

## 4. UI Components & Templates

### 4.1 Base Layout (`base.html`)
- **Head**: Includes meta tags, Google Fonts, FontAwesome, Leaflet CSS, and local `style.css`.
- **Navigation (`<nav>`)**: 
  - Logo "AI TravelGenie" with icon.
  - Links to Home, Features, Dashboard, About.
- **Main (`<main>`)**: Jinja block `{% block content %}` where specific page content is injected.
- **Footer**: Simple copyright and attribution.
- **Scripts**: Includes Leaflet JS and a block for page-specific scripts.

### 4.2 Landing Page (`index.html`)
- **Hero Section**:
  - **Background**: Immersive full-screen background using CSS/images.
  - **Content**: Headline "Craft Your Perfect Journey".
  - **Visuals**: Floating glass card with a travel image (Unsplash source) and icons.
- **Glass Form Container**:
  - A central form styled with glassmorphism (transparency, blur).
  - Fields: Destination, Start Date, Duration, Budget, Style, Transport.
  - Floating 3D-style icons (Location, Plane, Camera) acting as decorations.
- **Features Section**: Grid layout highlighting "Smart AI", "Instant Results", "Budget Safe".
- **About Section**: Brief project description.

### 4.3 Dashboard (`dashboard.html`)
- **Purpose**: Displays a list of previously generated trips.
- **Trip Cards**:
  - Each card shows a destination image, date, and budget.
  - Images are currently static/placeholder in the template for list view.
  - Empty state provided if no trips exist.

### 4.4 Result Page (`result.html`)
- **Header Slideshow**:
  - A dynamic slideshow background using images fetched for the specific destination.
  - Overlay with Trip Name, Summary, Total Cost, and Weather.
- **Itinerary Grid**:
  - **Day-by-Day**: Cards for each day with theme, date, and activity list.
  - **Accommodation**: Suggested hotel with price.
- **Sidebar**:
  - **Transport**: Flight/Train details.
  - **Cost Breakdown**: Graphical/list representation of expenses.
  - **Packing Tips**: Checklist.
  - **Gallery**: Grid of additional destination images.

## 5. Styling Strategy (`style.css`)
The application uses a modern, "Glassmorphism" design language.

- **Variables**: CSS variables (e.g., `--primary-color`, `--glass-bg`) control the theme.
- **Glassmorphism**: 
  - `.glass-card`, `.glass-form-container`.
  - Uses `backdrop-filter: blur(10px)`, `background: rgba(255, 255, 255, 0.1)`, and white borders to create a frosted glass effect.
- **Animations**:
  - `animate-up`: Slide-up fade-in effect for elements on load.
  - Floating animations for icons (`floating-icon`, `floating-decor`).
  - Hover effects on cards and buttons (`transform: translateY(-5px)`).
- **Typography**:
  - **Headings**: 'Outfit', sans-serif (Bold, modern).
  - **Body**: 'Space Grotesk', sans-serif (Clean, readable).

## 6. Image Handling Strategy

### 6.1 Source
- **Dynamic Images**: The application uses the **Unsplash API** to fetch high-quality images relevant to the user's destination.
- **Service**: `services/image_service.py` handles the API calls.
  - Function: `get_destination_images(query)`
  - Endpoint: `https://api.unsplash.com/search/photos`
  - Parameters: `query={destination}`, `orientation=landscape`.

### 6.2 Storage & Integration
- **Database**: Image URLs are stored in the `Trip` model as a JSON list (`image_urls` column).
- **Backend Passing**: The Flask route `/generate_trip` fetches images and passes them to the template via the `trip` object.
- **Frontend Rendering**:
  - **Backgrounds**: Used in CSS `background-image` for the header slideshow (`result.html`).
    ```html
    <div class="slide" style="background-image: url('{{ img_url }}');"></div>
    ```
  - **Gallery**: Rendered as `<img>` tags in the sidebar gallery.
    ```html
    <img src="{{ img_url }}" alt="..." class="gallery-img">
    ```

## 7. Interactivity (`main.js`)
- **Form Handling**:
  - Intercepts `submit` event on `#tripForm`.
  - **Loading State**: Disables button, shows spinner ("Processing...").
  - **API Call**: Sends POST request to `/generate_trip` with form data as JSON.
  - **Redirection**: On success, redirects user to `/trip/{trip_id}`.
- **Error Handling**: Alerts user on failure (e.g., API errors, missing fields).
