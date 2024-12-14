from fastapi import FastAPI, File, UploadFile
from PIL import Image, ImageFilter
from io import BytesIO
import uvicorn

app = FastAPI()

# Endpoint para procesar la imagen
@app.post("/convert_to_sketch/")
async def convert_to_sketch(file: UploadFile):
    try:
        # Cargar la imagen
        image = Image.open(file.file).convert("L")  # Convertir a escala de grises
        
        # Aplicar efecto de borde (simular lápiz)
        sketch_image = image.filter(ImageFilter.CONTOUR)

        # Guardar la imagen en memoria
        img_byte_arr = BytesIO()
        sketch_image.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "image": img_byte_arr.read()
        }

    except Exception as e:
        return {"error": str(e)}

# Iniciar servidor local
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)