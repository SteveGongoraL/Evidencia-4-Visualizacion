import cx_Oracle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
from fpdf import FPDF

def guardar_proyecto(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11):
    try:
        # Realizar la conexion.
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
        cursor= conexion.cursor()
        # Pasar valores y definir la sentencia SQL.
        valores = {"MATRICULA":i3, "NOMBRE":i0, "APELLIDOP":i1, "APELLIDOM":i2, "EDAD":i4, "CALLE":i5, "NUMERO":i6, "CARRERA":i7, "MUNICIPIO":i8, "ESTADO":i9, "BECA":i10, "MATERIAS":i11}
        statement="INSERT INTO CLIENTES(MATRICULA, NOMBRE, APELLIDOP, APELLIDOM, EDAD, CALLE, NUMERO, CARRERA, MUNICIPIO, ESTADO, BECA, MATERIAS) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :i12)"
        cursor.execute(statement, (i3, i0, i1, i2, i4, i5, i6, i7, i8, i9, i10, i11))
        conexion.commit()
        print("Se han guardado los datos!!\n")
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conexion.close()

def consultar_proyecto(i3):
    try:
        # Se realiza la conexion, seguido de la consulta, pasandole el dato que puso el usuario para saber de que fila actualizar datos.
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
        cursor= conexion.cursor()
        cursor.execute("SELECT * FROM CLIENTES WHERE MATRICULA= '%s'" %i3)
        row= cursor.fetchone()
        print(row)
    except Exception as e:
        print(str(e))
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        cursor.close()
        conexion.close()

def actualizar_proyecto(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11):
    try:
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
        cursor= conexion.cursor()
        valores = {"MATRICULA":i3, "NOMBRE":i0, "APELLIDOP":i1, "APELLIDOM":i2, "EDAD":i4, "CALLE":i5, "NUMERO":i6, "CARRERA":i7, "MUNICIPIO":i8, "ESTADO":i9, "BECA":i10, "MATERIAS":i11}
        cursor.execute("UPDATE CLIENTES SET NOMBRE= :NOMBRE, APELLIDOP= :APELLIDOP, APELLIDOM= :APELLIDOM, EDAD= :EDAD, CALLE= :CALLE, NUMERO= :NUMERO, CARRERA= :CARRERA, MUNICIPIO= :MUNICIPIO, ESTADO= :ESTADO, BECA= :BECA, MATERIAS= :MATERIAS WHERE MATRICULA= :MATRICULA", valores)
        conexion.commit()
        print(f"Se ha actualizado el registro con la matricula {i3}.\n")
    except Exception as e:
        print(str(e))
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_proyecto(i3):
    try:
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
        cursor= conexion.cursor()
        cursor.execute("DELETE FROM CLIENTES WHERE MATRICULA= '%s'" % i3)
        conexion.commit()
        print(f"Se ha eliminado el registro con la matricula: {i3}.\n")
    except Exception as e:
        print(str(e))
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        cursor.close()
        conexion.close()

def imprimir_proyecto():
    try:
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
        cursor= conexion.cursor()
        # Realizar Consultas.
        cursor.execute("SELECT MATRICULA, NOMBRE, APELLIDOP, APELLIDOM, EDAD, CALLE, NUMERO, ESTADO, BECA FROM CLIENTES ORDER BY CARRERA")
        result= cursor.fetchall()
        cursor.execute("SELECT CARRERA, MUNICIPIO, MATERIAS FROM CLIENTES ORDER BY CARRERA")
        result2= cursor.fetchall()
        cursor.execute("SELECT carrera, COUNT(*) AS AlumnosEnCarrera FROM clientes GROUP BY carrera")
        result3= cursor.fetchall()
        pdf=FPDF(format='letter', unit='in', orientation='L')
        pdf.add_page()
        pdf.set_font('Times','',10.0)
        epw=pdf.w - 4*pdf.l_margin
        col_width=epw/10
        # Escribir un Tecto.
        pdf.set_font('Times','B',16.0)
        pdf.cell(epw, 0.0, 'Reporte de Datos Evidencia 4', align='C')
        pdf.set_font('Times','',10.0)
        pdf.ln(0.5)
        th= pdf.font_size
        # Almacenar los datos.
        for row in result:
            for datum in row:
                pdf.cell(col_width, th, str(datum), border=1)
            pdf.ln(th)
        # Pasar Espacio.
        pdf.ln(2*th)
        epw2=pdf.w - 1*pdf.l_margin
        col_width2=epw2/4
        for row in result2:
            for datum in row:
                pdf.cell(col_width2, th, str(datum), border='L''T''B')
            pdf.ln(th)
        pdf.ln(4*th)
        pdf.set_font('Times','B',16.0)
        pdf.cell(epw, 0.0, 'Agrupados por Carrera', align='C')
        pdf.set_font('Times','',10.0)
        pdf.ln(0.5)
        th= pdf.font_size
        for row in result3:
            for datum in row:
                pdf.cell(col_width2, th, str(datum), border=1)
            pdf.ln(th)
        # Nombre del Archivo.
        pdf.output('evidencia_4.pdf','F')
        print("Se ha creado un archivo PDF con el nombre 'evidencia_4'.\n")
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conexion.close()

def conexion_DB(self):
    conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
    cursor= conexion.cursor()
    cursor.execute("SELECT MATRICULA, NOMBRE, APELLIDOP, APELLIDOM, EDAD, CALLE, NUMERO, CARRERA, MUNICIPIO, ESTADO, BECA, MATERIAS FROM CLIENTES")
    result= cursor.fetchall()
    self.tableWidget.clearContents()
    row = 0
    for endian in result:
        self.tableWidget.setRowCount(row + 1)
        idDato = QTableWidgetItem(endian[0])
        idDato.setTextAlignment(4)
        self.tableWidget.setItem(row, 0, idDato)
        self.tableWidget.setItem(row, 1, QTableWidgetItem(endian[1]))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(endian[2]))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(endian[3]))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(str(endian[4])))
        self.tableWidget.setItem(row, 5, QTableWidgetItem(endian[5]))
        self.tableWidget.setItem(row, 6, QTableWidgetItem(str(endian[6])))
        self.tableWidget.setItem(row, 7, QTableWidgetItem(endian[7]))
        self.tableWidget.setItem(row, 8, QTableWidgetItem(endian[8]))
        self.tableWidget.setItem(row, 9, QTableWidgetItem(endian[9]))
        self.tableWidget.setItem(row, 10, QTableWidgetItem(endian[10]))
        self.tableWidget.setItem(row, 11, QTableWidgetItem(endian[11]))
        row += 1
    cursor.close()
    conexion.close()

class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("CapturaDatos.ui",self)
        # Se define la accion que tendra cada boton al ser seleccionado.
        self.Boton_Grabar.clicked.connect(self.guardar)
        self.Boton_Consulta.clicked.connect(self.consulta)
        self.Boton_Limpiar.clicked.connect(self.limpiar)
        self.Boton_Actualizar.clicked.connect(self.actualizar)
        self.Boton_Eliminar.clicked.connect(self.eliminar)
        self.Boton_Imprimir.clicked.connect(self.imprimir)
        conexion_DB(self)

    def guardar(self):
        i0= str(self.val0.toPlainText())
        i1= str(self.val1.toPlainText())
        i2= str(self.val2.toPlainText())
        i3= str(self.val3.toPlainText())
        i4= int(self.val4.toPlainText())
        i5= str(self.val5.toPlainText())
        i6= int(self.val6.toPlainText())
        i7=self.cBoxCarrera.currentText()
        i8=self.cBoxMun.currentText()
        i9=self.cBoxEst.currentText()
        if self.radioButton0.isChecked():
            i10=0
        elif self.radioButton50.isChecked():
            i10=50
        elif self.radioButton80.isChecked():
            i10=80
        elif self.radioButton100.isChecked():
            i10=100
        else:
            print()
        materias= list()
        if self.cBoxProg.isChecked():
            materia1=("Programacion")
            materias.append(materia1)
        if self.cBoxEsta.isChecked():
            materia2=("Estadistica")
            materias.append(materia2)
        if self.cBoxConta.isChecked():
            materia3=("Contabilidad")
            materias.append(materia3)
        if self.cBoxDB.isChecked():
            materia4=("Base de Datos")
            materias.append(materia4)
        if self.cBoxInv.isChecked():
            materia5=("Investigación de Operaciones")
            materias.append(materia5)
        i11=str(materias)
        # Pasar todos los elementos definidos por el usuario, a la funcion que los guardara en la Base de Datos.
        guardar_proyecto(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11)
        conexion_DB(self)

    def consulta(self):
        i3= str(self.val3.toPlainText())
        consultar_proyecto(i3)

    def limpiar(self):
        # Ciclo for para limpiar el textEdit, CheckBox y RadioButton.
        for line in [self.val0, self.val1,self.val2,self.val3,self.val4,self.val5,self.val6]: line.clear()
        for box in [self.cBoxProg,self.cBoxEsta,self.cBoxConta,self.cBoxDB,self.cBoxInv]:box.setChecked(False)
        self.cBoxCarrera.setCurrentIndex(-1)
        self.cBoxMun.setCurrentIndex(-1)
        self.cBoxEst.setCurrentIndex(-1)
        for buttn in [self.radioButton0, self.radioButton50, self.radioButton80, self.radioButton100]:
            buttn.setAutoExclusive(False)
            buttn.setChecked(False)
            buttn.repaint()
            buttn.setAutoExclusive(True)

    def actualizar(self):
        # Se le pasan los datos que actualizara y mas abajo se especifica a que matricula sera a la que se aplicaran los cambios.
        i0= str(self.val0.toPlainText())
        i1= str(self.val1.toPlainText())
        i2= str(self.val2.toPlainText())
        i3= str(self.val3.toPlainText())
        i4= int(self.val4.toPlainText())
        i5= str(self.val5.toPlainText())
        i6= int(self.val6.toPlainText())
        i7=self.cBoxCarrera.currentText()
        i8=self.cBoxMun.currentText()
        i9=self.cBoxEst.currentText()
        if self.radioButton0.isChecked():
            i10=0
        elif self.radioButton50.isChecked():
            i10=50
        elif self.radioButton80.isChecked():
            i10=80
        elif self.radioButton100.isChecked():
            i10=100
        else:
            print()
        materias= list()
        if self.cBoxProg.isChecked():
            materia1=("Programacion")
            materias.append(materia1)
        if self.cBoxEsta.isChecked():
            materia2=("Estadistica")
            materias.append(materia2)
        if self.cBoxConta.isChecked():
            materia3=("Contabilidad")
            materias.append(materia3)
        if self.cBoxDB.isChecked():
            materia4=("Base de Datos")
            materias.append(materia4)
        if self.cBoxInv.isChecked():
            materia5=("Investigación de Operaciones")
            materias.append(materia5)
        i11=str(materias)
        actualizar_proyecto(i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11)
        conexion_DB(self)

    def eliminar(self):
        i3= str(self.val3.toPlainText())
        eliminar_proyecto(i3)
        conexion_DB(self)

    def imprimir(self):
        imprimir_proyecto()

app=QApplication(sys.argv)
dialogo = Ui_Dialog()
dialogo.show()
app.exec_()