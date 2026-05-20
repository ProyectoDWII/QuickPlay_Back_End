from fastapi import FastAPI

app = FastAPI(title="QuickPay API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "QuickPay API funcionando 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}