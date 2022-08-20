from distutils.command.upload import upload
import shutil

from fastapi import UploadFile


class Service:
    def upload_file(self, file: UploadFile):
        with open(f'{file.filename}', "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        shutil.move(file.filename, "uploads/" + file.filename)

    def sendFileToConverter(self, file: UploadFile):
        newJSON = file
        #dosmt
        return newJSON

    def sendJSONToRabbit(self, file: UploadFile):
        parameter = self.sendFileToConverter(file)
        print("JSON is sended to Rabbit")

