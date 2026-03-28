from groq import Groq
from config import GROQ_API_KEY

# 🔐 Safety check
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please set it in environment variables.")

client = Groq(api_key=GROQ_API_KEY)


# 🔁 Common API caller with fallback
def call_groq(prompt, temperature=0.7, max_tokens=2000):
    models = [
        "llama-3.3-70b-versatile",   # best quality
        "llama-3.1-8b-instant"       # fallback fast
    ]

    last_error = None

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )

            return response.choices[0].message.content

        except Exception as e:
            last_error = e
            continue

    raise last_error


# 🧠 STEP 1: Strategy
def generate_strategy(keyword, audience):
    prompt = f"""
You are an expert SEO strategist.

Analyze the keyword: "{keyword}"
Target audience: "{audience}"

Return:

Search Intent:
Primary Keyword:
Secondary Keywords:
Long-tail Keywords:
SERP Gap Opportunities:
Suggested Blog Angle:

Keep it concise and structured.
"""

    return call_groq(prompt, temperature=0.5, max_tokens=800)


# 🧩 STEP 2: Outline (NEW 🔥)
def generate_outline(keyword, audience):
    prompt = f"""
Create a detailed SEO blog outline for "{keyword}" targeting {audience}.

Requirements:
- SEO optimized title
- Introduction section
- H2 and H3 headings
- Include comparison section
- Include FAQ section (5 questions)
- Include CTA section
- Optimize for featured snippet

Return structured outline only.
"""

    return call_groq(prompt, temperature=0.5, max_tokens=600)


# ✍️ STEP 3: Blog Generation
def generate_blog(keyword, audience):
    strategy_output = generate_strategy(keyword, audience)
    outline_output = generate_outline(keyword, audience)

    prompt = f"""
You are a professional SEO blog writer.

Write a complete SEO-optimized blog using:

Keyword: {keyword}
Audience: {audience}

Strategy:
{strategy_output}

Outline:
{outline_output}

Requirements:
- 800 to 1200 words
- Catchy title
- Strong introduction with keyword in first 100 words
- Use H2 and H3 headings
- Add real examples
- Add 5 FAQs
- Add a strong CTA at the end
- Use natural human-like tone
- Make it engaging and conversion-focused

Return only the final blog.
"""

    return call_groq(prompt, temperature=0.7, max_tokens=2200)
