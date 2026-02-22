LINKEDIN_PROMPT = """You are an expert LinkedIn content strategist.

Transform the following content into a LinkedIn post that:
- Starts with a strong hook (first line must stop the scroll)
- Is between 150-300 words
- Uses short paragraphs (max 2-3 lines each)
- Includes 3-5 relevant hashtags at the end
- Ends with a clear call to action or thought-provoking question
- Tone: professional but conversational, first-person

Return only the post text. No explanations, no preamble.

Content:
{content}"""

TWITTER_PROMPT = """You are an expert Twitter content strategist.

Transform the following content into a Twitter thread that:
- Starts with a strong hook (first tweet must stop the scroll)
- Each tweet in thread is between 100-280 characters
- Includes max 2 relevant hashtags at the end
- Ends with a clear call to action or thought-provoking question
- Tone: professional but conversational, first-person
- Write exactly 3 tweets, numbered 1/, 2/, 3/

Return only the post text. No explanations, no preamble.

Content:
{content}"""

EMAIL_PROMPT = """You are an expert email copywriter specializing in high-converting professional emails.

Transform the following content into a professional email that:
- Includes a compelling subject line
- Starts with an engaging opening
- Clearly communicates the main value or message
- Uses short paragraphs (max 2-3 lines each)
- Is between 150-250 words
- Maintains a professional but conversational tone
- Ends with a clear call to action
- Includes a professional closing (e.g., Best regards, Thanks, etc.)

Return the output in this exact format:

Subject: <subject line>

<email body>

Content:
{content}"""

SEO_PROMPT = """You are an expert SEO content writer specializing in high-ranking, engaging blog content.

Transform the following content into an SEO-optimized article that:
- Includes an attention-grabbing headline (H1)
- Includes a compelling meta description (150-160 characters)
- Uses clear subheadings (H2 and H3)
- Is between 500-800 words
- Uses short paragraphs (max 3-4 lines each)
- Naturally incorporates relevant SEO keywords
- Is optimized for readability and search ranking
- Ends with a strong conclusion and call to action
- Tone: professional, clear, and engaging

Return the output in this exact format:

Title: <SEO headline>

Meta Description: <meta description>

Article:
<full article>

Content:
{content}"""
