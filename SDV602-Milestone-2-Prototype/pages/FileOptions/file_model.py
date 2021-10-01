"""
A model that manages the data required by the File View and Controller
Both the file upload and merge will share this model

"""
import os
import shutil
import csv
from datetime import datetime

class FileModel:
    """
    The file model does not to be initialized.
    Besides performing the file operations below:
    - upload file
    - merge file
    - get pie chart data
    - get bar graph data
    - get acres affected by fire data
    """
    
    des_selected = ""
    source = ""
    target = ""
    dest_path = os.path.join(os.path.dirname(
        os.path.abspath("data"))+"\\data\\")
    dest = ""
    data_dict = []

    def upload(self):
        """Upload the file to project source"""
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
        """Merge files from source to target file"""
        try:
            # read csv files with the source supplied
            def readCSVFile(path, isTargetFile):
                """
                Embedded function used to read the csv file

                Arg:
                    Path - the path to file
                    isTargetFile - To determine whether to use keep the header of 
                                    the csv file in the newly merged file.
                
                Returns:
                    header and the csv data
                """
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
        """
        Process the pie chart data from the "Fire type" column of the source.
        Counts the number of fire types

        Args:
            source - path to the file
        
        Returns:
            a dictionary that consist the data for the pie chart
        """
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
        """
        Process the IG_DATE column from the source 

        Args:
            source - path to the file
        
        Returns:
            sorted - bar chart dictionary
        """
        
        barDict = {}
        # read csv file
        with open(source, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date_str = row['IG_DATE']
                if date_str != "":

                    date_time_obj = getdatetimeObj(date_str)

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

    
    def getAcresData(self,source):
        """
        Group the Acres column into ranges from the file source

        Args:
            source - path to the file
        
        Return:
            Dictionary of ranges of acres affected by fire
        """
        
        data_dict = {}
        with open(source, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            ranges = {}

            for row in reader:
                acres = int(row['ACRES'])

                # range < 1200
                if acres < 1201:
                    range_key = '< 1200'
                    if range_key in ranges.keys():
                        ranges[range_key] += 1
                    else:
                        ranges[range_key] = 1

                # range between 1201-2000
                if acres > 1200 and acres < 2001:
                    range_key = '1201 - 2000'
                    if range_key in ranges.keys():
                        ranges[range_key] += 1
                    else:
                        ranges[range_key] = 1

                # range between 2001-3500
                if acres > 2000 and acres < 3501:
                    range_key = '2001 - 3500'
                    if range_key in ranges.keys():
                        ranges[range_key] += 1
                    else:
                        ranges[range_key] = 1

                # range between 3501-7000 
                if acres > 3500 and acres < 7001:
                    range_key = '3501 - 7000'
                    if range_key in ranges.keys():
                        ranges[range_key] += 1
                    else:
                        ranges[range_key] = 1

                # range > 7000
                if acres > 7000:
                    range_key = '< 1200'
                    if range_key in ranges.keys():
                        ranges[range_key] += 1
                    else:
                        ranges[range_key] = 1

            return ranges
               

def getdatetimeObj(date_str):
    """
    Get the date time obj from the file.
    Since the file might have 2 different date formats,
    this function will cater for that.
    """

    # remove the +00 at the back of the date
    date_time_str = date_str.split("+")[0]

    # break down the date
    date_time_obj = datetime

    # Dates in different files have different format
    # try '%Y/%m/%d %H:%M:%S' format and '%Y%m%d' format to cater for 2 different formats
    try:
        date_time_obj = datetime.strptime(
            date_time_str, '%Y/%m/%d %H:%M:%S')
    except ValueError as ve:
        date_time_obj = datetime.strptime(
            date_time_str, '%Y%m%d'
        )
    
    return date_time_obj