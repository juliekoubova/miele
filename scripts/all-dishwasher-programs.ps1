Using Namespace System.Globalization

Param ([hashtable]$StringsByCulture)

[CultureInfo[]]$Cultures = Get-ChildItem -Recurse -Filter Miele.Modules.Dishwasher.UI.resources.dll `
| Split-Path -Parent `
| Split-Path -Leaf `

$I = 0
$Cultures | ForEach-Object {
    Write-Progress `
        -Activity "Reading dishwasher programs" `
        -Status $_ `
        -PercentComplete (($I/$Cultures.Length) * 100)
    $Json = pwsh -File (Join-Path $PSScriptRoot "dishwasher-programs.ps1") $_.Name | ConvertFrom-Json -AsHashTable

    ForEach ($Entry in $Json.GetEnumerator()) {
        $StringsByCulture[$_.Name][$Entry.Key] = $Entry.Value
    }

    $I += 1
}