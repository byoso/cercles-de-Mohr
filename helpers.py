

def get_pressure_auto(file_path):
    pressure = int(file_path.split("/")[-1].split(".")[0].split("bb")[-1])
    return pressure