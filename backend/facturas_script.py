# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from datetime import date

# def crear_factura(datos):
#     c = canvas.Canvas(f"factura_{datos['numero']}.pdf", pagesize=A4)
#     ancho, alto = A4

#     # === Imagen (logo) ===
#     # Cambia "logo.png" por el nombre de tu imagen
#     # width y height en puntos (1 punto ≈ 1/72 pulgadas)
#     c.drawImage(datos['logo'], 400, alto - 100, width=120, height=60, preserveAspectRatio=True, mask='auto')

#     # Encabezado
#     c.setFont("Helvetica-Bold", 20)
#     c.drawString(50, alto - 50, "FACTURA")

#     # Datos de la empresa
#     c.setFont("Helvetica", 10)
#     c.drawString(50, alto - 80, "Mi Empresa S.A.")
#     c.drawString(50, alto - 95, "Calle Falsa 123, Ciudad")
#     c.drawString(50, alto - 110, "Tel: +53 555 555")

#     # Datos del cliente
#     c.setFont("Helvetica-Bold", 12)
#     c.drawString(50, alto - 150, "Facturar a:")
#     c.setFont("Helvetica", 10)
#     c.drawString(50, alto - 165, datos['cliente'])
#     c.drawString(50, alto - 180, datos['direccion'])

#     # Fecha y número
#     c.drawString(400, alto - 150, f"Factura N°: {datos['numero']}")
#     c.drawString(400, alto - 165, f"Fecha: {date.today()}")

#     # Tabla de productos
#     y = alto - 220
#     c.setFont("Helvetica-Bold", 10)
#     c.drawString(50, y, "Descripción")
#     c.drawString(300, y, "Precio")
#     c.drawString(370, y, "Cantidad")
#     c.drawString(450, y, "Total")

#     c.setFont("Helvetica", 10)
#     for item in datos['items']:
#         y -= 20
#         c.drawString(50, y, item['descripcion'])
#         c.drawString(300, y, f"{item['precio']:.2f}")
#         c.drawString(370, y, str(item['cantidad']))
#         c.drawString(450, y, f"{item['precio'] * item['cantidad']:.2f}")

#     # Total final
#     y -= 40
#     c.setFont("Helvetica-Bold", 12)
#     c.drawString(370, y, "TOTAL:")
#     c.drawString(450, y, f"{datos['total']:.2f}")

#     c.save()

# Ejemplo de uso
# factura = {
#     "numero": "001",
#     "cliente": "Juan Pérez",
#     "direccion": "Calle Real 45, La Habana",
#     "logo": "logo.png",
#     "items": [
#         {"descripcion": "Diseño web", "precio": 250.00, "cantidad": 1},
#         {"descripcion": "Hosting anual", "precio": 80.00, "cantidad": 1},
#     ],
#     "total": 330.00
# }



# crear_factura(factura)

