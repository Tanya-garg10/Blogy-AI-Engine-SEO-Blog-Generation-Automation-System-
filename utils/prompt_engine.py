from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_strategy(keyword, audience):
    prompt = f"""
You are an expert SEO strategist.

Analyze the keyword: "{keyword}"
Target audience: "{audience}"

Return the output in this format:

Search Intent:
Target Audience:
Primary Keyword:
Secondary Keywords:
Long-tail Keywords:
SERP Gap Opportunities:
Suggested Blog Angle:

Keep it concise, practical, and structured.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=700
    )

    return response.choices[0].message.content


def generate_blog(keyword, audience):
    strategy_output = generate_strategy(keyword, audience)

    prompt = f"""
You are a professional SEO blog writer.

Write a complete SEO-optimized blog using the following strategy.

Keyword: {keyword}
Audience: {audience}

Strategy:
{strategy_output}

Requirements:
- 800 to 1200 words
- Catchy title
- Strong introduction with keyword in first 100 words
- Use H2 and H3 headings
- Add a comparison section
- Add 5 FAQs
- Add a strong CTA at the end
- Use natural human-like tone
- Make it engaging, clear, and conversion-focused

Return only the final blog.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2200
    )

    return response.choices[0].message.content