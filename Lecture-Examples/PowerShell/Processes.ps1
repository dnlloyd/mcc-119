Write-Host "Killing all BASH sessions!"

foreach ($Process in $(Get-Process | Where-Object ProcessName -Like "bash")) {
    Stop-Process -Id $Process.Id
}
