$Cultures = Get-ChildItem -Recurse -Filter Miele.Modules.Dishwasher.UI.resources.dll `
| Split-Path -Parent `
| Split-Path -Leaf `

$I = 0
$Cultures | ForEach-Object {
    Write-Progress `
        -Activity "Reading dishwasher programs" `
        -Status $_ `
        -PercentComplete (($I/$Cultures.Length) * 100)
    pwsh -File (Join-Path $PSScriptRoot "dishwasher-programs.ps1") $_
    $I += 1
}