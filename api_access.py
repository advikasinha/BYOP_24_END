'''
import ctypes

# Define the MessageBox function
MessageBox = ctypes.windll.user32.MessageBoxW

# Call MessageBox to display a test message
result = MessageBox(None, 'Hello, this is a test!', 'API Test', 1)

# Check the result
if result == 1:
    print('User clicked OK.')
else:
    print('User clicked Cancel or closed the dialog.')


import ctypes

# Define necessary constants and types
HWND_BROADCAST = 0xFFFF
WM_SETTEXT = 0x000C

# Load the user32.dll library
user32 = ctypes.windll.user32

def set_notepad_title(new_title):
    # Find the Notepad window by class name
    notepad_handle = user32.FindWindowW("Notepad", None)

    if notepad_handle == 0:
        print("Notepad not found.")
        return

    # Send a WM_SETTEXT message to set the window title
    user32.SendMessageW(notepad_handle, WM_SETTEXT, 0, new_title)

if __name__ == "__main__":
    new_title = "Modified Notepad Title"
    set_notepad_title(new_title)

import ctypes
from ctypes import Structure, windll, sizeof, byref

class OSVersionInfo(Structure):
    _fields_ = [("dwOSVersionInfoSize", ctypes.c_ulong),
                ("dwMajorVersion", ctypes.c_ulong),
                ("dwMinorVersion", ctypes.c_ulong),
                ("dwBuildNumber", ctypes.c_ulong),
                ("dwPlatformId", ctypes.c_ulong),
                ("szCSDVersion", ctypes.c_wchar * 128)]

def get_windows_version():
    osvi = OSVersionInfo()
    osvi.dwOSVersionInfoSize = sizeof(OSVersionInfo)

    if windll.kernel32.GetVersionExW(byref(osvi)):
        return osvi.dwMajorVersion, osvi.dwMinorVersion, osvi.dwBuildNumber, osvi.szCSDVersion
    else:
        return None

if __name__ == "__main__":
    version_info = get_windows_version()

    if version_info:
        print(f"Windows Version: {version_info[0]}.{version_info[1]}, Build {version_info[2]}")
        print(f"Service Pack: {version_info[3]}")
    else:
        print("Failed to retrieve Windows version information.")
'''
import ctypes
import datetime

#to check the accessibility of low level operations of underlying system
class SYSTEMTIME(ctypes.Structure):
    _fields_ = [
        ("wYear", ctypes.c_uint16),
        ("wMonth", ctypes.c_uint16),
        ("wDayOfWeek", ctypes.c_uint16),
        ("wDay", ctypes.c_uint16),
        ("wHour", ctypes.c_uint16),
        ("wMinute", ctypes.c_uint16),
        ("wSecond", ctypes.c_uint16),
        ("wMilliseconds", ctypes.c_uint16)
    ]

def set_system_time(year, month, day, hour, minute, second):
    
    kernel32 = ctypes.windll.kernel32

    # Get the current system time
    current_time = datetime.datetime.utcnow()
    
    
    new_time = SYSTEMTIME()
    new_time.wYear = ctypes.c_uint16(year)
    new_time.wMonth = ctypes.c_uint16(month)
    new_time.wDay = ctypes.c_uint16(day)
    new_time.wHour = ctypes.c_uint16(hour)
    new_time.wMinute = ctypes.c_uint16(minute)
    new_time.wSecond = ctypes.c_uint16(second)
    
    # Set the system time
    success = kernel32.SetSystemTime(ctypes.byref(new_time))
    
    return success

if __name__ == "__main__":
    new_year = 2024
    new_month = 1
    new_day = 21
    new_hour = 17
    new_minute = 3
    new_second = 30

    # Attempt to set the system time
    if set_system_time(new_year, new_month, new_day, new_hour, new_minute, new_second):
        print("System time successfully changed.")
    else:
        print("Failed to change system time.")
