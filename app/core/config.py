from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Chatbot CV Portfolio"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Chatbot support responds to recruitment based on CV and portfolio."

    CV_PATH: str = "data/Resume Le Viet Khanh.pdf"
    PORTFOLIO_PATH: str = "data/Khanh Viet Le Portfolio.pdf" 

    class Config:
        env_file = ".env"

settings = Settings()
