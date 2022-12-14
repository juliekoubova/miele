#!/usr/bin/env pwsh

Using Namespace System.Globalization
Using Namespace System.Reflection
Using Namespace System.Resources

Param ([hashtable]$StringsByCulture)

$Source = Get-Content ProgramIdToNameConverter.cs -Raw
$Source = $Source -Replace '\(\) =>|\.RemoveParentheses\(\)', ''
$Source = $Source -Replace "(?ms)new Dictionary[^{]*{",'@('
$Source = $Source -Replace '};',')'
$Source = $Source -Replace '\{','@('
$Source = $Source -Replace '\}',')'
$Source = $Source -Replace 'Translations\.(\w+)','"$1"'
$Source = $Source -Replace '(\d+)L','$1'
$Source = $Source -Replace 'NoProgramSelectedKey', '"NoProgramSelectedKey"'
$Source = $Source -Replace 'LocalizationKeyDictionary', ''
$Source = "@{ $Source }"

$LaundryCare = [Assembly]::LoadFrom((Resolve-Path .\Miele.Modules.LaundryCare.dll))
$ResourceManager = New-Object ResourceManager 'Miele.Modules.LaundryCare.Localization.Translations', $LaundryCare

Function Normalize-GroupName ($Group) {
    Switch ($Group) {
        'SemiProfessionalTdProgram' { return 'semipro_dryer' }
        'SemiProfessionalWmProgram' { return 'semipro_washer' }
        'LegacyTdProgram' { return 'dop1_dryer' }
        'Dop2TdProgram' { return 'dop2_dryer' }
        'Dop2WmProgram' { return 'dop2_washer' }
        'Dop1WashingProgramNameMapping' { return 'dop1_washer'}
    }
}

Function Remove-Tags ($String) {
    $String -replace '<[^>]*>', ''
}

Function Normalize-ShortName ($ResourceKey) {
    $English = $ResourceManager.GetString($ResourceKey, 'en-US')
    If (-Not $English) {
        Return $ResourceKey
    }
    $English = $English.ToLower()
    $English = Remove-Tags $English
    $English = $English -replace "['\.]", ''
    $English = $English -replace ' ?\+', '_plus'
    $English = $English -replace '[-/]', ' '
    $English = $English.Trim() -replace '\s+', '_'
    $English
}

$Rows = $(ForEach ($Group In ($Source | Invoke-Expression).GetEnumerator()) {
    $GroupNormalized = Normalize-GroupName $Group.Key
    $(ForEach ($Entry In $Group.Value) {
        $ProgramID = $Entry[0]
        If ($ProgramID -Eq 0) {
            Continue
        }
        If ($ProgramID -Gt 0x8000000) {
            $ProgramID = '0x{0:x}' -F $ProgramID
        }
        New-Object PSCustomObject -Property @{
            Group = $GroupNormalized
            ProgramID = $ProgramID
            Resource = $Entry[1]
            ShortName = "${GroupNormalized}_program_$(Normalize-ShortName $Entry[1])"
        }
    }) | Sort-Object ProgramID
})

$Groups = $Rows | Group-Object Group

[CultureInfo[]]$Cultures =  Get-ChildItem -Recurse -Filter Miele.Modules.LaundryCare.resources.dll `
| Split-Path -Parent `
| Split-Path -Leaf `

$I = 0
$Total = $Groups.Length * $Cultures.Length

ForEach ($Group In $Groups) {
    $ProgramID_ShortName = @{}
    ForEach ($Row In $Group.Group) {
        $ProgramID_ShortName[$Row.ProgramID.ToString()] = $Row.ShortName
    }

    $ProgramID_ShortName | ConvertTo-Json > "$($Group.Name)_programs.json"

    ForEach ($Culture In $Cultures) {
        Write-Progress `
            -Activity "Reading laundry programs $($Group.Name)" `
            -Status $Culture.Name `
            -PercentComplete (($I/$Total) * 100)
        $I += 1

        If (-Not $StringsByCulture[$Culture.Name]) {
            $StringsByCulture[$Culture.Name] = @{}
        }

        $ShortName_Translation = @{}
        ForEach ($Row In $Group.Group) {
            $StringsByCulture[$Culture.Name][$Row.ShortName] = Remove-Tags ($ResourceManager.GetString($Row.Resource, $Culture))

        }
    }
}
# $Programs #| Format-Table ProgramId, ShortName, Localized -GroupBy Group
