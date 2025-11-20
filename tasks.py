#"""Task definitions for the Career Advisor crew."""
from __future__ import annotations

from typing import List

from crewai import Task

from tools import create_calculator_tool, create_rag_tool, create_web_search_tool


def create_career_guidance_task(agent) -> Task:
    """Task 1: Provide comprehensive career guidance and path recommendations."""
    return Task(
        description=(
            "Analyze the user's career profile including their background, interests, experience, and goals from '{user_profile}'. "
            "Research current job market trends, emerging opportunities, and growth potential in relevant fields. "
            "Provide personalized career path recommendations that align with their strengths, values, and aspirations. "
            "Consider short-term and long-term career goals, work-life balance preferences, and industry outlook."
        ),
        expected_output=(
            "A comprehensive career guidance report with: 1) Summary of user's career profile and aspirations, "
            "2) 3-5 recommended career paths with detailed justifications, 3) Market trends and opportunities analysis, "
            "4) Pros and cons for each path, 5) Actionable next steps for exploring each option."
        ),
        agent=agent,
        name="Career Guidance Analysis",
    )


def create_skills_assessment_task(agent, tools=None) -> Task:
    """Task 2: Assess current skills and identify gaps."""
    tools = list(tools) if tools is not None else [
        create_rag_tool(),
        create_web_search_tool(),
        create_calculator_tool(),
    ]
    return Task(
        description=(
            "Conduct a thorough skills assessment based on the user's profile '{user_profile}' and the recommended career paths. "
            "Evaluate technical skills, soft skills, and domain knowledge. Research in-demand skills for target roles using "
            "the RAG knowledge base and web search. Identify skill gaps between current capabilities and target role requirements. "
            "Prioritize skills based on market demand, learning curve, and career impact."
        ),
        expected_output=(
            "A detailed skills assessment report containing: 1) Current skills inventory with proficiency levels, "
            "2) In-demand skills for target career paths with market data, 3) Identified skill gaps prioritized by importance, "
            "4) Skill development roadmap with timeline estimates, 5) Quick wins vs. long-term skill building strategies."
        ),
        agent=agent,
        tools=tools,
        name="Skills Assessment",
    )


def create_resume_building_task(agent) -> Task:
    """Task 3: Build or optimize resume for target roles."""
    return Task(
        description=(
            "Create a professional, ATS-optimized resume based on '{user_profile}' tailored for the recommended career paths. "
            "Structure the resume to highlight relevant achievements, quantifiable results, and key skills. "
            "Use powerful action verbs and industry-specific keywords. Ensure proper formatting for both ATS systems and human readers. "
            "Include sections for: professional summary, work experience, skills, education, and certifications. "
            "Provide both a master resume and variations optimized for different target roles."
        ),
        expected_output=(
            "A complete, professionally formatted resume (or multiple versions for different career paths) with: "
            "1) Compelling professional summary, 2) Achievement-focused work experience with metrics, "
            "3) Skills section aligned with target roles, 4) Education and certifications, "
            "5) ATS optimization tips and keywords, 6) Additional suggestions for LinkedIn profile optimization."
        ),
        agent=agent,
        name="Resume Building",
    )


def create_course_recommendation_task(agent) -> Task:
    """Task 4: Recommend courses and learning resources."""
    return Task(
        description=(
            "Based on the skills assessment and career goals from '{user_profile}', recommend specific courses, certifications, "
            "and learning resources to bridge skill gaps and advance toward target career paths. "
            "Research the most effective and reputable courses from platforms like Coursera, Udemy, edX, LinkedIn Learning, "
            "and university programs. Consider learning style, budget, time commitment, and ROI. "
            "Create a structured learning path with short-term and long-term milestones."
        ),
        expected_output=(
            "A personalized learning roadmap featuring: 1) Prioritized list of recommended courses with platform, duration, and cost, "
            "2) Relevant certifications that boost employability, 3) Free vs. paid resource alternatives, "
            "4) Structured learning timeline (3-month, 6-month, 12-month plans), "
            "5) Project ideas for practical application, 6) Community resources and networking opportunities."
        ),
        agent=agent,
        name="Course Recommendations",
    )


def build_career_advisor_tasks(career_guidance_agent, skills_agent, resume_agent, course_agent, assessment_tools=None) -> List[Task]:
    """Convenience helper to create the full career advisor task list."""
    return [
        create_career_guidance_task(career_guidance_agent),
        create_skills_assessment_task(skills_agent, tools=assessment_tools),
        create_resume_building_task(resume_agent),
        create_course_recommendation_task(course_agent),
    ]
