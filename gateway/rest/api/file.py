from fastapi import APIRouter, UploadFile, Depends

from services.service import Service

router = APIRouter(
    prefix="/files"
)


@router.post('/')
def upload_file_toLocal(
        file: UploadFile,
        service: Service = Depends()
):
    service.upload_file(file=file)

@router.post('/toRabbit')
def upload_file_toRabbit(
        file: UploadFile,
        service: Service = Depends()
):
    service.sendJSONToRabbit(file=file)