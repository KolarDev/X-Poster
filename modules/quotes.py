def format_quotes(item):
    """Formats inspirational or book quotes."""
    author = item.get("author", "Unknown")
    quote = item.get("quote", "")
    source = item.get("book", "Wise Words")
    
    # Pad the quote number to 3 digits
    raw_count = item.get("count", 0)
    num = f"{int(raw_count):03}"
    
    tags = item.get("tags", "#Reading #Inspiration #Quotes")
    
    return f"📖 Book Quote #{num}\n\n\"{quote}\"\n\n— {author} ({source})\n\n{tags}"