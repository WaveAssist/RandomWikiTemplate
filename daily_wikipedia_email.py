import waveassist
waveassist.init()


# Fetch the Wikipedia article data from Node 1
article_data = waveassist.fetch_data("wiki_summary")

# Extract relevant information
title = article_data.get("title", "Unknown Article")
extract = article_data.get("extract", "No summary available.")
page_url = article_data.get("content_urls", {}).get("desktop", {}).get("page", "")

# Create HTML email content
html_content = f"""
<div style="font-family: Arial, sans-serif; padding: 16px; color: #333; line-height: 1.6;">
  <h2 style="margin-top: 0;">📚 Your Daily Wikipedia Discovery</h2>
  <h3 style="color: #1a0dab; margin-bottom: 8px;">{title}</h3>
  <p style="font-size: 16px; margin: 0 0 16px;">{extract}</p>
  <p style="margin: 0 0 24px;">
    <a href="{page_url}" style="color: #0066cc; text-decoration: none;" target="_blank" rel="noopener noreferrer">
      Read the full article on Wikipedia →
    </a>
  </p>
  <hr style="border: none; border-top: 1px solid #ddd; margin: 24px 0;">
  <p style="font-size: 14px; color: #666;">
    <em>Serendipitous learning in 60 seconds — powered by RandomWiki</em>
  </p>
</div>
"""

# Send the email
waveassist.send_email(
    subject=f"📘 Daily Wiki: {title}",
    html_content=html_content.strip()
)

# Store confirmation that email was sent
waveassist.store_data("email_sent", {"status": "success", "title": title})
print("✅ Daily Wikipedia email sent successfully.")

