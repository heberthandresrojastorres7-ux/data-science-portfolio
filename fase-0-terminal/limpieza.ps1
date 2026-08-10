# ============================================
#  SCRIPT DE LIMPIEZA AUTOMATICA - Downloads
#  Creado por: Heberth Rojas
#  Fecha: 2026
# ============================================

# 1. MOSTRAR EN QUE CARPETA ESTAMOS
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  LIMPIEZA AUTOMATICA DE DOWNLOADS" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Carpeta actual: $pwd" -ForegroundColor Yellow
Write-Host ""

# 2. CREAR CARPETAS SI NO EXISTEN
$carpetas = @("Instaladores_2026", "Documentos_Downloads", "Comprimidos", "Media", "Revisar_Borrar")

foreach ($carpeta in $carpetas) {
    if (!(Test-Path $carpeta)) {
        New-Item -ItemType Directory -Path $carpeta | Out-Null
        Write-Host "✅ Carpeta creada: $carpeta" -ForegroundColor Green
    } else {
        Write-Host "📁 Carpeta ya existe: $carpeta" -ForegroundColor Gray
    }
}

Write-Host ""

# 3. MOVER ARCHIVOS POR TIPO
Write-Host "📦 Moviendo archivos..." -ForegroundColor Cyan

# Instaladores
Move-Item *.exe, *.msi -Destination "Instaladores_2026\" -ErrorAction SilentlyContinue
Write-Host "   → .exe y .msi movidos a Instaladores_2026" -ForegroundColor Green

# Documentos
Move-Item *.pdf, *.docx, *.xlsx, *.pptx, *.doc, *.txt -Destination "Documentos_Downloads\" -ErrorAction SilentlyContinue
Write-Host "   → Documentos movidos a Documentos_Downloads" -ForegroundColor Green

# Comprimidos
Move-Item *.zip, *.rar, *.7z -Destination "Comprimidos\" -ErrorAction SilentlyContinue
Write-Host "   → Comprimidos movidos a Comprimidos" -ForegroundColor Green

# Media (fotos, videos)
Move-Item *.jpg, *.jpeg, *.png, *.gif, *.mp4, *.mp3, *.mov -Destination "Media\" -ErrorAction SilentlyContinue
Write-Host "   → Media movida a Media" -ForegroundColor Green

Write-Host ""

# 4. BORRAR ARCHIVOS TEMPORALES VIEJOS (mas de 30 dias)
Write-Host "🗑️ Buscando archivos temporales viejos..." -ForegroundColor Red

$fechaLimite = (Get-Date).AddDays(-30)
$temporales = Get-ChildItem *.log, *.tmp -ErrorAction SilentlyContinue | Where-Object { $_.LastWriteTime -lt $fechaLimite }

if ($temporales) {
    $temporales | ForEach-Object {
        Remove-Item $_.FullName -Recycle
        Write-Host "   🚮 Borrado (a Papelera): $($_.Name)" -ForegroundColor Red
    }
    Write-Host "   Total borrados: $($temporales.Count)" -ForegroundColor Red
} else {
    Write-Host "   ✅ No hay archivos temporales viejos" -ForegroundColor Green
}

Write-Host ""

# 5. MOVER LO QUE SOBRA A Revisar_Borrar
Write-Host "📂 Moviendo archivos restantes a Revisar_Borrar..." -ForegroundColor Yellow
Move-Item * -Exclude "Instaladores_2026", "Documentos_Downloads", "Comprimidos", "Media", "Revisar_Borrar", "limpieza.ps1" -Destination "Revisar_Borrar\" -ErrorAction SilentlyContinue
Write-Host "   → Hecho" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  LIMPIEZA COMPLETADA ✅" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan