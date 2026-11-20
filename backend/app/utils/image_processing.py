import uuid
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

IMAGE_UPLOAD_DIR = Path("static/media/profile_pics")


def process_profile_image(content: bytes) -> str:
    IMAGE_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    with Image.open(BytesIO(content)) as original:
        img = ImageOps.exif_transpose(original)

        # we will change the image orientation here
        img = ImageOps.fit(img, (300, 300), method=Image.Resampling.LANCZOS)

        # we will convert the formatting here
        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

        # the filename here
        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = IMAGE_UPLOAD_DIR / filename

        # we will create the directory if it does not exists

        img.save(filepath, "JPEG", quality=85, optimize=True)

    return filename


# this is for deleting the profile images
def delete_profile_image(filename: str | None) -> None:
    if filename is None:
        return

    filepath = IMAGE_UPLOAD_DIR / filename

    if filepath.exists():
        filepath.unlink()
