import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.tools.exa import ExaTools

import os
import phi
from phi.playground import Playground, serve_playground_app
# Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## web search agent
web_search_agent=Agent(
    name="Web Search New Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI New Agent",
    model=Groq(id="llama-3.1-70b-versatile"),
    role="analyse financial data for long run",
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use bullet points to display the data"],
    show_tool_calls=True,
    markdown=True,

)

##weekend planner Agent
weekend_agent = Agent(
    description="you help the user plan their weekends",
    name="Weekend plan",
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=[
        "You are a weekend planning assistant that helps users create a personalized weekend itinerary.",
        "Always mention the timeframe, location, and year provided by the user (e.g., '16–17 December 2023 in Bangalore'). Recommendations should align with the specified dates.",
        "Provide responses in these sections: Events, Activities, Dining Options.",
        "- **Events**: Include name, date, time, location, a brief description, and booking links from platforms like BookMyShow or Insider.in.",
        "- **Activities**: Suggest engaging options with estimated time required, location, and additional tips (e.g., best time to visit).",
        "- **Dining Options**: Recommend restaurants or cafés with cuisine highlights and links to platforms like Zomato or Google Maps.",
        "Ensure all recommendations are for the current or future dates relevant to the query. Avoid past events.",
        "If no specific data is available for the dates, suggest general activities or evergreen attractions in the city.",
        "Keep responses concise, clear, and formatted for easy reading.",
    ],
    tools=[ExaTools()],
)

app=Playground(agents=[finance_agent,web_search_agent,weekend_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)

