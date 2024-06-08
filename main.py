import os
import shutil
from datetime import datetime
import time
import schedule
import threading

schedule_backup_active = False
schedule_sort_active = False
scheduleTime = "12:00"

def backup(source_dir):
    dest_dir = source_dir + "_backups"
    backup_date = str(datetime.now())[:-10].replace(" ", "_").replace(":", "-")
    backup_dir = os.path.join(dest_dir, backup_date)

    try:
        shutil.copytree(source_dir, backup_dir)
        return "Backup Complete"
    except FileExistsError:
        return f"Folder already exists in: {dest_dir}"

        
def schedule_backup(source_dir):
    dest_dir = source_dir + "\\" + "backups"
    schedule.every().day.at(scheduleTime).do(lambda: backup(source_dir, dest_dir))

    while schedule_backup_active:
        schedule.run_pending()
        time.sleep(60)


def sort(source_dir):
    folder_type_map = {
        "png" : "media",
        "jpeg" : "media",
        "txt" : "text",
        "pdf" : "documents",
        "docx" : "documents",
        "csv" : "spreadsheets",
    }
    files = os.listdir(source_dir)

    for folder in folder_type_map.values():
        if not os.path.exists(source_dir+"\\"+folder):
            os.mkdir(source_dir+"\\"+folder)

    for file in files:
        file_type = file.split(".")[-1]
        folder_dest = folder_type_map.get(file_type)

        if folder_dest:
            if os.path.exists(source_dir + "\\" + folder_dest + "\\" +file):
                return f"File \"{file}\" already exists in folder \"{folder_dest}\""
            else:
                shutil.move(source_dir + "\\" + file, source_dir + "\\" + folder_dest + "\\" +file)

    return "Sorting Complete"

def schedule_sort():
    schedule.every().day.at(scheduleTime).do(lambda: sort())

    while schedule_sort_active:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    if schedule_backup_active:
        t1 = threading.Thread(target=schedule_backup, name='t1')
        t1.start()

    print("here")