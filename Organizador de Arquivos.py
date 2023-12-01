import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta')
listaArquivos = os.listdir(caminho)
locais = {
    'Imagens': ['.png','.jpg','.jpeg','.gif'],
    'Planilhas': ['.xlsx'],
    'Pdfs': ['.pdf'],
    'CSV': ['.csv'],
    'Documentos': ['.doc','.docx'],
    'Textos': ['.txt','.htm','.html','.rtf','.log','.tsv','.err','.alg'],
    'Power Point': ['.ppt','.pptx'],
    'Videos e Audios': ['.avi','.mp4','.mp3','.asf','.m4v','.mov','.mog','.mpeg','.wmv','.aiff','.au','.mid','.midi','.m4a','.wav','.wma'],
    'Executável':['.exe','.msi','.jar'],
    'Pastas': ['.zip','.rar'],

}

for arquivos in listaArquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivos}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivos}', f'{caminho}/{pasta}/{arquivos}')