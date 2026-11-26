
# Tech Newsletter Crew

## Project Overview

An AI-powered technology newsletter generator built using CrewAI.

The project uses two AI agents working sequentially to research current technology news and generate a concise five-line newsletter.

## Architecture

### Agent 1 - Researcher
- Searches the internet using SerperDevTool
- Finds the top three technology news stories
- Provides headlines, summaries and source links

### Agent 2 - Writer
- Receives the research output from the Researcher
- Converts the research into a newsletter
- Does not have web-search tools

## Workflow

Researcher -> Serper Web Search -> Research Output -> Writer -> Five-Line Newsletter

## Technologies Used

- Python
- CrewAI
- CrewAI Tools
- Serper API
- OpenAI API
- VS Code
- Git
- GitHub

## Project Files

- `news_crew.py` - Main Python application
- `requirements.txt` - Python dependencies
- `.env` - API keys (not uploaded to GitHub)
- `screenshots/` - Project execution screenshot

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/tech-newsletter-crew.git
cd tech-newsletter-crew
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API keys

Create a `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
MODEL=gpt-4o-mini
```

### 6. Run the project

```bash
python news_crew.py
```

## Output

The application generates a five-line technology newsletter containing:

1. Newsletter title
2. Technology news story 1
3. Technology news story 2
4. Technology news story 3
5. Why the news matters

## Author

Diwakar V
