def merge(source, target, has_header=True):
    target_file_obj = open(target, 'a')
    source_file_obj = open(source,'r')
    lines = source_file_obj.readlines()
    if has_header:
        lines = lines[1:]

    target_file_obj.writelines(lines)


def upload(source):
    # upload and return 
    pass