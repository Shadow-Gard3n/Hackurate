import speech_recognition as sr
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
# import os 

def takecommand():
    command = sr.Recognizer()
    query = None
    while query is None:
        with sr.Microphone() as source:
            print("Listening...")
            command.adjust_for_ambient_noise(source)
            command.pause_threshold = 1
            audio = command.listen(source)
            print("Recognizing...")
            try:
                query = command.recognize_google(audio, language="en-in")
                print(f"User said: {query.capitalize()}")
                query = query.lower()
            except sr.UnknownValueError:
                print("Voice too low. Please try again")
                query = None
            except sr.RequestError:
                print("Internet Problem. Please try again") 
                query = None  
    return query 

# def ai(contents):
#     # TODO need to change to chatgpt ai
#     apikey =""
#     llm = ChatGoogleGenerativeAI(api_key=apikey,model = "gemini-1.5-flash")
#     result = llm.invoke(contents)
#     return result.content

def ai(contents):
    message1=[
    ("system","You are a highly experienced and knowledgeable doctor, specializing in all fields of medicine"),
    ("human","Based on the conversation transcript of doctor and patient generate bulleted points of questions which the doctor should ask the patient. the transcript is: {transcript}")
    ]
    message2=[
    ("system","You are a highly experienced and knowledgeable doctor, specializing in all fields of medicine"),
    ("human","Based on the conversation transcript of doctor and patient generate bulleted points of diagnosis which the patient has. the transcript is: {transcript}")
    ]

    prompt1 = ChatPromptTemplate.from_messages(message1).format(transcript=contents)
    prompt2 = ChatPromptTemplate.from_messages(message2).format(transcript=contents)
    LLM = ChatOpenAI(api_key="",model="gpt-4o-mini")

    result_llm1 = LLM.invoke(prompt1)
    result_llm2 = LLM.invoke(prompt2)
    return [result_llm1.content, result_llm2.content]



