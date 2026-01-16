import os
import shutil
import datetime

def create_backup(source_folder, destination_folder):
    # Generar nombre único con fecha
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{date_str}"
    
    # Ruta completa del archivo comprimido
    full_path = os.path.join(destination_folder, backup_name)

    try:
        print(f"[*] Iniciando backup de: {source_folder}")
        # Comprimir la carpeta en formato .zip
        shutil.make_archive(full_path, 'zip', source_folder)
        print(f"[+] Archivo creado con éxito: {full_path}.zip")
        
        # Simulación de subida a la nube
        print(f"[*] Sincronizando {backup_name}.zip con el servidor remoto...")
        print("[OK] Sincronización completada al 100%.")
        
    except Exception as e:
        print(f"[!] Error durante el proceso: {e}")

if _name_ == "_main_":
    # Configuración de carpetas (Asegúrate de que estas carpetas existan para la prueba)
    ORIGEN = "./mi_data_importante"
    DESTINO = "./backups_locales"

    # Crear carpetas de ejemplo si no existen
    if not os.path.exists(ORIGEN): os.makedirs(ORIGEN)
    if not os.path.exists(DESTINO): os.makedirs(DESTINO)

    create_backup(ORIGEN, DESTINO)
