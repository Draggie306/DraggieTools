:: created by Draggie
:: discord.gg/GfetCXH
@echo off
echo Created by Draggie!
title Command Repeating Batch File
for /R %%a in (*.fsb) do (
  pushd "%%~dpa"
  "D:\Supercell Extraction Tools\Bank Files (to wav)\bank files\fsb_aud_extr.exe" "%%~nxa"
  popd
)