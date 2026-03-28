def format_blog(blog_text, platform):
    if platform == "LinkedIn":
        return blog_text.replace("##", "🔹")
    elif platform == "Medium":
        return blog_text
    elif platform == "WordPress":
        return blog_text.replace("##", "<h2>").replace("###", "<h3>")
    return blog_text
