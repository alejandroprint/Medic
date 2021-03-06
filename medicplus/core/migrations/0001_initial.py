# Generated by Django 3.1.3 on 2020-11-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminsitrador',
            fields=[
                ('id_administrador', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=20, null=True)),
                ('apellido_paterno', models.CharField(max_length=20, null=True)),
                ('permisos', models.CharField(max_length=20, null=True)),
                ('ad_id_usuario', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'adminsitrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id_alergia', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'alergia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BotAyuda',
            fields=[
                ('idbot', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'bot_ayuda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CentroAtencion',
            fields=[
                ('id_centro', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_centro', models.CharField(max_length=20, null=True)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'centro_atencion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cirugia',
            fields=[
                ('id_cirugia', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('area_afectada', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'cirugia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cupo',
            fields=[
                ('id_cupo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('detalle_cupo', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'cupo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CupoTaller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_id_cupo', models.CharField(max_length=100)),
                ('t_id_taller', models.CharField(max_length=100)),
                ('f_id_ficha', models.CharField(max_length=100)),
                ('capacidad', models.CharField(max_length=100)),
                ('inscripcion', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'cupo_taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleInforme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('df_id_informe', models.CharField(max_length=20, null=True)),
                ('df_id_administrador', models.CharField(max_length=20, null=True)),
                ('hora_creacion', models.DateField(null=True)),
                ('solicitud', models.CharField(max_length=40, null=True)),
                ('dia_entrega', models.DateField(null=True)),
            ],
            options={
                'db_table': 'detalle_informe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleTaller',
            fields=[
                ('id_medi', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('de_id_taller', models.CharField(max_length=10, null=True)),
                ('fecha', models.DateField(null=True)),
                ('hora_inicio', models.DateField(null=True)),
                ('hora_termino', models.DateField(null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('duracion_total', models.DateField(null=True)),
            ],
            options={
                'db_table': 'detalle_taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id_diagnostico', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('ficha_id_ficha', models.CharField(max_length=10, null=True)),
                ('medico_id_medico', models.CharField(max_length=10, null=True)),
                ('hallazgo', models.CharField(max_length=50, null=True)),
                ('estado', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'diagnostico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id_enfermedad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('gravedad', models.CharField(max_length=40, null=True)),
                ('indicaciones', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'enfermedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialidad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=10, null=True)),
                ('area_especialidad', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'especialidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id_ficha', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('domicilio', models.CharField(max_length=50, null=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('ficha_id_sangre', models.CharField(max_length=10, null=True)),
                ('ficha_id_sexo', models.CharField(max_length=10, null=True)),
                ('ficha_id_centro', models.CharField(max_length=10, null=True)),
                ('ficha_id_sistema', models.CharField(max_length=10, null=True)),
                ('estado', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'ficha',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormularioConsulta',
            fields=[
                ('id_formulario', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('motivo_consulta', models.CharField(max_length=100, null=True)),
                ('fc_id_ficha', models.CharField(max_length=10, null=True)),
                ('sintoma', models.CharField(max_length=100, null=True)),
                ('hora_solicitud', models.DateField(null=True)),
                ('prioridad', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'formulario_consulta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gruposangre',
            fields=[
                ('id_sangre', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipo_sangre', models.CharField(max_length=40, null=True)),
            ],
            options={
                'db_table': 'gruposangre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialAlergias',
            fields=[
                ('ha_id_ficha', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('al_id_alergia', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('prevencion', models.CharField(max_length=100, null=True)),
                ('riesgos', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'historial_alergias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialCirugias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hc_id_ficha', models.CharField(max_length=10, null=True)),
                ('hc_id_cirugia', models.CharField(max_length=10, null=True)),
                ('tipo', models.CharField(max_length=40, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('fecha_realizacion', models.DateField(null=True)),
            ],
            options={
                'db_table': 'historial_cirugias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialMedicamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hm_id_ficha', models.CharField(max_length=10, null=True)),
                ('hm_id_medicamento', models.CharField(max_length=10, null=True)),
                ('descipcion', models.CharField(max_length=50, null=True)),
                ('tratamiento', models.CharField(max_length=100, null=True)),
                ('dosis_suministrada', models.CharField(max_length=100, null=True)),
                ('horario', models.DateField(null=True)),
            ],
            options={
                'db_table': 'historial_medicamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fi_id_ficha', models.CharField(max_length=10, null=True)),
                ('med_id_medico', models.CharField(max_length=10, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('dia_atencion', models.DateField(null=True)),
                ('observaciones', models.CharField(max_length=100, null=True)),
                ('derivaciones', models.CharField(max_length=100, null=True)),
                ('procedimiento', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'historial_medico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id_informe', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'informe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('gramos', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=100)),
                ('dosis_recomendada', models.CharField(max_length=50)),
                ('laboratorio', models.CharField(max_length=50)),
                ('contraindicacion', models.CharField(max_length=100)),
                ('med_id_tipo_medi', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'medicamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_medico', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('dv', models.CharField(max_length=1)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('horario', models.DateField()),
                ('centro_estudio', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'medico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id_opcion', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'opcion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('primer_nombre', models.CharField(max_length=20, null=True)),
                ('segundo_nombre', models.CharField(max_length=20, null=True)),
                ('apellido_paterno', models.CharField(max_length=20, null=True)),
                ('apellido_materno', models.CharField(max_length=20, null=True)),
                ('edad', models.CharField(max_length=3, null=True)),
            ],
            options={
                'db_table': 'paciente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'pregunta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecordatorioMedico',
            fields=[
                ('id_recordatorio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('detalle_recordatorio', models.CharField(max_length=100, null=True)),
                ('hora_recordatorio', models.DateField(null=True)),
            ],
            options={
                'db_table': 'recordatorio_medico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_respuesta', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'respuesta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id_sexo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('sigla', models.CharField(max_length=2, null=True)),
                ('detalle_genero', models.CharField(max_length=15, null=True)),
            ],
            options={
                'db_table': 'sexo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SistemaDeSalud',
            fields=[
                ('id_sistema', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_sistema', models.CharField(max_length=50, null=True)),
                ('ubicacion', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'sistema_de_salud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id_taller', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_taller', models.CharField(max_length=100, null=True)),
                ('tema', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoEspecialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_esp', models.CharField(max_length=10, null=True)),
                ('id_med', models.CharField(max_length=10, null=True)),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('orientacion', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'tipo_especialidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoMedicamento',
            fields=[
                ('id_tipo_medicamento', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('indicaciones', models.CharField(max_length=100, null=True)),
                ('especificacion', models.CharField(max_length=100, null=True)),
                ('enfermedad_a_tratar', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tipo_medicamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sigla', models.CharField(max_length=50, null=True)),
                ('correo_electronico', models.CharField(max_length=50, null=True)),
                ('contrasena', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
