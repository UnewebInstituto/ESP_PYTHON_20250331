# 1. Define la ruta base y el nombre de la tabla
$basePath = "C:/ESP_PYTHON_20250331/NIVEL_V/HENRY/excel"
$tableName = "persona_individuos"

# 2. Genera el timestamp dinámico
$timestamp = (Get-Date -Format "yyyyMMdd_HHmmss")

# 3. Construye el nombre completo del archivo
$csvFileName = "persona_$timestamp.csv"
$fullPath = Join-Path $basePath $csvFileName -Resolve

# 4. Construye el comando \copy
# Asegúrate de reemplazar 'tu_usuario' con tu usuario real
$copyCommand = "\copy (SELECT id, cedula, nombre, apellido, direccion, fechanac FROM $tableName) TO '$fullPath' WITH (FORMAT CSV, HEADER, DELIMITER ',');"

# 5. Ejecuta psql e inyecta el comando \copy
# Esto ejecuta psql, le pasa el comando y luego sale
psql -h localhost -p 5432 -U tu_usuario -d bd_nivel2_henry -c "$copyCommand"

Write-Host "Exportación a CSV completada en: $fullPath"