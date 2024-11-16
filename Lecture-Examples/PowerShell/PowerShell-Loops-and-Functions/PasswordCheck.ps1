$CorrectUsername = "danl"
$CorrectPlainPassword = "abc123"
$CorrectSecurePassword = $CorrectPlainPassword | ConvertTo-SecureString -AsPlainText -Force
$CorrectCredentials = New-Object System.Management.Automation.PSCredential -ArgumentList $CorrectUsername, $CorrectSecurePassword

$UserName = Read-Host "Enter username"
$SecurePassword = Read-Host "Enter passowrd" -AsSecureString
$Credentials = New-Object System.Management.Automation.PSCredential ($UserName, $SecurePassword)

if ($Credentials.GetNetworkCredential().Password -eq $CorrectCredentials.GetNetworkCredential().Password) {
    Write-Output "Hello $Username, you can now access the system."
} else {
    Write-Host "System denied!"
}

# https://learn.microsoft.com/en-us/powershell/scripting/learn/deep-dives/add-credentials-to-powershell-functions?view=powershell-7.4
# https://learn.microsoft.com/en-us/archive/technet-wiki/4546.working-with-passwords-secure-strings-and-credentials-in-windows-powershell