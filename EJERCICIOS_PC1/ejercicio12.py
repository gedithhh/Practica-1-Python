nombre_archiv = input("Ingrese el nombre del archivo: ")

extension = nombre_archiv.lower().split('.')[-1]

tipos_de_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}


tipo_mime = tipos_de_mime.get(extension, 'application/octet-stream')


print(f"El tipo MIME del archivo {nombre_archiv} es {tipo_mime}")