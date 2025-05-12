from jobspy import scrape_jobs
from davia import Davia
from fastapi import UploadFile
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from utils import read_uploaded_file, SYSTEM_PROMPT
import pandas as pd

from models import Job

# Initialize Davia app - Davia is a framework built on top of FastAPI
# that simplifies API development and adds additional features
app = Davia(title="Job Search")

# Configuration constants for job search
SITES = ["indeed", "glassdoor"]
RESULTS_WANTED = 30
HOURS_OLD = 72
MODEL = "gemini-2.0-flash"


# This decorator creates a FastAPI endpoint that will be accessible at /display_latest_jobs
# The task decorator converts this function into an API endpoint that can be called via HTTP
@app.task
def display_latest_jobs(job_title: str, job_location: str) -> list[Job | None]:
    """
    Scrapes and returns the latest job listings based on the given criteria.

    Args:
        job_title (str): The job title or role to search for (e.g., "Software Engineer")
        job_location (str): The location to search in (e.g., "San Francisco, CA")

    Returns:
        list[Job]: A list of Job objects containing the latest job listings matching the criteria.
        Each Job object contains:
            - title: Job title
            - description: Job description in Markdown format
            - company: Company name
            - location: Job location
            - job_url: URL to the job posting
            - date_posted: Date when the job was posted
    """
    # Scrape jobs from multiple job sites using jobspy
    jobs = scrape_jobs(
        site_name=SITES,
        search_term=job_title,
        location=job_location,
        results_wanted=RESULTS_WANTED,
        hours_old=HOURS_OLD,
    )

    # Convert DataFrame rows to Job objects
    job_list = []
    for _, row in jobs.iterrows():
        # Skip rows that have NaN values
        if row.isna().any():
            continue

        job = Job(**{col: str(row[col]) for col in jobs.columns})
        job_list.append(job)

    return job_list


# This decorator creates a FastAPI endpoint that will be accessible at /generate_cover_letter
# The task decorator converts this function into an API endpoint that can be called via HTTP
@app.task
def generate_cover_letter(job_description: str, resume: UploadFile) -> str:
    """
    Generates a tailored cover letter based on a job posting and the user's resume.

    This function uses AI to create a professional cover letter that is customized for the specific
    job posting and highlights relevant experience from the user's resume. The cover letter follows
    best practices including being concise, specific, and tailored to the role.

    Args:
        job_description (str): A string containing the job posting details including title, description,
            company, location, and other relevant information.
        resume (UploadFile): The user's resume file in PDF format.

    Returns:
        str: A markdown-formatted cover letter that is tailored to the specific job posting.

    """
    # Read and process the uploaded resume file
    resume = read_uploaded_file(resume)

    # Set up the AI model configuration
    system_prompt = SYSTEM_PROMPT
    model = GeminiModel(MODEL, provider="google-gla")

    # Prepare the instruction template for the AI model
    instruc = """
    Here is the job description:
    {job_description}

    Here is the resume:
    {resume}
    """

    # Initialize the AI agent with the configured model
    agent = Agent(
        model=model,
        system_prompt=system_prompt,
    )

    # Generate the cover letter using the AI model
    return agent.run_sync(
        instruc.format(job_description=job_description, resume=resume)
    ).output


if __name__ == "__main__":
    app.run()
