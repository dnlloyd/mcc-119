$UserName = Read-Host "Enter username"
$SecurePassword = Read-Host "Enter passowrd" -AsSecureString

$Credentials = New-Object System.Management.Automation.PSCredential ($UserName, $SecurePassword)

if ($Credentials.GetNetworkCredential().Password -eq "abc123") {
    Write-Output "Hello $UserName, you can now access the system."
} else {
    Write-Host "System denied!"
}
