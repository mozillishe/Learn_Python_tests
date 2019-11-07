import os
import shutil
import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:////home/anton/Документы/python/test.db', echo=False)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
path = '/home/anton/Документы/python/input/Test 2/'
path2 = '/home/anton/Документы/python/input/'
formats=[]
array_on_formats=[]
full_names_by_formats=[]
all_frames=[]
log_file=open('write.txt','w')


def uniqie_formats(path):
	for file_name in os.listdir(path):
		# Определение уникальных форматов файлов
		tmp_var = os.path.splitext(file_name)[1].replace('.','')
		print('очередной попавшийся формат - ' + tmp_var)
		if tmp_var not in formats and len(tmp_var)!=0:
			formats.append(tmp_var)
	return formats


def transfer(result_uniqie_formats): 	
	for var_dir in result_uniqie_formats:
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
	return print('Файлы перенесены')


# functions for reading files
def xls_and_xlsx(formats):
	for file_open in formats:
	# (Тест)Чтение файла в формате xls
		if file_open=='xls':
			dis_xls=os.path.join(path2,file_open)
			print(dis_xls +' - ок')
			array_on_formats = os.listdir(os.path.join(path2,file_open))
			for file in array_on_formats:
				full_name=os.path.join(dis_xls,file)
				log_file.write(full_name + '\n')
				xls_df=pd.read_excel(full_name, dtype=str, header=None)	
				all_frames.append(xls_df)
	xls_all_df=pd.concat(all_frames)
	return print(all_frames)


result_uniqie_formats=uniqie_formats(path)
transfer(result_uniqie_formats)
print(formats)
xls_and_xlsx(formats)

#	if file_open=='xlsx':
#		dis_xlsx=os.path.join(path2,file_open)
#		print(dis_xlsx +' - ок')
#		array_on_formats = os.listdir(os.path.join(path2,file_open))
#		for file in array_on_formats:
#			full_name=os.path.join(dis_xls,file)
#			full_names_by_formats.append(full_name)
#		for start_read in full_names_by_formats:
#			xlsx_df=pd.read_excel(start_read,  dtype=str, header=None)
#			num_cols = range(len(xlsx_df.columns))
#			print(num_cols)
#			new_cols = ['col_'+str(i) for i in num_cols]
#			xlsx_df.columns = new_cols
#			xlsx_df.rename_axis('index')
#			print(xlsx_df)
#			xlsx_df.to_sql('test', con=engine)
#			log_file.write(str(xlsx_df)+'\n')
#log_file.close()

