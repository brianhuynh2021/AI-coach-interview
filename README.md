# AI Interview Coach

An intelligent AI-powered interview coaching platform designed to help candidates prepare for technical and behavioral interviews through realistic practice sessions, personalized feedback, and performance analytics.

## 🎯 Features

- **AI-Powered Interview Simulation**: Practice interviews with an intelligent AI coach
- **Real-time Feedback**: Get instant feedback on your responses
- **Multiple Interview Types**: Support for technical, behavioral, and case interviews
- **Performance Analytics**: Track your progress and identify areas for improvement
- **Customizable Scenarios**: Tailor interview sessions to specific roles and industries

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/brianhuynh2021/AI-coach-interview.git
cd AI-coach-interview
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`


## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: Lightning-fast ASGI server
- **Python-dotenv**: Environment variable management

## 🧪 Testing

```bash
# Run tests (to be implemented)
pytest
```

## 📝 Development

### Code Style

This project follows PEP 8 style guidelines. Format your code using:
```bash
black .
flake8 .
```

### Adding New Features

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Brian Huynh**
- GitHub: [@brianhuynh2021](https://github.com/brianhuynh2021)

## 🙏 Acknowledgments

- Thanks to all contributors who help improve this project
- Inspired by the need for accessible interview preparation tools

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

Made with ❤️ to help candidates succeed in their interviews