# AI Career Advisor - Multi-Agent System

An intelligent career advisor powered by AI agents that provides personalized career guidance, skills assessment, resume building, and course recommendations.

## Overview

This project uses CrewAI to orchestrate four specialized AI agents that work together to provide comprehensive career advice:

1. **Career Guidance Agent** - Analyzes career profiles and recommends optimal career paths
2. **Skills Assessment Agent** - Evaluates current skills and identifies gaps for target roles
3. **Resume Builder Agent** - Creates ATS-optimized resumes tailored to career goals
4. **Course Recommendation Agent** - Suggests personalized learning paths and resources

## Features

- 🎯 Personalized career path recommendations based on experience and goals
- 📊 Comprehensive skills assessment with gap analysis
- 📄 Professional, ATS-optimized resume generation
- 📚 Curated course recommendations with structured learning roadmaps
- 🔍 RAG-powered knowledge base with career development insights
- 🌐 Web search integration for current market trends
- 🖥️ Interactive Streamlit frontend

## Architecture

The system uses:
- **CrewAI**: Multi-agent orchestration framework
- **LangChain**: LLM integration and tool chaining
- **FAISS**: Vector database for career knowledge retrieval
- **OpenRouter**: Unified API for multiple LLM models (Meta Llama 3.3 70B)
- **Streamlit**: Interactive web interface

## Project Structure

```
AI-Agents-From-Idea-to-Deployment/
├── agents/                    # Agent definitions
│   ├── planner.py            # Career Guidance Agent
│   ├── researcher.py         # Skills Assessment Agent
│   ├── writer.py             # Resume Builder Agent
│   └── reviewer.py           # Course Recommendation Agent
├── config/                   # Configuration
│   ├── settings.py          # LLM and API settings
│   └── logging_config.py    # Logging configuration
├── tools/                    # Agent tools
│   ├── calculator.py        # Arithmetic calculations
│   ├── rag_tool.py          # Career knowledge retrieval
│   └── web_search.py        # Live web search (DuckDuckGo)
├── rag/                      # RAG pipeline
│   ├── build_vector_db.py   # Vector store builder
│   └── documents/           # Knowledge base documents
│       └── career_knowledge_base.txt
├── frontend/                 # Streamlit UI
│   └── app.py
├── crew.py                   # Crew orchestration
├── tasks.py                  # Task definitions
├── main.py                   # CLI entrypoint
└── requirements.txt          # Python dependencies
```

## Agent Details

### 1. Career Guidance Agent
- Analyzes user background, interests, and goals
- Researches market trends and opportunities
- Recommends 3-5 optimal career paths with justifications
- Provides actionable next steps

### 2. Skills Assessment Agent
- Evaluates technical and soft skills
- Identifies skill gaps for target roles
- Prioritizes skills by market demand
- Creates structured development roadmap with timelines

### 3. Resume Builder Agent
- Generates professional, ATS-optimized resumes
- Highlights achievements with quantifiable metrics
- Tailors content for specific career paths
- Provides LinkedIn optimization tips

### 4. Course Recommendation Agent
- Recommends courses from top platforms (Coursera, Udemy, edX)
- Suggests relevant certifications (AWS, Azure, Google Cloud)
- Creates 3/6/12-month learning timelines
- Includes free and paid resource alternatives

## Prerequisites

- Python 3.10+
- OpenRouter API key ([Get one here](https://openrouter.ai/))
- Virtual environment manager (venv, conda, or pipenv)

## Installation

1. **Clone the repository**
   ```powershell
   git clone <repository-url>
   cd AI-Agents-From-Idea-to-Deployment
   ```

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

5. **Build the vector database**
   ```powershell
   python rag\build_vector_db.py
   ```
   This processes `career_knowledge_base.txt` and creates a FAISS vector store.

## Usage

### Command Line Interface

Run the career advisor with a user profile:

```powershell
python main.py --profile "I am a software developer with 3 years of experience in Python and web development. I'm interested in transitioning to AI/ML engineering."
```

### Streamlit Web Interface

Launch the interactive web app:

```powershell
python -m streamlit run frontend\app.py
```

Then open `http://localhost:8501` and enter your career profile.

## Example User Profiles

**Career Transition:**
```
I'm a marketing manager with 5 years of experience. I want to transition into product management in tech. I have basic SQL skills and strong communication abilities.
```

**Skill Upgrade:**
```
Backend developer with 2 years Java/Spring experience. Want to learn cloud architecture and get AWS certified to move into senior roles.
```

**Career Starter:**
```
Recent computer science graduate. Strong in Python and algorithms. Interested in data science or machine learning engineering. Need guidance on first role.
```

## Configuration

### LLM Settings

Edit `config/settings.py` to customize:
- Model selection (default: Meta Llama 3.3 70B)
- Temperature and max tokens
- Fallback models and base URLs

### Knowledge Base

The career knowledge base includes:
- Career paths and opportunities across tech roles
- Skills assessment frameworks and in-demand skills
- Resume building best practices and ATS optimization
- Course recommendations and learning platforms
- Job search strategies and interview preparation
- Industry insights and salary information

To add custom content:
1. Add `.txt` files to `rag/documents/`
2. Rebuild vector store: `python rag\build_vector_db.py`

## Customization

### Adding New Agents

1. Create agent file in `agents/` with system prompt, role, goal, backstory
2. Add import to `agents/__init__.py`
3. Update `crew.py` to include in crew assembly
4. Add corresponding task in `tasks.py`

### Adding New Tools

1. Create tool class in `tools/` extending `BaseTool`
2. Implement `_run()` method
3. Add to `tools/__init__.py`
4. Include in `get_default_toolkit()` if needed for all agents

## Troubleshooting

**Vector store not found:**
```powershell
python rag\build_vector_db.py
```

**API key errors:**
Ensure `.env` contains valid `OPENROUTER_API_KEY`

**Import errors:**
```powershell
pip install -r requirements.txt
```

**Streamlit connection issues:**
Use `python -m streamlit run frontend\app.py` instead of direct `streamlit` command

## Technologies Used

- **CrewAI 0.37+**: Agent orchestration
- **LangChain**: LLM framework and tools
- **OpenRouter**: Multi-model API access
- **FAISS**: Vector similarity search
- **Sentence Transformers**: Text embeddings
- **DuckDuckGo Search**: Web search integration
- **Streamlit**: Web interface
- **Python 3.10+**: Core language

## Deployment

### Streamlit Community Cloud
1. Push repository to GitHub
2. Connect to Streamlit Cloud
3. Set `OPENROUTER_API_KEY` in secrets
4. Deploy from `frontend/app.py`

### Docker Containerization
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python rag/build_vector_db.py
EXPOSE 8501
CMD ["streamlit", "run", "frontend/app.py"]
```

### Cloud Platforms
- **Azure**: Azure Container Apps or App Service
- **AWS**: ECS, App Runner, or Lambda
- **GCP**: Cloud Run or App Engine

## Development Roadmap

Future enhancements:
- [ ] Integration with LinkedIn API for profile import
- [ ] PDF resume export with customizable templates
- [ ] Email delivery of career reports
- [ ] Multi-language support
- [ ] Interview preparation module
- [ ] Salary negotiation guidance
- [ ] Job matching recommendations
- [ ] Progress tracking dashboard

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

## License

See LICENSE file for details.

## Acknowledgments

Built with CrewAI, LangChain, and OpenRouter for intelligent career guidance through multi-agent AI systems.

---

**Need career advice?** Run the system and let our AI agents help guide your career journey! 🚀
