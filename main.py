import os
import pandas as pd
from tqdm import tqdm

from globals import SRC_PATH, OUTPUT_PATH
from sftp_client import SftpClient
from pdf_compressor import compress
from mail_sender import *

def made_tuple(row):
    return (row["farmname"] + ".pdf", row["farmname"], ";".join(str(row["email.pdf.recipientList"]).split("\n")))

def mails_to_string():
    """
    Have to return a dict of tuples with the following structure:
    [{pdfName : (pdfName, FarmName, email_string), ...}]
    """
    df_info = pd.read_excel("src\AGL_Mapping_farms-2024-09-05_14-38-26.xlsx")
    df_info["tuple"] = df_info.apply(made_tuple, axis=1)
    pdf_dict = dict(zip(df_info["farmname"] + ".pdf", df_info["tuple"]))

    return pdf_dict


if __name__ == "__main__":

    # SFTP connection and file download
    

    # Compression of PDF files
    list_of_files = os.listdir(SRC_PATH)
    for i in tqdm(list_of_files):
        if i.endswith(".pdf"):
            new_name = ("-").join(i.split("_")[0].split("-")[1:]) + ".pdf"
            compress(SRC_PATH + i, OUTPUT_PATH + new_name, power=2)


    # # Send compressed files by email using a PyautoGUI bot
    # dico_dirs = mails_to_string()

    # list_of_files_to_send = os.listdir(OUTPUT_PATH)
    # for i in tqdm(list_of_files_to_send):
    #     info_envoi = dico_dirs[i]
    #     create_mail()
    #     change_mail()
    #     objet, m1, m2 = create_contents(info_envoi)
    #     redact_mail(info_envoi, objet, m1, m2)
    #     attach_file(info_envoi)
    #     send_mail()
        
