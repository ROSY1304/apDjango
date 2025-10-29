import os
import requests

# === CONFIGURACIÓN ===
folders = {
    "user_datasets": "https://drive.google.com/uc?export=download&id=1SQD2lpRCVEF-hBOnLXbeiwdTS0XIyTTV",
    "datasets": "https://drive.google.com/uc?export=download&id=1qV0FIrHDwlsgv4thV9sa5YB6rkPhklTN",
    "modelo": "https://drive.google.com/uc?export=download&id=11u2pm9kWffxqdeaHQVCwI95vVudVl_1n"
}

def download_file(url, output_path):
    print(f"⬇️ Descargando {output_path} ...")
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Descargado correctamente: {output_path}")
    except Exception as e:
        print(f"⚠️ Error al descargar {url}: {e}")

# === DESCARGA DE ARCHIVOS ===
os.makedirs("datasets", exist_ok=True)
os.makedirs("user_datasets", exist_ok=True)
os.makedirs("modelo", exist_ok=True)

# Guardar en las rutas que Django espera
download_file(folders["user_datasets"], "user_datasets/user_datasets.csv")
download_file(folders["datasets"], "datasets/datasets.csv")
download_file(folders["modelo"], "modelo/rf_clasificador.joblib")

print("🎉 Todos los archivos fueron descargados correctamente.")
