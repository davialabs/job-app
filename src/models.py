from pydantic import BaseModel


class Job(BaseModel):
    title: str
    description: str
    company: str
    location: str
    job_url: str
    date_posted: str
