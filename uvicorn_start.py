
import uvicorn


if __name__=="__main__":
    uvicorn.run("api:app",host='https://vagrant-ai.streamlit.app', port=8000, reload=True,  workers=3)
