from progress.bar import Bar
import csv
with open('./testCode/csv/raikan_ahan.csv', encoding="utf8") as csvfile:
  test = csv.reader(csvfile)
  data = list(test)
  datass = test.[]
  row_count = len[""]
  bar = Bar('Processing', max=data)
  for i in test:
    # Do some work
    bar.next()
  bar.finish()

# import tqdm


# file_path = './testCode/csv/raikan_ahan.csv'
# with open(file_path) as file:
#     for line in tqdm(file, total=get_num_lines(file_path)):
# import csv
# import csv
# from progress.bar import IncrementalBar
# with open('./testCode/csv/raikan_ahan.csv', encoding="utf8") as csvfile:
#   test = csv.reader(csvfile)
#   data = list(test)
#   row_count = len(data)
# #   print(row_count)


#   max = 3000
#   bar = IncrementalBar(f'Word segment file ',max = max ,suffix='%(percent)d%% %(elapsed_td)s')
#   for i in range(1000000):
    
#    bar.next()
#   bar.finish()
