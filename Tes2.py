from phi.agent import Agent
from phi.model.openai import OpenAIChat

# Common Model
model = OpenAIChat(id="gpt-3.5-turbo")

# 1. Organizer Agent
organizer = Agent(
    name="Organizer",
    role="Meeting Organizer",
    model=model,
    instructions=[
        "Set the meeting agenda, select attendees, and schedule the time for an MS Teams meeting."
    ],
    markdown=False
)

# 2. Timekeeper Agent
timekeeper = Agent(
    name="Timekeeper",
    role="Time Manager",
    model=model,
    instructions=[
        "Ensure each topic stays within the allotted time and identify any overruns."
    ],
    markdown=False
)

# 3. Discussion Manager Agent
discussion_manager = Agent(
    name="Discussion Manager",
    role="Discussion Facilitator",
    model=model,
    instructions=[
        "Keep the conversation on track and ensure all agenda items are discussed in order."
    ],
    markdown=False
)

# 4. Minutes Recorder Agent
minutes_recorder = Agent(
    name="Minutes Recorder",
    role="Meeting Note Taker",
    model=model,
    instructions=[
        "Summarize the meeting transcript into concise notes and action items."
    ],
    markdown=False
)

# Simulated meeting input
meeting_topic = "Q2 Product Launch Planning"
transcript = """
John: Let's kick off with the landing page design. We need it by next Tuesday.
Sarah: I'll take that. Next, we should finalize pricing tiers.
Mike: Pricing will be sent to marketing by Friday.
Sarah: Great. Can we wrap this up in 10 minutes?
"""

# Step 1: Organizer sets the meeting plan
agenda_prompt = f"Plan a 30-minute MS Teams meeting on: {meeting_topic}"
agenda_response = organizer.run(agenda_prompt)
print("\n==== Organizer ====\n", agenda_response.content.strip())

# Step 2: Timekeeper reviews for time management
time_prompt = f"Evaluate the following conversation for time management:\n\n{transcript}"
time_response = timekeeper.run(time_prompt)
print("\n==== Timekeeper ====\n", time_response.content.strip())

# Step 3: Discussion Manager tracks the agenda
discussion_prompt = f"Analyze the following conversation and check if all agenda items are covered:\n\n{transcript}"
discussion_response = discussion_manager.run(discussion_prompt)
print("\n==== Discussion Manager ====\n", discussion_response.content.strip())

# Step 4: Minutes Recorder creates meeting notes
minutes_prompt = f"Create notes and action items from the following meeting:\n\n{transcript}"
minutes_response = minutes_recorder.run(minutes_prompt)
print("\n==== Minutes Recorder ====\n", minutes_response.content.strip())
