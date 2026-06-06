# utils/case_id_generator.py

from datetime import datetime


def generate_case_id():

    timestamp = datetime.now().strftime(
        "%Y%m%d%H%M%S"
    )

    return f"AML-{timestamp}"