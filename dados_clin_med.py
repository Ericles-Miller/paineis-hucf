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

    select_requests = "select data_do_aviso, nome_paciente, prestador_da_cirurgia,dt_chamada_transf, dt_centro_cirurgico,data_da_cirurgia,dt_entrada_rpa,dt_saida_rpa,centro_Cirurgico from dbamv.vdic_agenda_cirurgia WHERE DT_AVISO >= to_date(SYSDATE) AND DT_AVISO < to_date(SYSDATE+1) AND CENTRO_CIRURGICO = 'CENTRO CIRURGICO'"
    request = cursor.execute(select_requests)
    for requests in cursor.execute(select_requests):
        view_agenda_clin_med = {'data_do_aviso': requests[0], 'nome_paciente': requests[1],'prestador_cirurgia': requests[2], 'dt_chamada_transf': requests[3],'dt_centro_cirurgico': requests[4], 'data_da_cirurgia': requests[5],'dt_entrada_rpa': requests[6], 'dt_saida_rpa': requests[6],'centro_cirurgico': requests[7]}
        list_agenda_clin_med.append(view_agenda_clin_med)
        # end
    connection.commit()
    return list_agenda_clin_med


def receiver_agenda_cli_med():
    list_agenda = view_bloco()
    nlin = len(list_agenda)
    list_remove = list()
    
    for i in range(0, nlin):
        #verificar todos os campos que trabalham com datas se estao vazios
        a= 0     # irar depois

    nlin = len(list_agenda)
    list_agenda_cli_med  = []
    for i in range(0, nlin):
        if  list_agenda[i]['leito'] and list_agenda[i]['nome_paciente'] and list_agenda[i]['medico'] and list_agenda[i][
            'tecnico'] and list_agenda[i]['enfermeiro'] and list_agenda[i]['dias'] and list_agenda[i]['alta_prev'] and list_agenda[i]['el'] and list_agenda[i][
            'ep'] and list_agenda[i]['bs'] and list_agenda[i]['rx'] and list_agenda[i]['ed'] and list_agenda[i]['us'] and list_agenda[
            i]['pa'] and list_agenda[i]['ecg'] and list_agenda[i]['ac'] and list_agenda[i]['procedimentos']:
            dict_agenda = dict()
            dict_agenda['leito']         = list_agenda[i]['leito']
            dict_agenda['nome_paciente'] = list_agenda[i]['nome_paciente']
            dict_agenda['medico']        = list_agenda[i]['medico']
            dict_agenda['tecnico']       = list_agenda[i]['tecnico']
            dict_agenda['enfermeiro']    = list_agenda[i]['enfermeiro']
            dict_agenda['el']            = list_agenda[i]['el']
            dict_agenda['pa']            = list_agenda[i]['pa']
            dict_agenda['ecg']           = list_agenda[i]['ac']
            dict_agenda['procedimentos'] = list_agenda[i]['procedimentos']
            
            #verwificar condicoes para a efeutacao de salvamento da lista 
            
        list_agenda_cli_med.append(dict_agenda)
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