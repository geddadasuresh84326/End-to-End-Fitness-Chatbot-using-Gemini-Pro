# End-to-End Fitness Chatbot using Gemini Pro
### Objective : 
The primary goal is to design and implement a simple chatbot that can provide fitness-related advices, including workout recommendations and dietary guidance based on user inputs.

### Chatbot Development :
1. I choose Gemini-pro to develop this fitness chatbot.
2. Integrated serpapi with llm using langchain agents to connect to the external data resources and chatbot to be up-to-date 
3. Create frontend using Flask,HTML,CSS
4. Deployed the project on AWS EC2 Machine

### What it can do : 
1. It is a Fitness chatbot, It can provide fitness-related advice, including workout recommendations and dietary guidance based on user inputs.
2. It can understand questions about workout routines, dietary advice, and general fitness tips.
3. It can also provide  personalized workout and diet plans based on user inputs such as body type, fitness goals, and dietary restrictions.
4. It can also provide you real-time information ,as it has the access to the external resources serpapi , so the chatbot can provide you more accurate responses and it is up-to-date.

## How to run?
### STEPS :
#### clone the repository
```bash 
  github repo: https://github.com/geddadasuresh84326/End-to-End-Fitness-Chatbot-using-Gemini-Pro
```
### STEP 01 : Create a conda environment 
```bash
    conda create -p fitvenv python==3.10 -y
```
```bash
    conda activate fitvenv
```
### STEP 02 : Install the requirements
```bash
    pip install -r requirements.txt
```
### STEP 03 : Create .env file add Gemini-pro and serpapi credentials as below
```bash
GOOGLE_API_KEY = "XXXXXXXXXXXXXXXX"
serpapi_key = "XXXXXXXXXXXXXXXX"
```
### STEP 04 : Run the application
```bash
python app.py
```
## Techstack used :
- Python
- Gemini-pro
- Langchain
- Serpapi
- Flask
- AWS






