from querys_work import query_result
from tfxidf_load import load_mat,load_vec,save_info_to_Joblib
from HTMLProcessor import StructuredNew, HTMLProcessor,query_html_processor
import time
import os

first = True

# Ejecutar el test

# List all CSV files in the current directory
file_url='./files_charged/csv/'
csv_files = [f for f in os.listdir(file_url) if f.endswith('.csv')]

# Display menu options based on the CSV files found
for i, file in enumerate(csv_files):
    print(f"{i}. {file[:-4]}")  # Remove '.csv' from the printed name

# Ask the user to select a file
save_name = input("Seleccione el csv a cargar: ")
print("\n\n\n")
# Assuming save_name is an index, convert it to an integer
try:
    selected_file = csv_files[int(save_name)]
    url_csv = f"./files_charged/csv/{selected_file[:-4]}"
except IndexError:
    url_csv = f"./files_charged/{csv_files[int(0)][:-4]}"


mat_url = f'./files_charged/matrix/{selected_file[:-4]}_matrix.joblib'
vec_url = f'./files_charged/vect/{selected_file[:-4]}_vect.joblib'

url = input("\n\nIntroduzca la noticia (link): ")
query = query_html_processor(url)
    
while query != '':
    url = input("\n\nIntroduzca la noticia (link): ")
    query = query_html_processor(url)
    print("\n\n")
    if first:
        matrix = load_mat(mat_url)
        vectorizer = load_vec(vec_url)        
        first = False

    scores = query_result(query,matrix,f'{url_csv}.csv',vectorizer,10)
    
    for score in scores:
        score.print()

    