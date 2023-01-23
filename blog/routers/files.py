from fastapi import APIRouter, Depends, status, HTTPException,  UploadFile, Response
from .. import  schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from uuid import uuid4
import boto3
from loguru import logger
import magic
from botocore.exceptions import ClientError


KB=1024
MB = 1024*KB

SUPPORTED_FILE_TYPES ={
    'image/jpeg':'jpg',
    'image/png':'png',
    'application/pdf':'pdf'
}


AWS_BUCKET = 'fastapi-s3-1'   # Bucket name

s3=boto3.resource('s3',aws_access_key_id='AKIAUNLUCTIKYS5BA4FU',aws_secret_access_key='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')

bucket=s3.Bucket(AWS_BUCKET)

async def s3_upload(contents:bytes, key: str):
    logger.info(f'uploading {key} to s3 bucket')
    bucket.put_object(Key=key, Body=contents)


async def s3_download(key: str):
    try:
        return s3.Object(bucket_name=AWS_BUCKET, key=key).get()['Body'].read()
    except ClientError as error:        
        return str(error)

router = APIRouter(
    prefix ="/file",
    tags=['Files'])

@router.post('/uploadfile')
async def upload_file(file: UploadFile | None = None):
    if not file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No file found")
   
    contents = await file.read()

    size = len(contents)

    if not 0 < size <= 1*MB:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid file size, file size must be > 0 and < = 1MB")

    file_type = magic.from_buffer(buffer=contents,mime=True)
    if file_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Unsupported file type : {file_type}")

    filename = f'{uuid4()}.{SUPPORTED_FILE_TYPES[file_type]}'
    await s3_upload(contents=contents, key=filename)
    return {"filename": filename}


@router.get('/downloadfile')
async def download_file(file_name: str | None = None):
    if not file_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No file name found")

    contents = await s3_download(key = file_name)
    if type(contents) == str:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"{contents}")

    return Response(
        content = contents,
        headers = {'Content-Type':  'application/octet-stream',
        'Content-Disposition': f'attachment;filename={file_name}'}
    )


