from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="YOLO Trainer Backend")

# Разрешаем CORS (для фронтенда React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "YOLO Trainer Backend работает!"}

@app.get("/docs-check")
def docs_check():
    return {"status": "Swagger UI должен отображаться!"}

# Минимальные эндпоинты для проверки
@app.post("/api/upload-dataset")
async def upload_dataset(file: UploadFile):
    return {"filename": file.filename}

@app.post("/api/train")
async def train_yolo(model_name: str = Form(...), epochs: int = Form(10)):
    return {"status": f"Training {model_name} for {epochs} epochs started"}