from crewai import Agent, Crew
from langchain_openai import ChatOpenAI

# Setup LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.5)  # Balanced for precision & clarity

# Master Agent - Meeting Organizer
organizer = Agent(
    role="Meeting Organizer",
    goal="Plan and oversee a productive MS Teams meeting.",
    backstory="An experienced project manager ensuring structured discussions.",
    allow_delegation=True,  # Assigns tasks dynamically
    verbose=True,
    llm=llm
)

# Timekeeper Agent
timekeeper = Agent(
    role="Timekeeper",
    goal="Ensure all topics are discussed within the allocated time.",
    backstory="A strict but fair facilitator ensuring efficient meetings.",
    verbose=True,
    llm=llm
)

# Discussion Manager
discussion_manager = Agent(
    role="Discussion Manager",
    goal="Identify key discussion points and flag action items.",
    backstory="A proactive listener who ensures all voices are heard.",
    verbose=True,
    llm=llm
)

# Minutes Recorder
minutes_recorder = Agent(
    role="Minutes Recorder",
    goal="Summarize key takeaways, action items, and next steps.",
    backstory="An organized scribe known for capturing meeting highlights.",
    verbose=True,
    llm=llm
)

# Crew with Delegation
crew = Crew(
    agents=[organizer, timekeeper, discussion_manager, minutes_recorder],
    tasks=[
        organizer.task(
            description="Plan the meeting agenda, ensure a structured discussion, and delegate roles.",
            expected_output="A well-organized meeting plan with a summary of discussions and action items."
        )
    ],
    verbose=2  # Detailed logs
)

# Run the Meeting Simulation
result = crew.kickoff()

print("\n===== Final Meeting Summary =====\n")
print(result)
