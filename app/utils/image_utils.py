from PIL import Image
import io

async def read_image(file):
    return Image.open(io.BytesIO(await file.read()))