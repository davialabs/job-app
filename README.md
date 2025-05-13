# Job Search & Cover Letter Assistant

This project provides a set of tools to help with the job application process. It can:

1.  **Scrape job listings**: Fetch the latest job postings from various job boards based on your search criteria.
2.  **Generate cover letters**: Automatically create tailored cover letters using AI, based on a job description and your resume.

This application is built using the **Davia** framework, which helps create a complete app directly from your Python backend logic. You can find more information about Davia in our [official documentation](https://docs.davia.ai/introduction).

## Features

- Searches for jobs on multiple platforms (e.g., Indeed, Glassdoor).
- Filters jobs by title, location, and how recently they were posted.
- Parses PDF resumes to extract relevant information.
- Uses a Gemini AI model to generate professional and customized cover letters.
- Provides API endpoints for easy integration and usage.

## Project Structure

```
.
├── .env_example
├── .gitignore
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── job_search.py  # Main application logic with FastAPI endpoints
│   ├── models.py      # Pydantic models (e.g., Job)
│   └── utils.py       # Utility functions (e.g., PDF reader, AI prompt)
└── .venv/             # Virtual environment (if created)
```

## Technologies Used

- **Davia**: A framework that creates a complete app (including UI) directly from your Python backend. See [Davia Documentation](https://docs.davia.ai/introduction).
  - Underlying API built with **FastAPI**.
- **JobSpy**: For scraping job listings. ([GitHub Repository](https://github.com/speedyapply/JobSpy))
- **Pydantic & Pydantic-AI**: For data validation and AI model interaction.
- **Google Gemini**: As the AI model for cover letter generation.
- **PyMuPDF**: For reading PDF resumes.
- **Pandas**: For data manipulation.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/davialabs/job-app
    cd job-app
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    - Rename `.env_example` to `.env`.
      ```bash
      mv .env_example .env  # On Windows: rename .env_example .env
      ```
    - Open the `.env` file and add your Gemini API Key:
      ```
      GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_API_KEY
      ```
      You can obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Running the Application

To start the backend application, run:

```bash
python src/job_search.py
```

This will typically start a Uvicorn server, and you should see output indicating the address where the API is running.

Davia is designed to create a visual application around your Python tasks, so you can also interact with the application's functionalities through the Davia interface once it's set up with your Davia account.

## API Endpoints (Backend Tasks)

The application's core logic is exposed as backend tasks, which Davia can build a user interface around. You can also interact with them directly as API endpoints:

- **To search for jobs**: Trigger the `display_latest_jobs` task/endpoint with your desired job title and location.
- **To generate a cover letter**: Trigger the `generate_cover_letter` task/endpoint, providing the job description text and uploading your resume PDF.

## How to Use

1.  **Start the backend application** as described in the "Running the Application" section.
2.  **Interact with the application:**
    - **Via Davia's Visual Interface**: If you have connected this project to your Davia account, you can use the visual editor and the generated app to run the tasks.
    - **Via API Client**: Alternatively, use an API client (like Postman, Insomnia, or `curl`) to interact with the backend endpoints directly as described above.
