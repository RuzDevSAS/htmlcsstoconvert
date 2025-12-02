from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import Response
from html2image import Html2Image
import tempfile
import os
import shutil
from typing import Optional

router = APIRouter()

@router.post("/convert")
async def convert_html_to_image(
    html: Optional[str] = Form(None),
    html_file: Optional[UploadFile] = File(None),
    css: Optional[str] = Form(None),
    css_file: Optional[UploadFile] = File(None),
    image: Optional[UploadFile] = File(None),
    width: int = Form(1920),
    height: int = Form(1080),
):
    # Create a temporary directory for this request
    with tempfile.TemporaryDirectory() as temp_dir:
        hti = Html2Image(output_path=temp_dir)
        
        # Handle HTML input
        html_content = ""
        if html_file:
            content = await html_file.read()
            html_content = content.decode("utf-8")
        elif html:
            html_content = html
        else:
            raise HTTPException(status_code=400, detail="HTML content or file is required")

        # Handle CSS input
        # Handle CSS input
        css_content = "html, body { margin: 0; padding: 0; width: 100%; height: 100%; background-color: white; }"
        if css_file:
            content = await css_file.read()
            css_content += "\n" + content.decode("utf-8")
        elif css:
            css_content += "\n" + css

        # Handle Image Asset
        if image:
            image_path = os.path.join(temp_dir, image.filename)
            with open(image_path, "wb") as f:
                shutil.copyfileobj(image.file, f)
            # You might want to update HTML to reference this image if needed, 
            # but usually the user ensures the HTML references the filename correctly.
            # For simplicity, we assume the HTML uses the filename directly (e.g. <img src="image.png">)
            # and since we are rendering in temp_dir, it might work if we save the HTML file there too.

        # Embed CSS directly into HTML to avoid file linking issues
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                {css_content}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        # Save HTML to file
        html_filename = "index.html"
        html_path = os.path.join(temp_dir, html_filename)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)
        
        # We don't need a separate CSS file anymore since it's embedded
        css_path = None

        # Render
        output_filename = "output.png"
        try:
            print(f"Attempting to render to {output_filename} in {temp_dir}")
            # We pass the file paths to html2image. 
            # It will load index.html, which can reference style.css and image.png relatively.
            hti.screenshot(
                html_file=html_path,
                save_as=output_filename,
                size=(width, height)
            )
            print("Render command executed.")
        except Exception as e:
             print(f"Error during rendering: {e}")
             raise HTTPException(status_code=500, detail=f"Rendering failed: {str(e)}")

        output_path = os.path.join(temp_dir, output_filename)
        
        if not os.path.exists(output_path):
             print(f"Output file not found at {output_path}")
             raise HTTPException(status_code=500, detail="Output image was not generated. Ensure Chrome/Chromium is installed.")

        with open(output_path, "rb") as f:
            image_data = f.read()
            print(f"Read {len(image_data)} bytes from output image.")

        return Response(content=image_data, media_type="image/png")
