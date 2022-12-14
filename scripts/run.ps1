$StringsByCulture = @{}

& "${PSScriptRoot}/laundry-programs.ps1" $StringsByCulture
& "${PSScriptRoot}/all-dishwasher-programs.ps1" $StringsByCulture

ForEach ($Entry in $StringsByCulture.GetEnumerator()) {
    $Entry.Value | ConvertTo-Json > "strings_$($Entry.Key).json"
}