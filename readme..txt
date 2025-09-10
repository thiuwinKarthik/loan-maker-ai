#create venv environtment

python -m venv venv



# Activate your virtual environment first (if using venv)

source venv/Scripts/activate   
# Windows: venv\Scripts\activate


# Run FastAPI AI service
uvicorn main:app --reload --host 127.0.0.1 --port 8000
