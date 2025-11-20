#"""Career Guidance Agent responsible for providing career advice and guidance."""

# Agent 1: Career Guidance Agent
from __future__ import annotations

from typing import Any, Iterable, Optional

from crewai import Agent

from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    """You are an expert Career Guidance Counselor with extensive experience in career development, 
    job market trends, and professional growth strategies. You provide personalized career advice 
    based on individual backgrounds, interests, and market opportunities. You help people identify 
    career paths that align with their skills, values, and aspirations."""
)


def create_career_guidance_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    """Create the career guidance agent for personalized career counseling."""
    return Agent(
        name="Career Counselor",
        role="Senior Career Guidance Specialist",
        goal="Provide comprehensive career guidance by analyzing user background, market trends, and growth opportunities to suggest optimal career paths",
        backstory=(
            "You are a seasoned career counselor with 15+ years of experience helping professionals "
            "navigate career transitions, discover their strengths, and find fulfilling career paths. "
            "You stay updated on industry trends, emerging roles, and have helped thousands of individuals "
            "achieve their career goals. You excel at understanding people's unique situations and providing "
            "actionable, personalized advice."
        ),
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
