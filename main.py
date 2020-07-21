import pandas as pd
import numpy as np


def main():
	df = pd.read_excel('./data/file_1.xlsx')
	df_super = pd.read_excel('./data/file_2.xlsx')
	print(len(df))
	print('analyzing files...')
	
	values = set(df_super['casosAcumulado'])
	df['result'] = df['casosAcumulado'].isin(values).astype(int)
	df.to_excel('./data/result.xlsx')
	print("finished")


if __name__ == '__main__':
	main()
