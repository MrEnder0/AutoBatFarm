import pyautogui, keyboard, time

print('██████╗░░█████╗░████████╗  ███████╗░█████╗░██████╗░███╗░░░███╗\n██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║\n██████╦╝███████║░░░██║░░░  █████╗░░███████║██████╔╝██╔████╔██║\n██╔══██╗██╔══██║░░░██║░░░  ██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║\n██████╦╝██║░░██║░░░██║░░░  ██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║\n╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝');input("Press Enter to start...")
if not input=='x':
  print('Started...')
  while True:
   pyautogui.click(85,50);time.sleep(5)
   if keyboard.is_pressed('x'):break
