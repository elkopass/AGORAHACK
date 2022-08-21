from base64 import encode
import io
from publisher import publish_forever
from xml_json_yaml_convert.converter import Converter
MLs = ["pyDict", "xml", "json", "yaml"]
from fastapi import APIRouter, FastAPI, UploadFile
import shutil

router = APIRouter(
    prefix="/files"
)


def converter(data = "", input_ml:str = "pyDict", output_ml:str = "pyDict"):

    if input_ml == output_ml:
        return data
    else:
        translator = Converter(data)
        if input_ml == "xml":
            data = translator.from_xml()
        if input_ml == "json":
            data = translator.from_json()
        if input_ml == "yaml":
            data = translator.from_yaml()
        inverce_translator = Converter(data)
        if output_ml == "pyDict":
            return data
        if output_ml == "xml":
            return inverce_translator.to_xml()
        if output_ml == "json":
            return inverce_translator.to_json()
        if output_ml == "yaml":
            return inverce_translator.to_yaml()

def sendFileToConverter(file):
    return converter(file, input_ml="xml")

def sendJSONToRabbit(file):
    parameter = sendFileToConverter(file)
    print(parameter)
    publish_forever(file)
    


@router.post('/')
async def upload_file(
        file: UploadFile
):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    shutil.move(file.filename, "uploads/" + "file.xml")
    data = open("./uploads/file.xml", 'r', encoding='utf-8')
    sendJSONToRabbit(data.read())
        

app = FastAPI()

app.include_router(router)