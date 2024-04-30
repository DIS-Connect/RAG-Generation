from openai import OpenAI
from secret import api_key
from operator import itemgetter
from retriever import ToyRetriever
# langchain imports
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.documents import Document



# list of documents as dummy context data (data fetching)
documents = [
    Document(
        page_content='Model A: Red',
        metadata={"name": "model a", "color": "red"},
    ),
    Document(
        page_content='Model B: Blue',
        metadata={"name": "model b", "color": "blue"},
    ),
    Document(
        page_content='Model C: Green',
        metadata={"name": "model c", "color": "green"},
    ),
]
# dummy retriever method that returns the top k documents that contain the user query.
retriever = ToyRetriever(documents=documents, k=3)


class ChatBot:

    def __init__(self):
        self.openai_client = OpenAI(api_key=api_key)
        self.openai_client.api_key = api_key

    def answer_question(self, question, model, conversation):
        # prompt engineering to guide the LLM through the provided documents
        prompt_template = ("""
                           You will be faced with queries concerning a couple of vehicle models. You
                           are a salesperson and you should assist people using the information that is 
                           provided to you while being as concise as possible. The people you're dealing
                           are very important people and they don't have much time so the answer
                           needs to be simple. If you don't know the answer, just say I don't know.
                           Answer with a short sentence then ask the user if he wants more detail 
                           on the car.
""")
        prompt = ChatPromptTemplate.from_template(prompt_template)

        # check for an api key
        if api_key == "":
            openai_connected = False
            return "LLM connection is not implemented"
        else:
            openai_connected = True

        # create a rag chain instance if the api key is valid
                if openai_connected:
            """rag_chain = (
                # TODO: turn the question into a Runnable instance that returns the query
                {"context": retriever, "question": question}
                | prompt
                | model
                | StrOutputParser()
            )
            rag_chain.invoke(question)"""
            answer = retriever.invoke(question)
            if answer.__len__() == 0:
                return "Sorry, I can't answer this question."
            else:
                return answer
