def format_system_design(item):
    """
    Formats a System Design post with a professional structure.
    'item' is the dictionary from your JSON.
    'count' is the current number in the series.
    """
    topic = item.get("topic", "System Design")
    body = item.get("body", "")
    count = item.get("count", "?")
    tags = item.get("tags", "#SystemDesign #Architecture")
    
    return (
        f"🏗️ System Design {count}\n\n"
        f"🔹 {topic}\n\n"
        f"{body}\n\n"
        f"{tags}"
    )