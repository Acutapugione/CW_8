import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or '123456512' 
    

# print(Config.SECRET_KEY)