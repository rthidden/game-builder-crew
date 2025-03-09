"""This file contains the crew definition for the GameBuilder crew"""
from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class GameBuilderCrew:
    """GameBuilder crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def senior_engineer_agent(self) -> Agent:
        """Creates the Senior Engineer Agent"""
        return Agent(config=self.agents_config['senior_engineer_agent'])

    @agent
    def qa_engineer_agent(self) -> Agent:
        """Creates the QA Engineer Agent"""
        return Agent(config=self.agents_config['qa_engineer_agent'])

    @agent
    def chief_qa_engineer_agent(self) -> Agent:
        """Creates the Chief QA Engineer Agent"""
        return Agent(config=self.agents_config['chief_qa_engineer_agent'])

    @task
    def code_task(self) -> Task:
        """Creates the Code Task"""
        return Task(
            config=self.tasks_config['code_task'],
            agent=self.senior_engineer_agent()
        )   

    @task
    def review_task(self) -> Task:
        """Creates the Review Task"""
        return Task(
            config=self.tasks_config['review_task'],
            agent=self.qa_engineer_agent(),
            #### output_json=ResearchRoleRequirements
        )

    @task
    def evaluate_task(self) -> Task:
        """Creates the Evaluate Task"""
        return Task(
            config=self.tasks_config['evaluate_task'],
            agent=self.chief_qa_engineer_agent()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the GameBuilderCrew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
