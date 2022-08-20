from fastapi import FastAPI

from api.file import router

app = FastAPI()

app.include_router(router)
# from fastapi import APIRouter, FastAPI, UploadFile
# import shutil

# router = APIRouter(
#     prefix="/files"
# )

# def sendFileToConverter(file):
#         newJSON = file
#         #dosmt
#         return newJSON

# def sendJSONToRabbit(file):
#     parameter = sendFileToConverter(file)
#     print("JSON is sended to Rabbit")

# @router.post('/')
# def upload_file(
#         file: UploadFile
# ):
#     with open(f'{file.filename}', "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     shutil.move(file.filename, "uploads/" + file.filename) 
#     sendJSONToRabbit(file)

# @router.post('/toRabbit')
# def upload_file(
#         file: UploadFile
# ):
    
#     sendJSONToRabbit(file)

# app = FastAPI()

# app.include_router(router)