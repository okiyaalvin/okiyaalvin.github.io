import os
import zipfile

def recursive_unzip(start_zip):
    current_zip_path = os.path.abspath(start_zip)
    base_dir = os.path.dirname(current_zip_path)

    count = 0
    while True:
        with zipfile.ZipFile(current_zip_path) as zf:
            # Assume only one file inside
            names = zf.namelist()
            if len(names) != 1:
                print(f"[!] Unexpected contents in {current_zip_path}: {names}")
                break

            inner_file = names[0]
            inner_name = os.path.splitext(os.path.basename(inner_file))[0]

            # Prepare output directory
            next_dir = os.path.join(base_dir, f"extracted_{count}")
            os.makedirs(next_dir, exist_ok=True)

            try:
                print(f"[+] Extracting {current_zip_path} using password: {inner_name}")
                zf.extract(inner_file, path=next_dir, pwd=inner_name.encode())
            except RuntimeError as e:
                print(f"[!] Failed to extract {current_zip_path} with password '{inner_name}': {e}")
                break

            # Move to next ZIP
            current_zip_path = os.path.join(next_dir, inner_file)
            if not zipfile.is_zipfile(current_zip_path):
                print(f"[✓] Extraction complete. Final file: {current_zip_path}")
                break

            count += 1

# Replace with your actual starting ZIP file
if __name__ == "__main__":
    recursive_unzip("ExtractMe.zip")