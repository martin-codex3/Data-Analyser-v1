import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.services.tenant_service import CurrentUser

document_router = APIRouter()


@document_router.post("/upload/${user_id}")
async def upload_file(
    user_id: uuid.UUID,
    current_user: CurrentUser,
    file: UploadFile,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This route will be used to upload files"""

    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized to upload files",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"file": file.filename, "size": file.size, "content_type": file.content_type}
