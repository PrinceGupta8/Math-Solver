#Import libraries
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains.llm_math.base import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool ,initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
import os
Huggingface_api_key=os.getenv('Huggingface_api_key')
from huggingface_hub import login
login(Huggingface_api_key)

#set page config
st.set_page_config(page_title='Text to math problem solver')
st.title('Text to math problem solver')

###api key
hf_api_key=st.sidebar.text_input('Enter your huggingface api key',type='password')

if not hf_api_key:
    st.info('Please enter your groq api key')
    st.stop()

#initialize model
llm=HuggingFaceEndpoint(model='google/gemma-2-2b-it',api_key=hf_api_key)

#Initialize tools
wiki_wrapper=WikipediaAPIWrapper()
wiki_tool=Tool(
    name='wikipedia',
    func=wiki_wrapper.run,
    description='A tool for searching the internet solving your math problems'
)

#math tool
math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name='calculator',
    func=math_chain.run,
    description='A tool for solving math related problems. Only input math related expression need to be provided'
)

prompt='''
You are a agent to solve mathematics problems. Write all explanation step by step to understand solution of the question. {question}'''

prompt_template=PromptTemplate(
    input_variable=['question'],
    template=prompt
)

chain=LLMChain(llm=llm,prompt=prompt_template)

#reasoning tool
reasoning_tool=Tool(
    name='Reasoning tool',
    func=chain.run,
    description='A tool for answering logic based and reasoning question'
)

assistant_agent=initialize_agent(
    tools=[wiki_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    vervose=True,
    handle_parsing_errors=True
)

#create session state
if 'messages' not in st.session_state:
    st.session_state['messages']=[{
        'role':'assistant', 'content':'Hi, I am a math chatbot that can solve math problems'
    }]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])


#Let's start the interaction
question=st.text_area('Enter your question',value='I have 7 bananas and 5 apples , I eat 2 bananas and 1 apple. how many fruits are remaining?')
if st.button('Find my answer:'):
    if question:
        with st.spinner('Generate response....'):
            st.session_state.messages.append({'role':'user','content':question})
            st.chat_message('user').write(question)
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({'role':'assistant','content':response})
            st.success(response)
    else:
        st.warning('Please write a question')
