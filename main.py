from querys_work import query_result,sri,csv_files
from tfxidf_load import load_mat,load_vec,save_info_to_Joblib
from HTMLProcessor import HTMLProcessor,query_html_processor



for i, file in enumerate(csv_files):
    print(f"{i}. {file[:-4]}")  # Remove '.csv' from the printed name

save_name = input("Seleccione el csv a cargar: ")
print("\n")
url = input("\nIntroduzca la noticia (link): ")
while url != '':
    [struc_new,scores] = sri(save_name,url)
    print("Noticia: ")
    print(f"\n{struc_new.print_new()}\n")
    print("------------------------------------------------\n")

    print("Sugerencias:")
    for score in scores:
        print(f"\n{score.print_new()}\n")
    
    url = input("\nIntroduzca la noticia (link): ")
