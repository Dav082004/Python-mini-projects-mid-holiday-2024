import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime
import random

class PDF(FPDF):
    def header(self):
        self.add_font('ArialUnicode', '', 'arial-unicode-ms.ttf', uni=True)
        self.set_font('ArialUnicode', size=12)
        self.cell(0, 10, 'SySCursos Company', ln=True)

class InvoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Generador de Facturas')
        
        # Lista para almacenar las entradas de productos
        self.products = []
        
        # Crear los widgets de la interfaz de usuario
        self.create_widgets()

    def create_widgets(self):
        """
        Crea los widgets de la interfaz de usuario y los organiza en la ventana.
        """
        # Crear un marco para organizar los widgets
        frame = ttk.Frame(self.root, padding='10')
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear un marco para la información del cliente
        client_info_frame = ttk.Frame(frame)
        client_info_frame.grid(row=0, column=0, columnspan=2, pady=5)

        # Campos para la información del cliente
        ttk.Label(client_info_frame, text='Nombre del Cliente').grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.client_name_entry = ttk.Entry(client_info_frame, width=30)
        self.client_name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        ttk.Label(client_info_frame, text='Apellidos del Cliente').grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.client_surname_entry = ttk.Entry(client_info_frame, width=30)
        self.client_surname_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        ttk.Label(client_info_frame, text='Teléfono del Cliente').grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.client_phone_entry = ttk.Entry(client_info_frame, width=30)
        self.client_phone_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        ttk.Label(client_info_frame, text='DNI del Cliente').grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.client_dni_entry = ttk.Entry(client_info_frame, width=30)
        self.client_dni_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        ttk.Label(client_info_frame, text='Ciudad del Cliente').grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.client_city_entry = ttk.Entry(client_info_frame, width=30)
        self.client_city_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        # Crear un marco para la entrada de productos
        self.product_frame = ttk.Frame(frame)
        self.product_frame.grid(row=1, column=0, columnspan=2, pady=10)

        # Añadir la primera fila de productos
        self.add_product_row()
        
        # Botón para agregar más filas de productos
        add_product_btn = ttk.Button(frame, text='Agregar Producto', command=self.add_product_row)
        add_product_btn.grid(row=2, column=0, columnspan=2, pady=5)

        # Botón para generar la factura
        generate_invoice_btn = ttk.Button(frame, text='Generar Factura', command=self.generate_invoice)
        generate_invoice_btn.grid(row=3, column=0, columnspan=2, pady=5)

        # Botón para reiniciar los campos
        reset_fields_btn = ttk.Button(frame, text='Reiniciar Campos', command=self.reset_fields)
        reset_fields_btn.grid(row=4, column=0, columnspan=2, pady=5)

    def add_product_row(self):
        """
        Añade una nueva fila de entradas para un producto.
        """
        # Contador para el número de productos
        row = len(self.products)
        
        # Crear campos de entrada para el nombre del producto, descripción y total
        ttk.Label(self.product_frame, text=f'Producto {row+1} Nombre').grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
        product_name_entry = ttk.Entry(self.product_frame, width=20)
        product_name_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)
        
        ttk.Label(self.product_frame, text='Descripción').grid(row=row, column=2, sticky=tk.W, padx=5, pady=2)
        product_description_entry = ttk.Entry(self.product_frame, width=40)
        product_description_entry.grid(row=row, column=3, sticky=(tk.W, tk.E), padx=5, pady=2)
        
        ttk.Label(self.product_frame, text='Total (€)').grid(row=row, column=4, sticky=tk.W, padx=5, pady=2)
        product_total_entry = ttk.Entry(self.product_frame, width=10)
        product_total_entry.grid(row=row, column=5, sticky=(tk.W, tk.E), padx=5, pady=2)
        
        # Añadir los campos de producto a la lista
        self.products.append((product_name_entry, product_description_entry, product_total_entry))

    def generate_invoice(self):
        """
        Genera la factura en formato PDF con los datos ingresados.
        """
        # Obtener datos del cliente
        client_name = self.client_name_entry.get()
        client_surname = self.client_surname_entry.get()
        client_phone = self.client_phone_entry.get()
        client_dni = self.client_dni_entry.get()
        client_city = self.client_city_entry.get()

        # Obtener fecha actual y generar identificador de factura
        invoice_date = datetime.now().strftime('%d/%m/%Y')
        invoice_id = 'F' + str(random.randint(1000000, 9999999))

        # Crear el PDF
        pdf = PDF()
        pdf.add_page()

        # Añadir encabezado de la factura
        pdf.set_xy(10, 10)
        pdf.set_font('ArialUnicode', size=12)
        pdf.cell(0, 10, 'SySCursos Company', ln=True)
        pdf.cell(0, 10, 'Calle No existe N30 CP 21020', ln=True)
        pdf.cell(0, 10, 'B32312312', ln=True)
        pdf.cell(0, 10, f'Fecha: {invoice_date}', ln=True)

        pdf.ln(20)

        # Añadir título de la factura
        pdf.set_font('ArialUnicode', size=16)
        pdf.cell(0, 10, 'FACTURA', ln=True, align='C')

        # Añadir número de factura
        pdf.set_font('ArialUnicode', size=12)
        pdf.cell(0, 10, f'Número de Factura: {invoice_id}', ln=True, align='C')

        pdf.ln(10)

        # Añadir datos del cliente
        pdf.set_font('ArialUnicode', size=12)
        pdf.cell(0, 10, 'Datos del Cliente', ln=True, align='L')
        pdf.cell(0, 10, f'Nombre: {client_name}', ln=True, align='L')
        pdf.cell(0, 10, f'Apellidos: {client_surname}', ln=True, align='L')
        pdf.cell(0, 10, f'Teléfono: {client_phone}', ln=True, align='L')
        pdf.cell(0, 10, f'DNI: {client_dni}', ln=True, align='L')
        pdf.cell(0, 10, f'Ciudad: {client_city}', ln=True, align='L')

        pdf.ln(10)

        # Añadir detalles del servicio
        pdf.cell(0, 10, 'Detalles del Servicio', ln=True, align='L')
        pdf.cell(0, 10, '---------------------------------', ln=True, align='L')

        # Añadir encabezados de la tabla
        pdf.set_font('ArialUnicode', size=12)
        pdf.cell(60, 10, 'Nombre del Servicio', border=1)
        pdf.cell(80, 10, 'Descripción del Servicio', border=1)
        pdf.cell(30, 10, 'Total', border=1, ln=True)

        # Añadir filas de productos
        total_amount = 0
        for product in self.products:
            name_entry, description_entry, total_entry = product
            product_name = name_entry.get()
            product_description = description_entry.get()
            product_total = float(total_entry.get() or 0)  # Asegurarse de que el total sea un número

            pdf.cell(60, 10, product_name, border=1)
            pdf.cell(80, 10, product_description, border=1)
            pdf.cell(30, 10, f'{product_total:.2f}', border=1, ln=True)

            total_amount += product_total

        # Añadir el total general
        pdf.cell(0, 10, '================================================', ln=True, align='L')
        pdf.cell(0, 10, f'Total General: {total_amount:.2f} EUR', ln=True, align='L')
        pdf.cell(0, 10, 'Gracias por su compra!', ln=True, align='C')

        # Guardar el archivo PDF
        pdf_file = f'Factura_{client_name}_{client_surname}.pdf'
        pdf.output(pdf_file, 'F')
        messagebox.showinfo('Factura Generada', f'Factura generada exitosamente y guardada como {pdf_file}.')

    def reset_fields(self):
        """
        Limpia todos los campos de entrada y reinicia la lista de productos.
        """
        # Limpiar campos de cliente
        self.client_name_entry.delete(0, tk.END)
        self.client_surname_entry.delete(0, tk.END)
        self.client_phone_entry.delete(0, tk.END)
        self.client_dni_entry.delete(0, tk.END)
        self.client_city_entry.delete(0, tk.END)

        # Limpiar campos de productos
        for product in self.products:
            for widget in product:
                widget.delete(0, tk.END)

        # Eliminar las filas de productos
        for product in self.products:
            for widget in product:
                widget.destroy()

        self.products.clear()
        self.add_product_row()

if __name__ == '__main__':
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()
