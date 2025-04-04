
from crewai import Agent, Crew, Task
from langchain_openai import ChatOpenAI

# Set up LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.5)

# Define Agents
organizer = Agent(
    role="Meeting Organizer",
    goal="Plan and oversee a productive MS Teams meeting.",
    backstory="An experienced project manager ensuring structured discussions.",
    allow_delegation=True,
    verbose=True,
    llm=llm
)

timekeeper = Agent(
    role="Timekeeper",
    goal="Ensure all topics are discussed within the allocated time.",
    backstory="A strict but fair facilitator ensuring efficient meetings.",
    verbose=True,
    llm=llm
)

discussion_manager = Agent(
    role="Discussion Manager",
    goal="Identify key discussion points and flag action items.",
    backstory="A proactive listener who ensures all voices are heard.",
    verbose=True,
    llm=llm
)

minutes_recorder = Agent(
    role="Minutes Recorder",
    goal="Summarize key takeaways, action items, and next steps.",
    backstory="An organized scribe known for capturing meeting highlights.",
    verbose=True,
    llm=llm
)

# Define Tasks
task1 = Task(
    description="Plan a 45-minute MS Teams meeting covering project updates, budget discussion, and action items. Coordinate roles for timekeeping, managing discussions, and note-taking.",
    expected_output="Meeting agenda and team member task assignments.",
    agent=organizer
)

task2 = Task(
    description="Monitor the timing of each meeting topic and ensure they stay within the allotted time.",
    expected_output="Time logs for each topic with any timing issues flagged.",
    agent=timekeeper
)

task3 = Task(
    description="Track and highlight key discussion points, decisions made, and action items assigned.",
    expected_output="List of decisions, questions raised, and action items with owners.",
    agent=discussion_manager
)

task4 = Task(
    description="Summarize the entire meeting including agenda, major discussion points, and action items.",
    expected_output="Formatted meeting summary ready to be shared via email or Teams.",
    agent=minutes_recorder
)

# Assemble the Crew
crew = Crew(
    agents=[organizer, timekeeper, discussion_manager, minutes_recorder],
    tasks=[task1, task2, task3, task4],
    verbose=2
)

# Run the Crew
result = crew.kickoff()

print("\n===== Final Meeting Summary =====\n")
print(result)
