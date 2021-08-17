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
    #cursor_secundario = connection.cursor()

    # current_date = datetime.datetime.now()
    # date = current_date - datetime.timedelta(days = days)
    # date = date.strftime("%d/%m/%y")

    cont = 0
    select_requests = "select data_do_aviso, nome_paciente, prestador_da_cirurgia,dt_chamada_transf, dt_centro_cirurgico,data_da_cirurgia,dt_entrada_rpa,dt_saida_rpa,centro_Cirurgico from dbamv.vdic_agenda_cirurgia WHERE DT_AVISO >= to_date(SYSDATE) AND DT_AVISO < to_date(SYSDATE+1) AND CENTRO_CIRURGICO = 'CENTRO CIRURGICO'"
    request = cursor.execute(select_requests)
    for requests in cursor.execute(select_requests):
        view_agenda_clin_med = {'data_do_aviso': requests[0], 'nome_paciente': requests[1],'prestador_cirurgia': requests[2], 'dt_chamada_transf': requests[3],'dt_centro_cirurgico': requests[4], 'data_da_cirurgia': requests[5],'dt_entrada_rpa': requests[6], 'dt_saida_rpa': requests[6],'centro_cirurgico': requests[7]}
        list_agenda_clin_med.append(view_agenda_clin_med)
        # end
    connection.commit()
    return list_agenda_clin_med


