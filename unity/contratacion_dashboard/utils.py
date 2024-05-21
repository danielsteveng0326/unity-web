import csv
from datetime import datetime
from django.utils import timezone
from django.db import transaction
from .models import Contrato
from . import views

def cargar_datos_desde_csv():
    # Abrir el archivo CSV y cargar los datos
    ruta_archivo = "static/csv/2024_yar_alc.csv"
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter='|', quoting=csv.QUOTE_NONE, escapechar=' ')

        # Iterar sobre las filas del CSV y guardar los datos en la base de datos
        with transaction.atomic():
            for fila in lector_csv:
                id_contrato = fila['id_contrato']
                # Verificar si el id_contrato ya existe en la base de datos
                if not Contrato.objects.filter(id_contrato=id_contrato).exists():
                    contrato = Contrato(
                        id_contrato=id_contrato,
                        nombre_entidad=fila['nombre_entidad'],
                        nit_entidad=fila['nit_entidad'],
                        departamento=fila['departamento'],
                        ciudad=fila['ciudad'],
                        localizaci_n=fila['localizaci_n'],
                        orden=fila['orden'],
                        sector=fila['sector'],
                        rama=fila['rama'],
                        entidad_centralizada=fila['entidad_centralizada'],
                        proceso_de_compra=fila['proceso_de_compra'],
                        referencia_del_contrato=fila['referencia_del_contrato'],
                        estado_contrato=fila['estado_contrato'],
                        codigo_de_categoria_principal=fila['codigo_de_categoria_principal'],
                        descripcion_del_proceso=fila['descripcion_del_proceso'],
                        tipo_de_contrato=fila['tipo_de_contrato'],
                        modalidad_de_contratacion=fila['modalidad_de_contratacion'],
                        justificacion_modalidad_de=fila['justificacion_modalidad_de'],
                        fecha_de_firma=datetime.fromisoformat(fila['fecha_de_firma']) if fila['fecha_de_firma'] else None,
                        fecha_de_fin_del_contrato=datetime.fromisoformat(fila['fecha_de_fin_del_contrato']) if fila['fecha_de_fin_del_contrato'] else None,
                        condiciones_de_entrega=fila['condiciones_de_entrega'],
                        tipodocproveedor=fila['tipodocproveedor'],
                        documento_proveedor=fila['documento_proveedor'],
                        proveedor_adjudicado=fila['proveedor_adjudicado'],
                        es_grupo=fila['es_grupo'],
                        es_pyme=fila['es_pyme'],
                        habilita_pago_adelantado=fila['habilita_pago_adelantado'],
                        liquidaci_n=fila['liquidaci_n'],
                        obligaci_n_ambiental=fila['obligaci_n_ambiental'],
                        obligaciones_postconsumo=fila['obligaciones_postconsumo'],
                        reversion=fila['reversion'],
                        origen_de_los_recursos=fila['origen_de_los_recursos'],
                        destino_gasto=fila['destino_gasto'],
                        valor_del_contrato=int(fila['valor_del_contrato']),
                        valor_de_pago_adelantado=int(fila['valor_de_pago_adelantado']),
                        valor_facturado=int(fila['valor_facturado']),
                        valor_pendiente_de_pago=int(fila['valor_pendiente_de_pago']),
                        valor_pagado=int(fila['valor_pagado']),
                        valor_amortizado=int(fila['valor_amortizado']),
                        valor_pendiente_de=int(fila['valor_pendiente_de']),
                        valor_pendiente_de_ejecucion=int(fila['valor_pendiente_de_ejecucion']),
                        estado_bpin=fila['estado_bpin'],
                        c_digo_bpin=fila['c_digo_bpin'],
                        anno_bpin=fila['anno_bpin'],
                        saldo_cdp=int(fila['saldo_cdp']),
                        saldo_vigencia=int(fila['saldo_vigencia']),
                        espostconflicto=fila['espostconflicto'],
                        dias_adicionados=int(fila['dias_adicionados']),
                        puntos_del_acuerdo=fila['puntos_del_acuerdo'],
                        pilares_del_acuerdo=fila['pilares_del_acuerdo'],
                        urlproceso=fila['urlproceso'],
                        nombre_representante_legal=fila['nombre_representante_legal'],
                        nacionalidad_representante_legal=fila['nacionalidad_representante_legal'],
                        domicilio_representante_legal=fila['domicilio_representante_legal'],
                        tipo_de_identificaci_n_representante_legal=fila['tipo_de_identificaci_n_representante_legal'],
                        identificaci_n_representante_legal=fila['identificaci_n_representante_legal'],
                        g_nero_representante_legal=fila['g_nero_representante_legal'],
                        presupuesto_general_de_la_nacion_pgn=int(fila['presupuesto_general_de_la_nacion_pgn']),
                        sistema_general_de_participaciones=int(fila['sistema_general_de_participaciones']),
                        sistema_general_de_regal_as=int(fila['sistema_general_de_regal_as']),
                        recursos_propios_alcald_as_gobernaciones_y_resguardos_ind_genas=int(fila['recursos_propios_alcald_as_gobernaciones_y_resguardos_ind_genas']),
                        recursos_de_credito=int(fila['recursos_de_credito']),
                        recursos_propios=int(fila['recursos_propios']),
                        codigo_entidad=fila['codigo_entidad'],
                        codigo_proveedor=fila['codigo_proveedor'],
                        objeto_del_contrato=fila['objeto_del_contrato'],
                        fecha_de_inicio_del_contrato=datetime.fromisoformat(fila['fecha_de_inicio_del_contrato']) if fila['fecha_de_inicio_del_contrato'] else None,
                        ultima_actualizacion=datetime.fromisoformat(fila['ultima_actualizacion']) if fila['ultima_actualizacion'] else None,
                        fecha_inicio_liquidacion=datetime.fromisoformat(fila['fecha_inicio_liquidacion']) if fila['fecha_inicio_liquidacion'] else None,
                        fecha_fin_liquidacion=datetime.fromisoformat(fila['fecha_fin_liquidacion']) if fila['fecha_fin_liquidacion'] else None,
                    )
                    contrato.save()
                    
                else:
                    print(f"El contrato con ID {id_contrato} ya existe en la base de datos y no será insertado.")
