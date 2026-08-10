import os
from pathlib import Path
from dotenv import load_dotenv

def load_config() -> None:

    # Get project root and var location
    project_root = Path(__file__).resolve().parents[2]
    env_path = project_root / "vars" / ".env"

    # Load the .env file
    load_dotenv(env_path)

    # Access the variables
    print(os.getenv("TEST_VAR"))