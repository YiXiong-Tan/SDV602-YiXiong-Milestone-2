import os
import shutil
import glob
import csv


class FileModel:
    source = ""
    target = ""
    dest_path = os.path.join(os.path.dirname(
        os.path.abspath("data"))+"\\data\\")
    dest = ""
    data_dict = []

    def upload(self):
        # upload the file to local storage from source

        if self.source != "":

            # get file name
            dest_filename = os.path.basename(self.source)

            # combine path and filename
            self.dest = self.dest_path + dest_filename

            # copy from source path to local path in project dir
            shutil.copy(self.source, self.dest)

    def merge(self, has_header=True):
        """
            Credit: Todd
        """
        # open the target file for appending
        target_file_obj = open(self.target,'a')

        # open the source file for reading
        source_file_obj = open(self.source,'r')

        lines = source_file_obj.readlines()
        
        if has_header:
            lines = lines[1:]

        target_file_obj.writelines(lines)

        # close files
        target_file_obj.close()
        source_file_obj.close()



    def getPieChartDataFromFile(self, source):
        pieDict = {}
        # pieDataDict = {'label':['a', 'b', 'c'], percentages:[]}
        # read file
        with open(source, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                fire_type = row['FIRE_TYPE']
                if row['FIRE_TYPE'] != "":
                    if fire_type in pieDict.keys():
                        pieDict[fire_type] += 1
                    else:
                        pieDict[fire_type] = 1

        return pieDict
