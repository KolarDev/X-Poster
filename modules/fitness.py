def format_fitness(item):
    """Formats daily workout or health tips."""
    topic = item.get("topic", "Daily Fitness")
    body = item.get("body", "Keep moving!")
    
    # Pad the part number to 3 digits (e.g., 001)
    raw_count = item.get("count", 0)
    part = f"{int(raw_count):03}"
    
    tags = item.get("tags", "#Fitness #Health #DailyWorkout")
    
    return f"🏋️ Fitness Series: Part {part}\n\n🔹 Topic: {topic}\n\n{body}\n\n{tags}"