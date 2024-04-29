from flask import Flask, render_template, request
from generation import ChatBot
# load relevant vars
import dotenv
dotenv.load_dotenv()

# Create a flask app instance
app = Flask(__name__)

# Initial conversation
conversation = [("Hi, who are you?", "Hello, I do not have a name."),
                ("How old are you?", "I do not know, my creators did not tell me.")]

chatbot = ChatBot()


# Chatbot function
def chatbot_response(question):
    # Here you can implement your chatbot logic
    # For simplicity, I'll just return a hardcoded response
    if question.lower() in ["hi", "hello"]:
        return "Hello! How can I assist you today?"
    elif question.lower() == "how are you?":
        return "I'm just a bot, but thanks for asking!"
    else:
        return "I'm sorry, I didn't understand that question."


@app.route('/')
def home():
    return render_template('index.html', conversation=conversation)


@app.route('/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        question = request.form['question']
        model = request.form['model']

        answer = chatbot.answer_question(question, model, conversation)
        conversation.append((question, answer))
        return render_template('index.html', conversation=conversation)


if __name__ == '__main__':
    app.run(debug=True)
