def collect_brace_content(text):
    content_list = []
    start = text.find('{')
    end = text.find('}', start)  # Find the closing brace after the opening brace

    while start != -1 and end != -1:
        # Extract content between the braces
        content = text[start + 1:end]
        
        # Add content to the list
        content_list.append(content)
        
        # Find the next `{` and `}`
        start = text.find('{', end)
        end = text.find('}', start)
    
    return content_list

# Example usage
text = "Hello {World}, this is {Python} and {}!"
content_between_braces = collect_brace_content(text)
print(content_between_braces)