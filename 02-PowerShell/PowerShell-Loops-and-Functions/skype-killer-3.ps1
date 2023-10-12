Write-Output "Listing all Skype processes"
Get-Process | Where-Object ProcessName -Like "*skype*"

function Close-Process-By-ID {
    param($proc_to_kill)
    Write-Output "Killing process: $($proc_to_kill.ProcessName) ($($proc_to_kill.Id))"
    $proc_to_kill.Kill()
}

foreach ($proc in (Get-Process | Where-Object ProcessName -Like "*skype*")) {
    Close-Process-By-ID -proc_to_kill $proc
}

Write-Output "Listing all Skype processes"
Get-Process | Where-Object ProcessName -Like "*skype*"
