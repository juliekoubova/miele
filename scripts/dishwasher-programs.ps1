#!/usr/bin/env pwsh

Using Namespace System.Reflection
Using Namespace System.Globalization

Param([CultureInfo]$Culture)

[CultureInfo]::CurrentUICulture = $Culture
$DishwasherUI = [Assembly]::LoadFrom((Resolve-Path .\Miele.Modules.Dishwasher.UI.dll))
$ProgramTranslations = $DishwasherUI.GetType('Miele.Modules.Dishwasher.UI.Translations.ProgramTranslations', $true)
$Translations = $ProgramTranslations::TranslationsAndIconSourceData

$ProgramID_ShortName = [Ordered]@{}
$ShortName_Translation = [Ordered]@{}

$Mapping = $ProgramTranslations.GetProperty('TranslationData', [BindingFlags]'NonPublic,Static').GetValue($null).GetEnumerator() `
| Where-Object Key -NE 0 ` # ignore the NONE value, it's something like "Please select"
| ForEach-Object {
    $ShortName = ($_.Value.ToLower() -Replace '^GLOBAL_PRG(_DW)?_','dishwasher_program_')
    $ProgramID_ShortName[$_.Key.ToString()] = $ShortName
    $ShortName_Translation[$ShortName] = $Translations[$_.Value].Item2 -Replace ' \{0\}(\{1\})?',''
}

$ProgramID_ShortName | ConvertTo-Json > dishwasher_programs.json
$ShortName_Translation | ConvertTo-Json