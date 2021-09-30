from pages.FileOptions.file_model import FileModel
from pages.FileOptions.file_merge_view import FileMergeView
from pages.FileOptions.file_merge_controller import FileMergeController
from pages.FileOptions.file_upload_view import FileUploadView
from pages.FileOptions.file_upload_controller import FileUploadController


def uploadPopUp():
    file = FileUploadController(FileUploadView(), FileModel())
    return file.load()


def mergePopUp():
    file = FileMergeController(FileMergeView(), FileModel())
    return file.load()


def getPieChartDataFromFile(source):
    pieDataDict = {}

    if not sourceExist(source):
        return pieDataDict

    fileModel = FileModel()
    pieDataDict = fileModel.getPieChartDataFromFile(source)
    print(pieDataDict)
    return pieDataDict


def getBarChartDataFromFile(source):
    barGraphDict = {}

    if not sourceExist(source):
        return barGraphDict

    fileModel = FileModel()
    barGraphDict = fileModel.getBarGraphDataFromFile(source)
    return barGraphDict


def getAcresData(source):
    fileModel = FileModel()
    acresData = fileModel.getAcresData(source)
    return acresData


def sourceExist(source):
    try:
        f = open(source)
        f.close()
    except FileNotFoundError:
        # remove from file history list
        return False

    return True
