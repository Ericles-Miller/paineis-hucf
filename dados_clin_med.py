from datetime import datetime, timedelta
import datetime
import os, json, time
import cx_Oracle
from connection import mvintegra
import connection
from operator import itemgetter

def view_bloco():
    list_agenda_clin_med = []
    connection = mvintegra()
    cursor = connection.cursor()

    select_requests = f"select DS_LEITO, NM_PACIENTE, NM_PRESTADOR,PRESTA, PRESTAN,DIAS,DT_PREVISTA_ALTA,L_PEDIDO,UL_PEDIDO,P_PEDIDO,\
        UP_PEDIDO,S_PEDIDO,SU_PEDIDO,RX_SN_PEDIDO,URX_SN_PEDIDO,ED_PEDIDO,UED_PEDIDO,US_PEDIDO, UUS_PEDIDO,TP_SOLICITADO,ECG,UECG,\
        AVISO,CD_ATENDIMENTO,DT_ALTA_MEDICA,RPA,CD_ATENDIMENTO_PAI,TP_SEXO,PROCL1,PROCL2,PROCL3\
        from dbamv.vdic_painel "
        
    request = cursor.execute(select_requests)
    
    for requests in cursor.execute(select_requests):
        view_agenda_clin_med = {'DS_LEITO':requests[0],' ':request[1],'NM_PRESTADOR':requests[2],'PRESTA':requests[3],
        'PRESTAN':requests[4],'DIAS':requests[5],'DT_PREVISTA_ALTA':requests[6],'L_PEDIDO':requests[7],'UL_PEDIDO':requests[8],
        'P_PEDIDO':requests[9],'up_pedido':requests[10],'S_PEDIDO':request[11],'SU_PEDIDO':request[12],'RX_SN_PEDIDO':request[13],
        'URX_SN_PEDIDO':request[14],'ED_PEDIDO':request[15],'UED_PEDIDO':request[16],'US_PEDIDO':request[17],'UUS_PEDIDO':request[18],
        'TP_SOLICITADO':request[19],'ECG':request[20],'UECG':request[21],'AVISO':request[22],'CD_ATENDIMENTO':request[23],
        'DT_ALTA_MEDICA':request[24],'RPA':request[25],'CD_ATENDIMENTO_PAI':request[26],'TP_SEXO':request[27], 
        'PROCL1':request[28],'PROCL2':request[29],'PROCL3':request[30]}
        
        list_agenda_clin_med.append(view_agenda_clin_med)
        # end
    connection.commit()
    return list_agenda_clin_med


def receiver_agenda_cli_med():
    list_agenda = view_bloco()
    nlin = len(list_agenda)
    list_remove = list()
    
    
        
    #END FOR 
    
    list_agenda_cli_med = sorted(list_agenda_cli_med, key=itemgetter('data_aviso'))  #verificar os dado de data para a efetuacao da ordenacao
    manda_gravar(list_agenda_cli_med)
               
               
               


def manda_gravar(list_agenda_cirurgica):
    print(list_agenda_cirurgica)
    arquivo = 'list_agenda_cli_med.json'
    grava_em_arquivo(arquivo,list_agenda_cirurgica)
    
def grava_em_arquivo(nome_arq,lista):
    with open(nome_arq, 'w', encoding='utf8') as f:
        json.dump(lista,f,ensure_ascii=False,sort_keys=True ,indent=4, separators=(',', ':'))
#end