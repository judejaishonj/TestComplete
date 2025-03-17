def Test1():
  Browsers.Item[btChrome].Navigate("https://www.google.com/search?q=moolya&rlz=1C1GCEA_enIN1153IN1153&oq=moo&gs_lcrp=EgZjaHJvbWUqDggBEEUYJxg7GIAEGIoFMgYIABBFGDwyDggBEEUYJxg7GIAEGIoFMgYIAhBFGDkyFQgDEC4YJxivARjHARiABBiKBRiOBTISCAQQLhhDGK8BGMcBGIAEGIoFMhIIBRAuGEMYrwEYxwEYgAQYigUyDAgGEAAYQxiABBiKBTIGCAcQRRg90gEIMjMwNWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8")
  Aliases.browser.BrowserWindow.Maximize()

def Test2():
  Aliases.Notepad.wndNotepad.DesktopWindowXamlSource2.Click(317, 18)

def Test3():
  Aliases.explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(1331, 42)
  Aliases.Notepad.wndNotepad.NotepadTextBox.RichEditD2DPT.wtext = "Moolya"
