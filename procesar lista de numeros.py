def procesar_cadena(cadena):
    # Separamos la cadena en secciones utilizando los puntos como delimitadores
    secciones = cadena.split('.')
    
    # Inicializamos el diccionario que contendrá la información procesada
    resultado = {"tiendas": {}, "pedido": {}}
    
    # Procesamos las secciones de las tiendas (todas excepto la última sección)
    for seccion in secciones[:-1]:
        # Separamos la sección por comas
        partes = seccion.split(',')
        
        # El primer elemento es el nombre de la tienda
        nombre_tienda = partes[0].strip()
        
        # Inicializamos una lista para los productos de esta tienda
        productos = []
        
        # Procesamos los productos
        for producto in partes[1:]:
            producto = producto.strip()
            partes_producto = producto.split(' ')
            
            cantidad = float(partes_producto[0])
            nombre_producto = " ".join(partes_producto[1:-1])
            
            if '/' in partes_producto[-1]:
                costo_compra, precio_venta = map(float, partes_producto[-1].split('/'))
            else:
                costo_compra = precio_venta = float(partes_producto[-1])
            
            productos.append({
                "cantidad": cantidad,
                "nombre": nombre_producto,
                "costo_compra": costo_compra,
                "precio_venta": precio_venta
            })
        
        # Guardamos la lista de productos en el diccionario de resultado
        resultado["tiendas"][nombre_tienda] = productos
    
    # Procesamos la última sección (datos del pedido)
    datos_pedido = secciones[-1].split(',')
    for dato in datos_pedido:
        clave, valor = dato.split(':')
        resultado["pedido"][clave.strip()] = float(valor.strip())
    
    return resultado

# Ejemplo de uso
cadena = "reyes, 1 coca 12/34, 3 elotes 23/34. irma, 1 platano 1/2, 3 leches lala 20. Total real:36, Cobro total:70, Tarifa:10, Propina:5, Final:85"
resultado = procesar_cadena(cadena)
print(resultado)
