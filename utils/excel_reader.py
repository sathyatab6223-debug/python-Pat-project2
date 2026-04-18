import openpyxl
from utils.logger import get_logger

logger = get_logger(__name__)


def read_login_data(file_path, sheet_name):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        logger.info(f"Reading data from '{file_path}' -> sheet '{sheet_name}'")

        headers = [cell.value for cell in sheet[1]]
        data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if any(cell is not None for cell in row):
                row_dict = dict(zip(headers, row))
                data.append(row_dict)

        logger.info(f"Loaded {len(data)} row(s) from Excel")
        return data

    except FileNotFoundError:
        logger.error(f"Excel file not found: {file_path}")
        raise
    except KeyError:
        logger.error(f"Sheet '{sheet_name}' not found in '{file_path}'")
        raise
