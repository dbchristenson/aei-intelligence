import logging
import os

from django.core.files import File

from aei.settings import MEDIA_ROOT
from applibrary.intake.intake_docx import handle_docx
from applibrary.intake.intake_pdf import handle_pdf
from applibrary.intake.intake_pptx import handle_pptx
from applibrary.intake.intake_xlsx import handle_xlsx
from applibrary.utils.loggers import basic_logging

basic_logging(__name__)


def handle_file(file: File) -> None:
    """
    Handles the file by saving it to the server and processing it
    based on its type.

    Args:
        file (File): The uploaded file.
    """
    file_ext = file.name.split(".")[-1].lower()  # Apparently this is not safe
    logging.warning(
        "Collecting file extension using potentially vulnerable method in handle_file.py"  # noqa 501
    )

    upload_directory = os.path.join(MEDIA_ROOT, "uploads", file_ext)
    os.makedirs(upload_directory, exist_ok=True)

    # Save file, pages to the server
    if file_ext == "pdf":
        handle_pdf(file, upload_directory)
    elif file_ext == "pptx":
        handle_pptx(file, upload_directory)
    elif file_ext == "xlsx":
        handle_xlsx(file, upload_directory)
    elif file_ext == "docx":
        handle_docx(file, upload_directory)
    else:
        logging.error(f"Unsupported file type: {file_ext}")
        raise ValueError(f"Unsupported file type: {file_ext}")

    return
