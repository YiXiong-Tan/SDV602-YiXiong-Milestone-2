"""
Route the file operations to respective modules/ classes.

File operations like:
- Upload files
- Merge files
- Get pie chart Data
- Get bar chart data
- Get acres of fires
- check if file source exists
"""

from pages.FileOptions.file_model import FileModel
from pages.FileOptions.file_merge_view import FileMergeView
from pages.FileOptions.file_merge_controller import FileMergeController
from pages.FileOptions.file_upload_view import FileUploadView
from pages.FileOptions.file_upload_controller import FileUploadController


def uploadPopUp():
    """
    Create file upload object and load the class
    File upload MVC
    - File Model
    - File Upload View
    - File upload Controller
    """
    file = FileUploadController(FileUploadView(), FileModel())
    return file.load()


def mergePopUp():
    """
    Create merge file object and load the class
    File merge MVC
    - File Model
    - File merge View
    - File merge Controller
    """
    file = FileMergeController(FileMergeView(), FileModel())
    return file.load()


def getPieChartDataFromFile(source):
    """
    Get the data to create pie chart from file source
    Checks if the file source exists and uses the file model to filter
    csv file to obtain the data needed. Returns a dict when successful.
    """

    pieDataDict = {}

    if not sourceExist(source):
        return pieDataDict

    fileModel = FileModel()
    pieDataDict = fileModel.getPieChartDataFromFile(source)
    print(pieDataDict)
    return pieDataDict


def getBarChartDataFromFile(source):
    """
    Get the data to create bar chart from file source
    Checks if the file source exists and uses the file model to filter
    csv file to obtain the data needed. Returns a dict when successful.
    """
    barGraphDict = {}

    if not sourceExist(source):
        return barGraphDict

    fileModel = FileModel()
    barGraphDict = fileModel.getBarGraphDataFromFile(source)
    return barGraphDict


def getAcresData(source):
    """
    Filter csv file to get acres affected by fire
    Uses the file model to 
    """
    fileModel = FileModel()
    acresData = fileModel.getAcresData(source)
    return acresData


def sourceExist(source):
    """
    Open the file to check if the source is available.
    Returns:
        True - file is available for opening
        False - file is not available
    """
    try:
        f = open(source)
        f.close()
    except FileNotFoundError:
        # remove from file history list
        return False

    return True
