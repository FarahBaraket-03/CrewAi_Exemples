#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from textwrap import dedent
from travel_planing.crew import TravelPlaning

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from dotenv import load_dotenv
load_dotenv()


def run(origin, cities, date_range, interests):
    """
    Run the crew with user inputs.
    """
    inputs = {
        "origin": origin,
        "cities": cities,
        "range": date_range,
        "interests": interests,
        "current_year": str(datetime.now().year)
    }

    try:
        TravelPlaning().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')

    origin = input(
        dedent("""
        From where will you be traveling from?
        > """))
    cities = input(
        dedent("""
        What are the cities options you are interested in visiting?
        (comma separated, e.g., Paris, Rome, Tokyo)
        > """))
    date_range = input(
        dedent("""
        What is the date range you are interested in traveling?
        (e.g., 2025-09-15 to 2025-09-25)
        > """))
    interests = input(
        dedent("""
        What are some of your high level interests and hobbies?
        (e.g., history, food, nightlife, hiking)
        > """))

    # Run the crew with collected inputs
    run(origin, cities, date_range, interests)
    
    