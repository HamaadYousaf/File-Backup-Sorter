import tkinter as tk
from tkinter import filedialog
from main import backup, sort

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        
        self.root.geometry("1000x600")
        self.root.title("File Backup/Sort")

        self.title_label = tk.Label(self.root, text="Sort or Backup Files", font=('Arial', 18))
        self.title_label.pack(padx=20, pady=20)

        self.folder_frame = tk.Frame(self.root)
        self.folder_frame.columnconfigure(0, weight=2)

        self.source_folder = None

        self.choose_label = tk.Label(self.folder_frame, text="Choose a Folder:", font=('Arial', 14))
        self.choose_label.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5)

        self.folder_btn = tk.Button(self.folder_frame, text="Choose", font=('Arial', 10), command=self.selectFolder)
        self.folder_btn.grid(row=0, column=2, sticky=tk.W+tk.E, padx=5)

        self.display_folder = tk.StringVar()
        self.display_folder.set(self.source_folder.split("/")[-1] if self.source_folder else "None")

        self.folder_label = tk.Label(self.folder_frame, textvariable=self.display_folder, font=('Arial', 10))
        self.folder_label.grid(row=0, column=3, sticky=tk.W+tk.E, padx=5)

        self.folder_frame.pack(padx=20)

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.columnconfigure(0, weight=2)

        self.backup_btn = tk.Button(self.btn_frame, text="Backup", font=('Arial', 14), command=self.backupHandler)
        self.backup_btn.grid(row=0, column=0, sticky=tk.W+tk.E, padx=20)
        self.sort_btn = tk.Button(self.btn_frame, text="Sort", font=('Arial', 14), command=self.sortHandler)
        self.sort_btn.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20)

        self.btn_frame.pack(padx=20, pady=10)

        self.status = tk.StringVar()

        self.status_label = tk.Label(self.root, textvariable=self.status, font=('Arial', 12))
        self.status_label.pack(padx=20, pady=(5,20))

        self.time_label = tk.Label(self.root, text="Choose Time:", font=('Arial', 14))
        self.time_label.pack(padx=20, pady=5)

        self.myentry = tk.Entry(self.root)
        self.myentry.pack(padx=20, pady=5)

        self.backup_state = tk.IntVar()
        self.check_backup = tk.Checkbutton(self.root, text="Schedule Backup", font=('Arial', 12), variable=self.backup_state)
        self.check_backup.pack(padx=20, pady=2)

        self.sort_state = tk.IntVar()
        self.check_sort = tk.Checkbutton(self.root, text="Schedule Sort", font=('Arial', 12), variable=self.sort_state)
        self.check_sort.pack(padx=20, pady=2)

        self.schedule_btn = tk.Button(self.root, text="Schedule", font=('Arial', 14))
        self.schedule_btn.pack(padx=20, pady=10)

        self.root.mainloop()


    def selectFolder(self):
        self.source_folder = filedialog.askdirectory()
        self.display_folder.set(self.source_folder.split("/")[-1] if self.source_folder else "None")

    def backupHandler(self):
        if self.source_folder:
            self.status.set(backup(source_dir=self.source_folder))

    def sortHandler(self):
        if self.source_folder:
            self.status.set(sort(source_dir=self.source_folder))

    
MyGUI()