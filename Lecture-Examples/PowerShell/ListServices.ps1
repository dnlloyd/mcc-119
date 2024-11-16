Write-Host "Services that are stopped:"

foreach ($Service in $(Get-Service)) {
    if ($Service.status -eq "Stopped") {
        Write-Host $service.Name
    }
}
