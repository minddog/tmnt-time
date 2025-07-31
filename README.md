# TMNT Hub - Teenage Mutant Ninja Turtles API & Website

A full-stack web application featuring the Teenage Mutant Ninja Turtles, built with FastAPI backend and vanilla JavaScript frontend, deployed on Vercel.

## Features

### Backend API
- **FastAPI** with automatic documentation
- RESTful endpoints for turtles, villains, episodes, weapons, and quotes
- Search functionality across all data
- CORS enabled for frontend integration

### Frontend Website
- Responsive design with TMNT-themed styling
- Interactive pages for browsing turtles, villains, and episodes
- Real-time search functionality
- Mobile-friendly navigation
- Dark theme with character-specific color schemes

## API Endpoints

- `GET /api` - API documentation
- `GET /api/v1/turtles` - List all turtles
- `GET /api/v1/turtles/{name}` - Get specific turtle
- `GET /api/v1/villains` - List all villains
- `GET /api/v1/villains/{name}` - Get specific villain
- `GET /api/v1/episodes` - List episodes (with pagination)
- `GET /api/v1/episodes/{id}` - Get specific episode
- `GET /api/v1/quotes/random` - Get random quote
- `GET /api/v1/weapons` - List all weapons
- `GET /api/v1/search?q={query}` - Search across all data

## Local Development

### Prerequisites
- Python 3.12+
- pip

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd vercel-python
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
uvicorn api.main:app --reload
```

5. Open your browser:
- Frontend: http://localhost:8000
- API docs: http://localhost:8000/docs

## Edge Config Setup (New!)

For ultra-fast API responses, set up Vercel Edge Config:

```bash
# Install dependencies
npm install

# Run the interactive setup wizard
npm run edge-config-wizard
```

This will:
- Guide you through creating Edge Config
- Automatically hydrate it with TMNT data
- Connect it to your project

## Deployment to Vercel

### Prerequisites
- Vercel account
- GitHub repository
- Vercel CLI (optional)

### Automatic Deployment

1. Push your code to GitHub
2. Import the project in Vercel dashboard
3. Vercel will automatically detect the configuration and deploy

### Manual Deployment

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

### Environment Variables

For GitHub Actions CI/CD, add these secrets to your repository:
- `VERCEL_TOKEN` - Your Vercel access token
- `VERCEL_ORG_ID` - Your Vercel organization ID
- `VERCEL_PROJECT_ID` - Your Vercel project ID

## Testing

Run tests locally:
```bash
pytest tests/ -v
```

Tests run automatically on push/PR via GitHub Actions.

## Project Structure

```
vercel-python/
├── api/
│   ├── main.py          # FastAPI application
│   ├── models.py        # Pydantic models
│   ├── routes/          # API endpoints
│   └── data/            # TMNT data
├── frontend/
│   ├── index.html       # Homepage
│   ├── pages/           # HTML pages
│   ├── css/             # Styling
│   └── js/              # JavaScript
├── tests/               # API tests
├── .github/workflows/   # CI/CD
├── vercel.json          # Vercel config
└── requirements.txt     # Python deps
```

## Technologies Used

- **Backend**: FastAPI, Python 3.12, Pydantic
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Vercel Serverless Functions
- **CI/CD**: GitHub Actions
- **Testing**: Pytest, FastAPI TestClient

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- TMNT characters and lore belong to their respective copyright holders
- Built with love for the heroes in a half shell!

---

**Cowabunga!** 🐢🍕