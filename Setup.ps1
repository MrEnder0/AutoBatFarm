Write-Output "Installing projects dependencies and updating pip this should not take long."

python -m pip install --upgrade pip
pip install pyautogui

Write-Output "Done!"
