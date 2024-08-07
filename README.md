# Simple Chatbot Project

This is a simple chatbot project using OpenAI's GPT-3.5-turbo model. The chatbot takes user input, sends it to OpenAI's API, and returns a response. The project uses Python and the `dotenv` library to manage environment variables.

## Features
- Interactive command-line chatbot
- Uses OpenAI's GPT-3.5-turbo model
- Environment variable management with `.env` file
- Error handling for API requests

## Prerequisites
- Python 3.7 or higher
- An OpenAI API key

## Setup

1. **Clone the repository:**
   
bash
   git clone https://github.com/your-username/chatbot.git\
   
   cd simple_chatbot-main
  

2. **Create and activate a virtual environment (optional but recommended):**
   
bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
  

3. **Install dependencies:**
   
bash
   pip install openai python-dotenv
  

4. **Create a `.env` file in the root directory and add your OpenAI API key:**
   
env
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  

5. **Create a `.gitignore` file to ignore sensitive and unnecessary files.**


   
## Usage

1. **Run the chatbot:**
   
bash
   python chatbot.py
  

2. **Interact with the chatbot:**
   - Type your message and press Enter.
   - To exit, type `exit` or `quit`.

## Project Structure
- `chatbot.py`: The main script to run the chatbot.
- `.env`: Environment file to store the OpenAI API key.
- `.gitignore`: File to specify which files and directories to ignore in version control.

## Example
![لقطة شاشة 2024-08-07 171210](https://github.com/user-attachments/assets/ec17ce34-59fd-4a13-864a-188d6f029979)

