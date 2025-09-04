from crewai import Agent, Crew, Process, Task , LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools import BaseTool 
from crewai_tools import  ScrapeWebsiteTool
from typing import List, Type
from pydantic import BaseModel, Field
from tools.browser_tools import scrape_and_summarize_website
from tools.calculator_tools import calculate
from tools.search_tools import search_internet

from textwrap import dedent
from datetime import date
from dotenv import load_dotenv
load_dotenv()


@CrewBase
class TravelPlaning:
    """TravelPlanning crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    
    
    Ollama_LLM = LLM(
    model="ollama/mistral",        # full model name
    base_url="http://localhost:11434"  # Ollama server URL
    )
     
     
     

    # ---------- Agents ----------
    @agent
    def city_selection_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['city_selection_agent'],
            tools=[
                search_internet,
                scrape_and_summarize_website
            ],
            llm=self.Ollama_LLM,
            verbose=True
        )

    @agent
    def local_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['local_expert'],
            tools=[
                search_internet,
                scrape_and_summarize_website
            ],
            llm=self.Ollama_LLM,
            verbose=True
        )

    @agent
    def travel_concierge(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_concierge'],
            tools=[
                search_internet,
               scrape_and_summarize_website,
                calculate
            ],
            llm=self.Ollama_LLM,
            verbose=True
        )

    # ---------- Tasks ----------
    @task
    def identify_task(self) -> Task:
        return Task(
            config=self.tasks_config['identify_task'],
            agent=self.city_selection_agent(),
            expected_output="Detailed report on the chosen city including flight costs, weather forecast, and attractions"
        )
        
    @task
    def gather_task(self) -> Task:
        return Task(
           config=self.tasks_config['gather_task'],
           agent=self.local_expert(),
           expected_output="Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips"
        )
    
    @task
    def plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_task'],
            agent=self.travel_concierge(),
            expected_output="Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown"
        )

    # ---------- Crew ----------
    @crew
    def crew(self) -> Crew:
        """Creates the TravelPlanning crew"""
        return Crew(
            agents=self.agents,  # from @agent decorators
            tasks=self.tasks,    # from @task decorators
            process=Process.sequential,
            verbose=True,
        )