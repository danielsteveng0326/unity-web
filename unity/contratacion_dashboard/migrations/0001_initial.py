# Generated by Django 5.0.6 on 2024-05-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id_contrato', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre_entidad', models.CharField(max_length=100)),
                ('nit_entidad', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('localizaci_n', models.CharField(max_length=100)),
                ('orden', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=100)),
                ('rama', models.CharField(max_length=20)),
                ('entidad_centralizada', models.CharField(max_length=20)),
                ('proceso_de_compra', models.CharField(max_length=100)),
                ('referencia_del_contrato', models.CharField(max_length=100)),
                ('estado_contrato', models.CharField(max_length=20)),
                ('codigo_de_categoria_principal', models.CharField(max_length=100)),
                ('descripcion_del_proceso', models.CharField(max_length=500)),
                ('tipo_de_contrato', models.CharField(max_length=100)),
                ('modalidad_de_contratacion', models.CharField(max_length=100)),
                ('justificacion_modalidad_de', models.CharField(max_length=100)),
                ('fecha_de_firma', models.DateTimeField(null=True)),
                ('fecha_de_fin_del_contrato', models.DateTimeField(null=True)),
                ('condiciones_de_entrega', models.CharField(max_length=100)),
                ('tipodocproveedor', models.CharField(max_length=100)),
                ('documento_proveedor', models.CharField(max_length=100)),
                ('proveedor_adjudicado', models.CharField(max_length=200)),
                ('es_grupo', models.CharField(max_length=100)),
                ('es_pyme', models.CharField(max_length=100)),
                ('habilita_pago_adelantado', models.CharField(max_length=100)),
                ('liquidaci_n', models.CharField(max_length=100)),
                ('obligaci_n_ambiental', models.CharField(max_length=100)),
                ('obligaciones_postconsumo', models.CharField(max_length=100)),
                ('reversion', models.CharField(max_length=100)),
                ('origen_de_los_recursos', models.CharField(max_length=100)),
                ('destino_gasto', models.CharField(max_length=100)),
                ('valor_del_contrato', models.BigIntegerField()),
                ('valor_de_pago_adelantado', models.BigIntegerField()),
                ('valor_facturado', models.BigIntegerField()),
                ('valor_pendiente_de_pago', models.BigIntegerField()),
                ('valor_pagado', models.BigIntegerField()),
                ('valor_amortizado', models.BigIntegerField()),
                ('valor_pendiente_de', models.BigIntegerField()),
                ('valor_pendiente_de_ejecucion', models.BigIntegerField()),
                ('estado_bpin', models.CharField(max_length=100)),
                ('c_digo_bpin', models.CharField(max_length=100)),
                ('anno_bpin', models.CharField(max_length=100)),
                ('saldo_cdp', models.BigIntegerField()),
                ('saldo_vigencia', models.BigIntegerField()),
                ('espostconflicto', models.CharField(max_length=100)),
                ('dias_adicionados', models.BigIntegerField()),
                ('puntos_del_acuerdo', models.CharField(max_length=100)),
                ('pilares_del_acuerdo', models.CharField(max_length=100)),
                ('urlproceso', models.CharField(max_length=500)),
                ('nombre_representante_legal', models.CharField(max_length=200)),
                ('nacionalidad_representante_legal', models.CharField(max_length=100)),
                ('domicilio_representante_legal', models.CharField(max_length=100)),
                ('tipo_de_identificaci_n_representante_legal', models.CharField(max_length=100)),
                ('identificaci_n_representante_legal', models.CharField(max_length=100)),
                ('g_nero_representante_legal', models.CharField(max_length=100)),
                ('presupuesto_general_de_la_nacion_pgn', models.BigIntegerField()),
                ('sistema_general_de_participaciones', models.BigIntegerField()),
                ('sistema_general_de_regal_as', models.BigIntegerField()),
                ('recursos_propios_alcald_as_gobernaciones_y_resguardos_ind_genas', models.BigIntegerField()),
                ('recursos_de_credito', models.BigIntegerField()),
                ('recursos_propios', models.BigIntegerField()),
                ('codigo_entidad', models.CharField(max_length=100)),
                ('codigo_proveedor', models.CharField(max_length=100)),
                ('objeto_del_contrato', models.CharField(max_length=500)),
                ('fecha_de_inicio_del_contrato', models.DateTimeField(null=True)),
                ('ultima_actualizacion', models.DateTimeField(null=True)),
                ('fecha_inicio_liquidacion', models.DateTimeField(null=True)),
                ('fecha_fin_liquidacion', models.DateTimeField(null=True)),
            ],
        ),
    ]
