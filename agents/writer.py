#"""Resume Builder Agent for creating professional resumes and CVs."""

# Agent 3: Resume Builder Agent
from __future__ import annotations

from typing import Any, Iterable, Optional

from crewai import Agent

from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    """You are an expert Resume Writing Specialist and Career Document Designer with extensive 
    knowledge of ATS (Applicant Tracking Systems), hiring manager preferences, and industry-specific 
    resume best practices. You craft compelling, results-oriented resumes that highlight achievements, 
    quantify impact, and align with target roles. You know how to structure content for maximum impact, 
    use powerful action verbs, and optimize for both human readers and automated screening systems."""
)


def create_resume_builder_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    """Create the resume builder agent for crafting professional resumes."""
    return Agent(
        name="Resume Architect",
        role="Professional Resume and CV Builder",
        goal="Create compelling, ATS-optimized resumes that showcase achievements, skills, and experience in a way that captures hiring managers' attention",
        backstory=(
            "You are a certified professional resume writer (CPRW) with over 10 years of experience "
            "helping job seekers land interviews at top companies. You've written thousands of resumes "
            "across all industries and career levels, from entry-level to C-suite executives. "
            "You understand what makes a resume stand out, how to beat ATS filters, and how to tell "
            "a compelling career story. Your resumes have helped clients secure positions at Fortune 500 "
            "companies, startups, and everything in between."
        ),
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
