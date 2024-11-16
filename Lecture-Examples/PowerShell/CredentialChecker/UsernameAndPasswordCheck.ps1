$UserName = Read-Host "Enter username"
$SecurePassword = Read-Host "Enter passowrd" -AsSecureString

$Credentials = New-Object System.Management.Automation.PSCredential ($UserName, $SecurePassword)

$UsernameFromCreds = $Credentials.GetNetworkCredential().UserName
$PlainTextPassword = $Credentials.GetNetworkCredential().Password

if ($UsernameFromCreds -eq "danl" -and $PlainTextPassword -eq "abc123") {
    Write-Output "Hello $($Credentials.GetNetworkCredential().UserName), you can now access the system."
} else {
    Write-Host "System denied!"
}
