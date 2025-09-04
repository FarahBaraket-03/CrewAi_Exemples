#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import NewsScraper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year),
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }
    
    try:
        NewsScraper().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()