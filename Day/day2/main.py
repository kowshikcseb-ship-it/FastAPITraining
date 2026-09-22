from fastapi import FastAPI
app =FastAPI()
@app.get("/")
def read_root():
    return {"message": "hello world","number":8}
@app.get("/about")
def about():
    return {"page":"about", "authour":"koushik"}
@app.get("/health")
def health():
    return {"status":"ok"}
#post reuest
@app.post("/create")
def create_something():
    return {"message":"created successfullys"}


