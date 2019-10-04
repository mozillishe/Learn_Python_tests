import os
import shutil
import pandas as pd
path = '/home/anton/Документы/python/input/Test 2/'
path2 = '/home/anton/Документы/python/input/'
formats=[]
array_on_formats=[]
full_names_by_formats=[]
for file_name in os.listdir(path):
	# Определение уникальных форматов файлов
	tmp_var = os.path.splitext(file_name)[1].replace('.','')
	print('очередной попавшийся формат - ' + tmp_var)
	if tmp_var not in formats and len(tmp_var)!=0:
		formats.append(tmp_var)
for var_dir in formats:
	new_path = path2+var_dir
	print('это кароче папки с уникальными форматами - '+new_path)
	os.makedirs(new_path,exist_ok=True)
for file_transfer in os.listdir(path):
	# Разбивка оригинального пула файлов по папкам форматов
	tmp_transfer = os.path.splitext(file_transfer)[1].replace('.','')
	print('Формат текущего файла - ' +tmp_transfer)
	if tmp_transfer in formats:
		try:
			shutil.move(os.path.join(path,file_transfer),os.path.join(path2,tmp_transfer))
		except shutil.Error:
			print(os.path.join(path,file_transfer)+' есть в папке формата, следующий...')
for file_open in formats:
	# (Тест)Чтение файла в формате xls
	if file_open=='xls':
		dis_xls=os.path.join(path2,file_open)
		print(dis_xls +' - ок')
		array_on_formats = os.listdir(os.path.join(path2,file_open))
		for file in array_on_formats:
			full_name=os.path.join(dis_xls,file)
			full_names_by_formats.append(full_name)
		for start_read in full_names_by_formats:
			Data=(pd.read_excel(io=start_read,sheet_name=None))
			print(Data)
			Data.to_csv('start_read.csv')

		