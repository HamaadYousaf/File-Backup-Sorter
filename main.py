import os
import shutil
from datetime import datetime
import time
import schedule
import threading

source_dir = r""
dest_dir = r""
scheduleActive = False

def backup(source, dest):
    backup_date = str(datetime.now())[:-10].replace(" ", "_").replace(":", "-")
    backup_dir = os.path.join(dest, backup_date)

    try:
        shutil.copytree(source, backup_dir)
        print(f"Folder copied to: {backup_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

        
def schedule_task():
    schedule.every().day.at("12:00").do(lambda: backup(source_dir, dest_dir))

    while scheduleActive:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    if scheduleActive:
        t1 = threading.Thread(target=schedule_task, name='t1')
        t1.start()