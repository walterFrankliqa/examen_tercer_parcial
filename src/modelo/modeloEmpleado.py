from flask import jsonify
from modelo.coneccion import db_connection
class EmpleadoModel():
    @classmethod
    def listar_empleado(self):
        try:
            conn = db_connection()
            cur = conn.cursor()
            cur.execute("select ci, nombre, fecha_nac, procedencia from empleado")
            datos = cur.fetchall()
            empleados =[]
            for fila in datos:
                empleado = {
                       'ci': fila[0],
                       'nombre': fila[1],
                       'fecha_nac': fila[2],
                       'procedencia': fila[3],
                       }
                empleados.append(empleado)
            conn.close()
            return jsonify({'empleados': empleados, 'mensaje': "Empleados listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})