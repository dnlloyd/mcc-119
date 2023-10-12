# Get-Process -Id 9168 | Get-Member
# Get-Process | Where-Object ProcessName -Like "*skype*"

Write-Output "Finding all Skype processes"

foreach ($proc in (Get-Process | Where-Object ProcessName -Like "*skype*")) {
    Write-Output "Killing process: $($proc.ProcessName) ($($proc.Id))"
    $proc.Kill()
}
