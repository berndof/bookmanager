


def search_pdf_files(directory_path):
    import os

    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
    
    return pdf_files


def copy_book_to_library(book_path):

    #Primeiro quero editar os metadados do livro
    #editar titulo, autor, ano de publicação, genero tags e etc

    #Depois quero copiar o livro para a pasta da biblioteca com as novas informações


    import shutil

    shutil.copy(book_path, library_path)
    print(f"Book copied to library: {book_path}")