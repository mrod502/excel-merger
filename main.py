import tkinter as tk
from tkinter import filedialog


def main():
  root = tk.Tk()
  root.withdraw()

  file_path = filedialog.askopenfilename()

  return


if __name__ == "__main__":
  main()