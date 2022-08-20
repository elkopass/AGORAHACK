# if __name__ == '__main__':
import uvicorn

from settings import settings


uvicorn.run(
    'REST.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)