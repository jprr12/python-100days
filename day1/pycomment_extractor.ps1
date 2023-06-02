$pythonScriptPath = "D:\Don't Ever Delete\My Documents\Repos\python-100days\day1\script.py"

# Read the Python script file
$scriptContent = Get-Content $pythonScriptPath

# Regex pattern to match Python comments
$commentPattern = '(?m)^\s*#(.*)$'

# Extract comments from the script
$comments = $scriptContent | Select-String -Pattern $commentPattern | ForEach-Object { $_.Matches.Groups[1].Value.Trim() }

# Output the comments
$comments

#to run this script in powershell:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned