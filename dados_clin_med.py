from datetime import datetime, timedelta
import datetime
import os, json, time
import cx_Oracle
from connection import mvintegra
import connection
from operator import itemgetter
#import numpy as np

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
        view_agenda_clin_med = {'DS_LEITO':requests[0],'NM_PACIENTE':requests[1],'NM_PRESTADOR':requests[2],'PRESTA':requests[3],
        'PRESTAN':requests[4],'DIAS':requests[5],'DT_PREVISTA_ALTA':requests[6],'L_PEDIDO':requests[7],'UL_PEDIDO':requests[8],
        'P_PEDIDO':requests[9],'up_pedido':requests[10],'S_PEDIDO':requests[11],'SU_PEDIDO':requests[12],'RX_SN_PEDIDO':requests[13],
        'URX_SN_PEDIDO':requests[14],'ED_PEDIDO':requests[15],'UED_PEDIDO':requests[16],'US_PEDIDO':requests[17],'UUS_PEDIDO':requests[18],
        'TP_SOLICITADO':requests[19],'ECG':requests[20],'UECG':requests[21],'AVISO':requests[22],'CD_ATENDIMENTO':requests[23],
        'DT_ALTA_MEDICA':requests[24],'RPA':requests[25],'CD_ATENDIMENTO_PAI':requests[26],'TP_SEXO':requests[27], 
        'PROCL1':requests[28],'PROCL2':requests[29],'PROCL3':requests[30]}
        
        list_agenda_clin_med.append(view_agenda_clin_med)
        # end
    connection.commit()
    return list_agenda_clin_med

def Verif_list_date(list_agenda):
    nlin = len(list_agenda)
    list_leitos_vagos = list()
    
    list_agenda_cli_med = list()
    for i in range(0, nlin):
        
        if list_agenda[i]['NM_PACIENTE'] == 'Leito vago':
            list_leitos_vagos.append(i)
        else:        
            if list_agenda[i]['DIAS'] is None:
                list_agenda[i]['DIAS'] = 'vazio'
            
            if list_agenda[i]['DT_PREVISTA_ALTA'] is None:
                list_agenda[i]['DT_PREVISTA_ALTA'] = 'vazio'
            '''else:
                if type(list_agenda[i]['DT_PREVISTA_ALTA']) != class 'str':
                    aux = list_agenda[i]['DT_PREVISTA_ALTA'].strftime('%d/%m/%Y')
                    list_agenda[i]['DT_PREVISTA_ALTA'] = aux'''

            if list_agenda[i]['DT_ALTA_MEDICA'] is None:
                list_agenda[i]['DT_ALTA_MEDICA'] = 'vazio'
            '''else:
                aux = list_agenda[i]['DT_ALTA_MEDICA'].strftime('%d/%m/%Y %H/%M')
                list_agenda[i]['DT_ALTA_MEDICA'] = aux'''

            if list_agenda[i]['NM_PRESTADOR'] is None:
                list_agenda[i]['NM_PRESTADOR'] = 'vazio'

            if list_agenda[i]['PRESTA'] is None:
                list_agenda[i]['PRESTA'] = 'vazio'

            if list_agenda[i]['PRESTAN'] is None:
                list_agenda[i]['PRESTAN'] = 'vazio'

            if list_agenda[i]['CD_ATENDIMENTO'] is None:
                list_agenda[i]['CD_ATENDIMENTO'] = 'vazio'

            if list_agenda[i]['CD_ATENDIMENTO_PAI'] is None:
                list_agenda[i]['CD_ATENDIMENTO_PAI'] = 'vazio'

            if list_agenda[i]['PROCL1'] is None:
                list_agenda[i]['PROCL1'] = 'vazio'

            if list_agenda[i]['PROCL2'] is None:
                list_agenda[i]['PROCL2'] = 'vazio'

            if list_agenda[i]['PROCL3'] is None:
                list_agenda[i]['PROCL3'] = 'vazio'
    #np.array(list_agenda)  #verificar
    return list_agenda, list_leitos_vagos

def receiver_agenda_cli_med():
    list_agenda = view_bloco()
    leito_ocupados = dict()
    list_agenda_cli_med,list_vaga = Verif_list_date()
    nlin = len(list_agenda_cli_med)
    
    for i in range(0,nlin):
        leito_ocupados['NM_PACIENTE'] = list_agenda[i]['NM_PACIENTE']
    list_agenda_cli_med = sorted(list_agenda_cli_med, key=itemgetter('DS_LEITO'))  #verificar os dado de data para a efetuacao da ordenacao
    manda_gravar(list_agenda_cli_med)
               
               
               


def manda_gravar(list_agenda_cirurgica):
    print(list_agenda_cirurgica)
    arquivo = 'list_agenda_cli_med.json'
    grava_em_arquivo(arquivo,list_agenda_cirurgica)
    
def grava_em_arquivo(nome_arq,lista):
    with open(nome_arq, 'w', encoding='utf8') as f:
        json.dump(lista,f,ensure_ascii=False,sort_keys=True ,indent=4, separators=(',', ':'))
#end