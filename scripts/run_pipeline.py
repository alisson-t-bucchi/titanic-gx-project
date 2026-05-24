import subprocess

scripts = [
    "scripts/load_mysql.py",
    "scripts/create_expectations.py",
    "scripts/validate_data.py"
]

for script in scripts:
    print(f"Executando {script}...")
    subprocess.run(["python", script], check=True)

print("Pipeline finalizada.")