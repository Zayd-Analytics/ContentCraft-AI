📌 ContentCraft AI ✍️

ContentCraft AI is an AI-powered content generator chatbot that helps create professional, motivational, and creative content tailored for social media, blogs, reports, and more.

Built with Streamlit and powered by the Gemini API, this application offers an interactive and easy-to-use interface with both single-prompt and bulk-generation modes.

🚀 Features

Customizable Content Generation

Choose content type (captions, posts, summaries, reports, etc.)

Adjust tone (professional, casual, motivational, friendly, etc.)

Select length (short, medium, long)

Two Working Modes

Single Prompt Mode – Enter a topic and generate instant content

Bulk CSV Mode – Upload a CSV with multiple topics and auto-generate content for all

Smart Enhancements

Automatic emoji integration for better engagement

Hashtag suggestions tailored to topic and tone

Export results to CSV for reuse

Technology Stack

Frontend/UI: Streamlit

AI Model: Gemini API

Data Handling: Pandas

Environment Management: Python-dotenv

📂 Project Structure
ContentCraft-AI/
│── app.py               # Main Streamlit app
│── utils.py             # Helper functions (emojis, hashtags, export)
│── templates.json       # Predefined templates
│── requirements.txt     # Dependencies
│── data/
│   └── sample.csv       # Example input for bulk mode
│── README.md            # Project documentation

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/ContentCraft-AI.git
cd ContentCraft-AI


Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux


Install dependencies:

pip install -r requirements.txt


Add your API key to .env file:

GEMINI_API_KEY=your_api_key_here

▶️ Usage

Run the Streamlit app:

streamlit run app.py


Select Single Prompt or Bulk CSV from sidebar

Generate content instantly or in bulk

Export results for later use

📊 Example CSV for Bulk Mode
topic,content_type,tone,length
Gym Motivation,caption,motivational,short
AI in Education,summary,professional,medium
Healthy Lifestyle,post,friendly,long

📦 Dependencies

streamlit

pandas

openai / gemini API

python-dotenv

🎯 Conclusion

ContentCraft AI is a professional and customizable AI chatbot built to simplify content creation for individuals, influencers, and businesses. With both single and bulk modes, hashtag generation, emoji integration, and export features, it provides a complete solution for fast and engaging content generation.
