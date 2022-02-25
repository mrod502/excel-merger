from excel_merger import ExcelMerger

def main():

  merger = ExcelMerger()

  merger.merge()

  merger.save()

if __name__ == "__main__":
  main()
