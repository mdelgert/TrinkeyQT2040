# Get the current working directory
$currentPath = Get-Location

$sourcePath = Join-Path $currentPath "Mouse"

# Set the destination path
$destinationPath = "E:\"

# Check if the source folder exists
if (Test-Path $sourcePath -PathType Container) {
    # Copy all items from source to destination
    Copy-Item -Path "$sourcePath\*" -Destination $destinationPath -Recurse -Force

    Write-Host "Copy completed successfully."
} else {
    Write-Host "Source folder not found: $sourcePath"
}
