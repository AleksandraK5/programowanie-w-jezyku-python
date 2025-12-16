def is_palindrome(text: str) -> bool:
    cleaned_text = ''.join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]
