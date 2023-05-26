#Jaime Ronaldo Calderon Sanchez 1970947
# CODIGO CORREGIDO
# Escaneo de equipos activos en la subred
# Determinando gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando tu gateway ..."
Write-Host "Tu gateway: $subred"
#
# Determinando rango de subred
#
$rango = $subred.Substring(0, $subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host "== Determinando tu rango de subred ..."
echo $rango
#
# Determinando si $rango termina en "."
$punto = $rango.EndsWith('.')
if (-not $punto) {
    $rango = $rango + '.' # agregamos el punto en caso de que no estuviera.
}

$rango_ip = @(1..254)
Write-Output ""
Write-Host "-- Subred actual:"
Write-Host "Escaneando: " -NoNewline
Write-Host $rango -NoNewline
Write-Host "0/24" -ForegroundColor Red
Write-Output ""
foreach ($r in $rango_ip) {
    $actual = $rango + $r
    $responde = Test-Connection $actual -Quiet -Count 1
    if ($responde) {
        Write-Output ""
        Write-Host "Host responde: " -NoNewline
        Write-Host $actual -ForegroundColor Green
    }
}
