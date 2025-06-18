import waveassist
waveassist.init("2fec42dd-492b-4294-8154-d33c3ccf", "darshika_test")


# Fetch the Wikipedia article data from Node 1
article_data = waveassist.fetch_data("wiki_summary")

# Extract relevant information
title = article_data.get("title", "Unknown Article")
extract = article_data.get("extract", "No summary available.")
page_url = article_data.get("content_urls", {}).get("desktop", {}).get("page", "")

# Create HTML email content
html_content = f"""
<h2>📚 Your Daily Wikipedia Discovery</h2>
<h3>{title}</h3>
<p>{extract}</p>
<p><a href="{page_url}">Read the full article on Wikipedia</a></p>
<hr>
<p><em>Serendipitous learning in 60 seconds via RandomWiki</em></p>
"""

# Send the email
waveassist.send_email(
    subject=f"Daily Wiki: {title}",
    html_content=html_content
)

# Store confirmation that email was sent
waveassist.store_data("email_sent", {"status": "success", "title": title})
print("Daily Wikipedia email sent successfully.")
