import os
import shutil
from datetime import datetime
import time
import schedule
import threading

source_dir = r""
dest_dir = r""
schedule_backup_active = False
schedule_sort_active = False
scheduleTime = "12:00"

def backup(source, dest):
    backup_date = str(datetime.now())[:-10].replace(" ", "_").replace(":", "-")
    backup_dir = os.path.join(dest, backup_date)

    try:
        shutil.copytree(source, backup_dir)
        print(f"Folder copied to: {backup_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

        
def schedule_backup():
    schedule.every().day.at(scheduleTime).do(lambda: backup(source_dir, dest_dir))

    while schedule_backup_active:
        schedule.run_pending()
        time.sleep(60)


def sort():
    files = os.listdir(source_dir)
    folders = ["media", "text", "pdf", "spreadsheets"]

    for folder in folders:
        if not os.path.exists(source_dir+"\\"+folder):
            os.mkdir(source_dir+"\\"+folder)

    for file in files:
        if(os.path.exists(source_dir+"\\spreadsheets\\"+file)):
            print(f"File \"{file}\" already exists in folder \"spreadsheets\"")
        elif ".csv" in file:
            shutil.move(source_dir + "\\" + file, source_dir+"\\spreadsheets\\"+file)


def schedule_sort():
    schedule.every().day.at(scheduleTime).do(lambda: sort())

    while schedule_sort_active:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    if schedule_backup_active:
        t1 = threading.Thread(target=schedule_backup, name='t1')
        t1.start()

    sort()