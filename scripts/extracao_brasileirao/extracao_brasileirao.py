# %%
# importacao de pacote e configuracao de log de execucao ----------------------------------------- #

import logging
from time import time
from datetime import datetime

exec_numb = str(datetime.now().strftime("%Y%m%d%H%M%S"))
log_file_name = f"execution_{exec_numb}.log"

logging.basicConfig(
    filename=log_file_name,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


# %%
# importacao de pacotes -------------------------------------------------------------------------- #

import requests
from os import getenv
from io import BytesIO, open
from bs4 import BeautifulSoup
from boto3 import client, resource



# %%
# declaracao de variáveis ------------------------------------------------------------------------ #


key_id = getenv("AWS_ACCESS_KEY_ID")
secret_key = getenv("AWS_SECRET_ACCESS_KEY")

url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a#ranking-schedule"

destination_bucket_name = "projeto-brasileirao"
destination_folder_name = "bronze"

destination_logs_folder_name = "logs"
log_path = f"{destination_logs_folder_name}/{log_file_name}"


# %%
# declaracao de funcao getting_s3_objects -------------------------------------------------------- #


def getting_s3_objects(key_id, secret_key, bucket_name, service="s3"):
    """
    key_id:       credencial para acesso - id
    secret_key:   credencial para acesso - secret
    bucket_name:  nome do bucket desejado para acesso
    service:      servico da AWS desejado para acesso
    return:       global all_objects > lista de todos os objetos existentes no bucket consultado
    """
    logging.info(f"funcao acessada > getting_s3_objects:...")
    try:
        global s3
        s3 = client(service, aws_access_key_id=key_id, aws_secret_access_key=secret_key)
        logging.info(
            f"Acesso ao servidor cloud (AWS S3, bucket: {bucket_name}) estabelecido com sucesso.\nDados de conexão: {s3}"
        )

        paginator = s3.get_paginator("list_objects")
        page_iterator = paginator.paginate(Bucket=bucket_name)

        global all_objects
        all_objects = []
        for page in page_iterator:
            for i in range(0, len(page["Contents"]), 1):
                all_objects.append(page["Contents"][i])

        logging.info(
            f"Metadados de objetos existentes (conteúdo do bucket) capturados."
        )

        s3.close()
        logging.info(f"Conexão com S3 encerrada!")

    except Exception as e:
        logging.error(f"{e}")
        raise print(f"Erro!\n{e}")


# %%
# declaracao de funcao creating_zipped_obj_list -------------------------------------------------- #


def creating_obj_list(dict_metadata):
    """
    dict_metadata:  dicionario com os metadados dos arquivos existentes no bucket consultado.
    return:         global objects_list > lista com os nomes dos arquivos extraidos dos metadados dos objetos coletados.
    """
    logging.info(f"funcao acessada > creating_zipped_obj_list:...")
    try:
        global objects_list
        objects_list = []
        for i in range(0, len(dict_metadata), 1):
            objects_list.append(dict_metadata[i]["Key"])
        logging.info(f"Lista de arquivos existentes no bucket criada.")

    except Exception as e:
        logging.error(f"{e}")
        raise print(f"Erro!\n{e}")


# %%
# declaracao de funcao upload_file_to_s3 --------------------------------------------------------- #


def upload_file_to_s3(key_id, secret_key, buffer, bucket_name, file_name, service="s3"):
    """
    df:           dataframe a ser gravado
    bucket_name:  nome do bucket de destino
    file_name:    exatamente o nome do arquivo (metadado)
    file:         corpo do binario do arquivo que e' de interesse # io_file,
    path:         caminho dentro do bucket de destino a ser utilizado para gravacao # path,
    return:       None
    """
    logging.info(f"funcao acessada > upload_file_to_s3:...")
    try:
        s3 = resource("s3", aws_access_key_id=key_id, aws_secret_access_key=secret_key)
        logging.info(
            f"Acesso ao servidor cloud (AWS S3, bucket: {bucket_name}) estabelecido com sucesso.\nDados de conexão: {s3}"
        )

        s3.Object(bucket_name, file_name).put(Body=buffer)

        logging.info(
            f"Arquivo {file_name} escrito (gravado) no bucket de destino com sucesso!"
        )
        logging.info(f"Conexão com S3 encerrada!")

    except Exception as e:
        logging.error(f"{e}")
        raise print(f"Erro!\n{e}")


# %%
# main script ------------------------------------------------------------------------------------ #


def main():
    try:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")

        jogo_list = []
        for link in soup.find_all(attrs={"class": "btn btn-xs btn-success m-t-5"}):
            jogo_list.append(link.get("href"))

        global sumula_list
        sumula_list = []
        for i in jogo_list:
            page = requests.get(i).text
            soup = BeautifulSoup(page, "html.parser")
            sumula_list.append(
                soup.find_all(attrs={"class": "icons pull-right"})[0].a.get("href")
            )

        for i in range(0, 2, 1): # len(sumula_list)
            file_name = sumula_list[i].split("/")
            file_name = f"{file_name[-2]}_{file_name[-3]}_brasileirao_serie_a_jogo_{file_name[-1][3:]}.pdf"

            getting_s3_objects(key_id, secret_key, destination_bucket_name)
            creating_obj_list(all_objects)
            path = f"{destination_folder_name}/{file_name}"

            if path not in objects_list:
                buffer = requests.get(sumula_list[i])
                buffer = BytesIO(buffer.content)
                upload_file_to_s3(
                    key_id,
                    secret_key,
                    buffer,
                    destination_bucket_name,
                    path,
                    service="s3",
                )

                logging.info(f"loop i= {i+1} de {len(sumula_list)} finalizado")

    except Exception as e:
        logging.error(f"{e}")
        raise print(f"Erro!\n{e}")


# %%
# Run script ------------------------------------------------------------------------------------- #
def handler(event, context):
    try:
        if __name__ == "__main__":
            logging.info(f"STARTING Script !!!")
            start_time = time()
            main()
            logging.info("--- %s seconds ---" % round(time() - start_time, 1))
            logging.info(f"Execution ended successfully!\n\n\n")

            print("--- %s seconds ---" % round(time() - start_time, 1))
            
            s3 = client('s3', aws_access_key_id=key_id, aws_secret_access_key=secret_key)
            s3.upload_file(log_file_name, destination_bucket_name, log_path)
            s3.close()

    except Exception as e:
        logging.error(f"{e}")
        print("--- %s seconds ---" % round(time() - start_time, 1))
        raise print(f"Erro!\n{e}")
    
    return 'Ok!'

# handler()