function GetCurrentYear {
    Param($YourAge, $Year)

    $CurrentYear = [int]$Age + [int]$BirthYear
    Write-Output "The current year is: $CurrentYear"
}

$BirthYear = Read-Host "What year were you born?"
$Age = Read-Host "How old are you?"

GetCurrentYear -YourAge $Age -Year $BirthYear
