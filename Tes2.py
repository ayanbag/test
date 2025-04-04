
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

# Initialize the language model
llm = OpenAIChat(model="gpt-4")

# Define the assistant with specific instructions
meeting_assistant = Assistant(
    llm=llm,
    instructions=[
        "You are a Meeting Organizer Assistant responsible for planning and overseeing productive MS Teams meetings.",
        "Your tasks include creating agendas, assigning roles, monitoring time, managing discussions, and summarizing key points.",
        "Ensure all tasks are completed efficiently and provide clear outputs for each."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Example prompts to interact with the assistant
prompts = [
    "Plan a 45-minute MS Teams meeting covering project updates, budget discussion, and action items.",
    "Monitor the timing of each meeting topic and ensure they stay within the allotted time.",
    "Track and highlight key discussion points, decisions made, and action items assigned.",
    "Summarize the entire meeting including agenda, major discussion points, and action items."
]

# Execute the prompts and display responses
for prompt in prompts:
    print(f"\nPrompt: {prompt}\n")
    meeting_assistant.print_response(prompt, stream=True)
