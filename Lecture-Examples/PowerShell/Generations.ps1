$BirthYear = Read-Host "What year were you born"

switch ($BirthYear)
{
    {$_ -lt 1899} {Write-Output "No idea. Just happy you're alive.`n"}
    {$_ -gt 1900 -and $_ -lt 1924} {Write-Output "Gen: The G.I. Generation (Greatest Generation)`n"}
    {$_ -gt 1925 -and $_ -lt 1945} {Write-Output "Gen: The Silent Generation (Lucky Few)`n"}
    {$_ -gt 1946 -and $_ -lt 1965} {Write-Output "Gen: The Baby Boom Generation (Baby Boomers)`n"}
    {$_ -gt 1966 -and $_ -lt 1979} {Write-Output "Gen: Generation X (Latchkey Kids)`n"}
    {$_ -gt 1980 -and $_ -lt 1994} {Write-Output "Gen: Generation Y (Millennials)`n"}
    {$_ -gt 1995 -and $_ -lt 2016} {Write-Output "Gen: Gen: Generation Z (Gen Next)`n"}
    {$_ -gt 2016} {Write-Output "Gen: Too young to tell`n"}
    default {Write-Output "Invalid birth year`n"}
}
