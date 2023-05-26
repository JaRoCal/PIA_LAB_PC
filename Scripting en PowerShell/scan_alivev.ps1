#Escaneo de equipos activos en la subred
#Determinando gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Tu gateway: $subred"
#
# Determinando rango de subred
#
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3 )
echo $rango
#
## Determinando si $rango termina en "."

$punto = $rango.EndsWith('.')
if ( $rango -like "False" )
{
	$rango = $rango + '.' #agregamps el punto en caso de que no estuviera.	
}

$rango_ip = @(1..254)

foreach ( $r in $rango_ip )
{
	$actual = $rango + $r
	$responde = Test-Connection $actual -Quiet -Count 1
	if ( $responde -eq "True" )
	{
		Write-Output ""
		Write-Host " Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
	}
}