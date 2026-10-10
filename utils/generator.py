import anthropic

def generate_agenda(api_key: str, topic: str, description: str, duration: int) -> str:
    """
    Generates a meeting agenda using Anthropic's Claude model.
    """
    if not api_key:
        raise ValueError("Anthropic API key is required.")
        
    if api_key.lower() == "demo":
        return f"""# 📝 Meeting Agenda: {topic}
**Duration**: {duration} minutes

### 1. 🧊 Icebreaker & Welcome (5 mins)
- Quick check-in with all attendees.
- Review meeting objectives: {description}

### 2. 📊 Status Updates (15 mins)
- Round-robin updates from team leads.
- Blockers and challenges.

### 3. 🎯 Deep Dive: {topic} ({(duration - 30) if duration > 30 else 5} mins)
- Open discussion on main topic.
- Action items mapping.

### 4. 🏁 Wrap-up & Next Steps (10 mins)
- Assign action items.
- Confirm date for next sync.
"""

    client = anthropic.Anthropic(api_key=api_key)
    
    prompt = f"""
You are an expert meeting facilitator and productivity coach. 
Please create a detailed, professional meeting agenda based on the following information:

Topic: {topic}
Description/Goals: {description}
Total Meeting Duration: {duration} minutes

Requirements:
1. Organize the agenda logically.
2. Provide an estimated time duration for each agenda item. Make sure the total time does not exceed {duration} minutes.
3. Output the agenda in clean Markdown format.
4. Do not include any introductory or concluding pleasantries, just the Markdown agenda.
"""
    
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text
