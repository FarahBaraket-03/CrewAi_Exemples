from crewai import Agent, Crew, Process, Task ,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool , ScrapeWebsiteTool , FileWriterTool
from typing import List ,Dict , Any
from dotenv import load_dotenv

load_dotenv()



@CrewBase
class NewsScraper():
    """NewsScraper crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    
    Ollama_LLM = LLM(
    model="ollama/mistral",        # full model name
    base_url="http://localhost:11434"  # Ollama server URL
    )

    @agent
    def retreive_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retreive_news'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()],  # Use the SerperDevTool instance
            llm=self.Ollama_LLM,  # Use the Ollama LLM instance 
            # Add explicit instructions
        instructions="When using the search tool, provide the query as a plain string. Example: 'Latest AI LLM developments in 2025'"
        )

    @agent
    def web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['web_scraper'], # type: ignore[index]
            verbose=True,
            llm=self.Ollama_LLM,
            tools=[ScrapeWebsiteTool()]  # Assuming you want to use the same tool
        )
        
    @agent
    def ai_new_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_new_writer'], # type: ignore[index]
            verbose=True,
            llm=self.Ollama_LLM,
            tools=[]  # Assuming you want to use the same tool
        )

    
    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'], # type: ignore[index]
            verbose=True,
            llm=self.Ollama_LLM,
            tools=[FileWriterTool()],
            # Assuming you want to use the same tool
            instructions="""
        When saving files:
        1. Always include the full path including 'news/' directory in the filename
        2. The File Writer Tool will automatically create directories if needed
        
        """
        )

    
    
    @task
    def retreive_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['retreive_news_task'], # type: ignore[index]
        )

    @task
    def website_scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['website_scraper_task'], # type: ignore[index
        )
        
        
    @task
    def ai_news_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_writer_task'], # type: ignore[index
        )
            
    
    @task
    def file_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['file_writer_task'], # type: ignore[index
        )
        
    
        
    @crew
    def crew(self) -> Crew:
        """Creates the NewsScraper crew"""
        

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
