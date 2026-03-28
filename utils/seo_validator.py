def calculate_seo_score(blog_text, keyword):
    score = 0

    if keyword.lower() in blog_text.lower():
        score += 20

    if len(blog_text.split()) >= 700:
        score += 20

    if "FAQ" in blog_text or "faq" in blog_text:
        score += 20

    if "##" in blog_text or "###" in blog_text:
        score += 20

    if "get started" in blog_text.lower() or "try blogy" in blog_text.lower():
        score += 20

    return score