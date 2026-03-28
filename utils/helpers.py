import os

def save_blog_to_file(content, filename="outputs/generated_blogs.txt"):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n\n" + "="*50 + "\n\n")
            f.write(content)
        return True
    except Exception as e:
        return False


def word_count(text):
    return len(text.split())


def clean_text(text):
    return text.strip()


def estimate_readability(text):
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')

    if sentences == 0:
        return "Medium"

    avg_words = words / sentences

    if avg_words < 12:
        return "Easy"
    elif avg_words < 18:
        return "Medium"
    else:
        return "Hard"