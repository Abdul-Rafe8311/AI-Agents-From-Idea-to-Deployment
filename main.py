"""Entrypoint for running the Career Advisor AI pipeline end-to-end."""
from __future__ import annotations

import argparse
import logging

from dotenv import load_dotenv

from crew import run_career_advisor_pipeline
from config.logging_config import configure_logging


def run_pipeline(user_profile: str) -> str:
    """Run the configured career advisor crew against the provided user profile."""
    load_dotenv()
    configure_logging()
    logging.getLogger(__name__).info("Starting career advisor pipeline for user profile")
    return run_career_advisor_pipeline(user_profile)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Career Advisor AI crew pipeline.")
    parser.add_argument(
        "--profile",
        default="I am a software developer with 3 years of experience in Python and web development. I'm interested in transitioning to AI/ML engineering and want to understand what skills I need and how to build my resume for this career path.",
        help="User profile description including background, experience, interests, and career goals.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    output = run_pipeline(args.profile)
    print(output)
