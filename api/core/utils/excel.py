import pandas as pd


def validate_dataframe(
    df: pd.DataFrame, expected_header: str = "Sales Recapitulation Detail Report"
) -> None:
    """
    Validates that the first cell of the DataFrame matches the expected header.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to validate.
    expected_header : str, optional
        The expected text in the first cell (default is "Sales Recapitulation Detail Report").

    Raises
    ------
    ValueError
        If the first cell does not match the expected header.
    """
    first_cell = str(df.iat[0, 0]).strip()
    if first_cell != expected_header:
        raise ValueError(
            f"Invalid file format: expected '{expected_header}' "
            f"in first cell, but found '{first_cell}'."
        )


def load_and_parse_order_details(file_path: str, sheet_name: str = 0) -> pd.DataFrame:
    """
    Loads an Excel file, validates the first cell, and skips the first 12 rows.

    Parameters
    ----------
    file_path : str
        Path to the Excel file.
    sheet_name : str or int, optional (default=0)
        Sheet name or index to load (default is the first sheet).

    Returns
    -------
    pd.DataFrame
        DataFrame containing the sheet data (first 12 rows skipped).
    """
    # Load raw data without skipping rows to validate first cell
    df_raw = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    validate_dataframe(df_raw)  # raises if invalid

    # Now reload, skipping first 12 rows and treating row 13 as headers
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=11)

    return df
