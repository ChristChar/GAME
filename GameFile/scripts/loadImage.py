import pygame
import ctypes
import os
from ctypes import wintypes

LPOFNHOOKPROC = ctypes.c_voidp # TODO
LPCTSTR = LPTSTR = ctypes.c_wchar_p

class OPENFILENAME(ctypes.Structure):
    _fields_ = [("lStructSize", wintypes.DWORD),
                ("hwndOwner", wintypes.HWND),
                ("hInstance", wintypes.HINSTANCE),
                ("lpstrFilter", LPCTSTR),
                ("lpstrCustomFilter", LPTSTR),
                ("nMaxCustFilter", wintypes.DWORD),
                ("nFilterIndex", wintypes.DWORD),
                ("lpstrFile", LPTSTR),
                ("nMaxFile", wintypes.DWORD),
                ("lpstrFileTitle", LPTSTR),
                ("nMaxFileTitle", wintypes.DWORD),
                ("lpstrInitialDir", LPCTSTR),
                ("lpstrTitle", LPCTSTR),
                ("flags", wintypes.DWORD),
                ("nFileOffset", wintypes.WORD),
                ("nFileExtension", wintypes.WORD),
                ("lpstrDefExt", LPCTSTR),
                ("lCustData", wintypes.LPARAM),
                ("lpfnHook", LPOFNHOOKPROC),
                ("lpTemplateName", LPCTSTR),
                ("pvReserved", wintypes.LPVOID),
                ("dwReserved", wintypes.DWORD),
                ("flagsEx", wintypes.DWORD)]

GetOpenFileName = ctypes.windll.comdlg32.GetOpenFileNameW
GetSaveFileName = ctypes.windll.comdlg32.GetSaveFileNameW

OFN_ENABLESIZING      =0x00800000
OFN_PATHMUSTEXIST     =0x00000800
OFN_OVERWRITEPROMPT   =0x00000002
OFN_NOCHANGEDIR       =0x00000008
MAX_PATH=1024


def _buildOFN(title, default_extension, filter_string, fileBuffer):

  ofn = OPENFILENAME()
  ofn.lStructSize = ctypes.sizeof(OPENFILENAME)
  ofn.lpstrTitle = title
  ofn.lpstrFile = ctypes.cast(fileBuffer, LPTSTR)
  ofn.nMaxFile = MAX_PATH
  ofn.lpstrDefExt = default_extension
  ofn.lpstrFilter = filter_string
  ofn.Flags = OFN_ENABLESIZING | OFN_PATHMUSTEXIST | OFN_OVERWRITEPROMPT | OFN_NOCHANGEDIR
  return ofn


def loadFile(title, default_extension, filter_string, initialPath):
  if initialPath is None:
    initialPath = ""
  filter_string = filter_string.replace("|", "\0")
  fileBuffer = ctypes.create_unicode_buffer(initialPath, MAX_PATH)
  ofn = _buildOFN(title, default_extension, filter_string, fileBuffer)
  if GetOpenFileName(ctypes.byref(ofn)):
    return fileBuffer[:]
  else:
    return None



def loadImage(MaxFiles):
    oldPath = os.getcwd()
    file_paths = loadFile("scegli una immagine brutto idiota", None, "Image Files\0*.bmp;*.jpg;*.jpeg;*.png;*.gif\0",None)
    os.chdir(oldPath)
    if file_paths is None:
        return
    if MaxFiles > 1:
        images = [pygame.image.load(path) for path in file_paths]
        return images
    else:
        image = pygame.image.load(file_paths)
        return image
