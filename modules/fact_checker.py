def format_tech_fact(item):
    """
    Formats a Tech Fact post with an engaging 'Did you know' style.
    'index' provides a unique number for the fact.
    """
    fact = item.get("fact", "")
    raw_num = item.get("fact_number", "?")
    num = f"{int(raw_num):03}"
    tags = item.get("tags", "#TechFacts #Learning")
    
    return (
        f"💡 Tech Fact #{num}\n\n"
        f"Did you know? {fact}\n\n"
        f"{tags}"
    )