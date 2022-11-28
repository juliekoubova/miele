#!/usr/bin/env pwsh

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

$(ForEach ($Group In ($Source | Invoke-Expression).GetEnumerator()) {
    $(ForEach ($Entry In $Group.Value) {
        New-Object PSCustomObject -Property @{
            Group = $Group.Key
            ProgramId = $Entry[0]
            ShortName = $Entry[1]
        }
    }) | Sort-Object ProgramId
}) | Format-Table ProgramId, ShortName -GroupBy Group