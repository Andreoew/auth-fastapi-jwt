from fastapi import FastAPI
from app.routes import user_router, test_router

app = FastAPI(
    title='API for simple authentication',
    description='API made in FastAPI for testing and authentication.',
    version='1.0.0'
)

@app.get(
    '/',
    summary='Health Check',
    description="Checks if the API is working correctly.",
    response_description="Retorn a simple status message"
)
def health_check():
    return "Ok, it's working"


app.include_router(user_router)
app.include_router(test_router)
