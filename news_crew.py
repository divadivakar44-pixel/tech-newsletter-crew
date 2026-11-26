
import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o-mini")

# Validate API keys
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing!")

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY is missing!")

# Configure the model
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# Create web search tool
search_tool = SerperDevTool()

# --------------------------------------------------
# AGENT 1: RESEARCHER
# --------------------------------------------------

researcher = Agent(
    role="Technology News Researcher",

    goal="Find today's three most important technology news stories.",

    backstory=(
        "You are an experienced technology news researcher. "
        "You search the internet for the latest technology news "
        "from reliable sources. You focus on AI, cybersecurity, "
        "cloud computing, software, startups and major technology companies. "
        "You provide accurate information with the source name and link."
    ),

    tools=[search_tool],

    llm=MODEL,

    verbose=True
)

# --------------------------------------------------
# AGENT 2: WRITER
# --------------------------------------------------

writer = Agent(
    role="Technology Newsletter Writer",

    goal="Create a clear and engaging five-line technology newsletter.",

    backstory=(
        "You are a professional technology newsletter writer. "
        "You convert research into a short, informative newsletter. "
        "You do not search the internet. You only use the research "
        "provided to you by the Researcher."
    ),

    llm=MODEL,

    verbose=True
)

# --------------------------------------------------
# TASK 1: RESEARCH
# --------------------------------------------------

research_task = Task(
    description=(
        "Search the internet for today's latest technology news. "
        "Find the three most important technology stories. "
        "Focus on AI, cybersecurity, cloud computing, software "
        "and major technology companies. "
        "For each story, provide a headline, a brief explanation "
        "and its source URL. Make sure the news is current."
    ),

    expected_output=(
        "Three technology news stories. Each story must contain "
        "a headline, a short explanation and a source URL. "
        "Organize the information clearly so the Writer can use it."
    ),

    agent=researcher
)

# --------------------------------------------------
# TASK 2: NEWSLETTER WRITING
# --------------------------------------------------

newsletter_task = Task(
    description=(
        "Use the research provided by the Researcher to create "
        "a technology newsletter. Include exactly three news stories. "
        "Each story must be summarized in one line. "
        "The newsletter must contain exactly five lines total: "
        "Line 1: Newsletter title. "
        "Lines 2, 3 and 4: Three technology news stories. "
        "Line 5: Why these stories matter. "
        "Do not add introductions, conclusions or extra lines."
    ),

    expected_output=(
        "Exactly five lines of text. "
        "Line 1 must be the title 'Tech in 5 Lines'. "
        "Lines 2-4 must contain three numbered news stories. "
        "Line 5 must start with 'Why it matters:'. "
        "Do not include any additional text."
    ),

    agent=writer,

    context=[research_task]
)

# --------------------------------------------------
# CREATE CREW
# --------------------------------------------------

tech_news_crew = Crew(
    agents=[researcher, writer],

    tasks=[research_task, newsletter_task],

    process=Process.sequential,

    verbose=True
)

# --------------------------------------------------
# EXECUTE CREW
# --------------------------------------------------

if __name__ == "__main__":

    print("\nStarting Tech Newsletter Crew...\n")

    result = tech_news_crew.kickoff()

    print("\n" + "=" * 50)
    print("FINAL TECHNOLOGY NEWSLETTER")
    print("=" * 50)

    print(result)

    print("\n" + "=" * 50)
    print("PROJECT EXECUTION COMPLETED")
    print("=" * 50)
