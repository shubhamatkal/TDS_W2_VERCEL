from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

def load_data():
    with open('q-vercel-python.json', 'r') as file:
        data = json.load(file)
    return data



# Dummy data for student marks
student_marks = load_data()

@app.get("/api")
def get_marks(name: list[str] = []):
    """
    API Endpoint: /api?name=A&name=B
    Returns the marks of requested students.
    """
    return {"marks": [student_marks.get(n, 0) for n in name]}
