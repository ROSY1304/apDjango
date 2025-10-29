import os
import requests

# === CONFIGURACIÓN ===
# URLs directas de descarga desde Google Drive
folders = {
    "user_datasets": "https://drive.google.com/uc?export=download&id=1SQD2lpRCVEF-hBOnLXbeiwdTS0XIyTTV",
    "datasets": "https://drive.google.com/uc?export=download&id=1qV0FIrHDwlsgv4thV9sa5YB6rkPhklTN",
    "modelo": "https://drive.google.com/uc?export=download&id=11u2pm9kWffxqdeaHQVCwI95vVudVl_1n"
}

# === FUNCIONES ===
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
os.makedirs("models", exist_ok=True)

for name, url in folders.items():
    if "modelo" in name:
        path = os.path.join("models", f"{name}.pkl")
    else:
        path = os.path.join("datasets", f"{name}.csv")
    download_file(url, path)

print("🎉 Todos los archivos fueron descargados correctamente.")
