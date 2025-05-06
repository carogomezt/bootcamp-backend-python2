from uuid import uuid4
import boto3
from django.conf import settings


def generate_presigned_url(file_name, expiration=3600):
    file_path = f"documents/{file_name}"
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )

    try:
        response = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": settings.AWS_STORAGE_BUCKET_NAME, "Key": file_path},
            ExpiresIn=expiration,
        )
    except Exception as e:
        return None

    return response


def get_document_s3_file_path(instance, filename: str):
    return f"{uuid4().hex}.{filename.split('.')[-1]}"
