import tkinter as tk
from tkinter import filedialog
import pandas as pd
import re


class ExcelMerger:

  REX_FOOTER = re.compile(r'[\d] [A-Z]')

  def __init__(self):

    # select the files you want to merge
    root = tk.Tk()
    root.withdraw()
    self.file_paths = sorted(filedialog.askopenfilenames(filetypes=[("Excel Files","*.xls"),("Excel Files","*.xlsx")]))

    if len(self.file_paths) == 0:
      raise ValueError("no files selected")
  
  @staticmethod
  def filter_df(df:pd.DataFrame)->pd.DataFrame:
    '''this function filters out the footer notes'''
    index = [not bool(REX_FOOTER.match(str(df.loc[i,df.columns[0]]))) for i in df.index.values]
    return df.loc[df.index[index],:]
  
  def merge(self):
    self.df_main = None
    for file_path in self.file_paths:
      df = pd.read_excel(file_path,skiprows=3)

      if type(df) == None:
        self.df_main = df
      else:
        self.df_main = pd.concat([self.df_main,df],ignore_index=True)
    
  def save(self):
    root = tk.Tk()
    root.withdraw()
    save_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    self.df_main.to_excel(save_file_path, index=False)



