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
    fileModel = FileModel()
    pieDataDict = fileModel.getPieChartDataFromFile(source)
    return pieDataDict
