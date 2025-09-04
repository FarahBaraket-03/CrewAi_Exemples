from crewai import Agent, Crew, Process, Task , LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class GameBuilder():
    """GameBuilder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    
    Ollama_LLM = LLM(
    model="ollama/mistral",        # full model name
    base_url="http://localhost:11434"  # Ollama server URL
    )
    
    #!------------------------------ AGENTS -----------------------------------
    
    @agent
    def senior_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_engineer_agent'],
            allow_delegation=False,
            llm=self.Ollama_LLM,
            verbose=True
        )
    
    @agent
    def qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer_agent'],
            allow_delegation=False,
            llm=self.Ollama_LLM,
            verbose=True
        )
    
    @agent
    def chief_qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_qa_engineer_agent'],
            allow_delegation=True,
            llm=self.Ollama_LLM,
            verbose=True
        )
    
    
    
    #! ------------------------------- TASKS -------------------------------------------------------
    
    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'],
            agent=self.senior_engineer_agent()
        )

    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'],
            agent=self.qa_engineer_agent(),
            #### output_json=ResearchRoleRequirements
        )

    @task
    def evaluate_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_task'],
            agent=self.chief_qa_engineer_agent()
        )


    
   

    @crew
    def crew(self) -> Crew:
        """Creates the GameBuilder crew"""
        

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
