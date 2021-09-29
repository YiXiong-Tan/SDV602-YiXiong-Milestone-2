import os
import shutil
import glob
import csv


class FileModel:
    des_selected = ""
    source = ""
    target = ""
    dest_path = os.path.join(os.path.dirname(
        os.path.abspath("data"))+"\\data\\")
    dest = ""
    data_dict = []


    def upload(self):
        # TODO wrap in try except
        # upload the file to local storage from source
        try:
            if self.source != "":
                # get file name
                dest_filename = os.path.basename(self.source)

                # combine path and filename
                self.dest = self.dest_path + dest_filename

                # copy from source path to local path in project dir
                shutil.copy(self.source, self.dest)

        except Exception as e:
            print(e)


    def merge(self):

        try:
            # read csv files with the source supplied
            def readCSVFile(path, isTargetFile):
                with open(path) as csvfile:
                    header = []
                    lines = []
                    reader = csv.reader(csvfile)

                    # if target file, use header
                    if isTargetFile:
                        header = next(reader)
                    else:
                        next(reader)

                    # read line by line and append to list
                    for line in reader:
                        lines.append(line)

                return header, lines

            # read csv files and get lines and headers
            target_header, target_lines = readCSVFile(self.target, True)
            source_header, source_lines = readCSVFile(self.source, False)

            # combine the lines
            lines = target_lines + source_lines

            # name the file as the target file and point to local storage path
            des_filename = self.dest_path + os.path.basename(self.target)

            # write the new merged csv file to the local storage path
            with open(des_filename, 'w', encoding='UTF8', newline='') as f:
                # use csv library to write file
                writer = csv.writer(f)

                # write header
                writer.writerow(target_header)

                # write rows
                writer.writerows(lines)

            # assign the file path to the dest variable in model
            self.dest = des_filename

            return self.dest

        except Exception as e:
            print(e)


    def getPieChartDataFromFile(self, source):
        pieDict = {}

        # read file
        with open(source, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                fire_type = row['FIRE_TYPE']
                if fire_type != "":
                    if fire_type in pieDict.keys():
                        pieDict[fire_type] += 1
                    else:
                        pieDict[fire_type] = 1

        return pieDict


    def getBarGraphDataFromFile(self, source):
        from datetime import datetime

        barDict = {}
        # read csv file
        with open(source, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date = row['IG_DATE']
                if date != "":

                    # remove the +00 at the back of the date
                    date_time_str = date.split("+")[0]

                    # break down the date
                    date_time_obj = datetime.strptime(
                        date_time_str, '%Y/%m/%d %H:%M:%S')

                    # combine year and month eg. 01/2015
                    month_year = str(date_time_obj.month) + \
                        "/"+str(date_time_obj.year)

                    # count amount of fires on month
                    if month_year in barDict.keys():
                        barDict[month_year] += 1
                    else:
                        barDict[month_year] = 1

                    # sort the dict
                    sorted_bar_dict = {}
                    for i in sorted(barDict):
                        sorted_bar_dict[i] = barDict[i]

        return sorted_bar_dict
