#"""Skills Assessment Agent for evaluating professional competencies."""

# Agent 2: Skills Assessment Agent
from __future__ import annotations

from typing import Any, Iterable, Optional

from crewai import Agent

from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    """You are an expert Skills Assessment Specialist with deep knowledge of professional competencies 
    across various industries. You evaluate technical skills, soft skills, and identify skill gaps. 
    You provide detailed assessments of current skill levels, market demand for specific skills, and 
    create personalized skill development roadmaps. You use industry frameworks and standards to ensure 
    accurate and actionable assessments."""
)


def create_skills_assessment_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    """Create the skills assessment agent for evaluating professional competencies."""
    return Agent(
        name="Skills Analyzer",
        role="Professional Skills Assessment Specialist",
        goal="Conduct comprehensive skills assessments, identify strengths and gaps, and create actionable skill development plans aligned with career goals",
        backstory=(
            "You are a certified skills assessment professional with expertise in competency frameworks, "
            "technical evaluations, and talent development. You have assessed thousands of professionals "
            "across diverse industries including technology, business, healthcare, and creative fields. "
            "Your assessments are known for being thorough, objective, and incredibly useful for career planning. "
            "You understand both current market demands and future skill trends."
        ),
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
