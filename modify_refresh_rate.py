import ctypes

# Constants from winuser.h
VREFRESH = 116
DM_DISPLAYFREQUENCY = 0x00400000

CDS_TEST=0x02
CDS_SET_PRIMARY = 0x10
CDS_UPDATEREGISTRY= 0x01
CDS_RESET= 0x40000000
CDS_GLOBAL=0x08


# Structure for DEVMODE
class DEVMODE(ctypes.Structure):
    _fields_ = [
        ("dmPelsWidth", ctypes.c_long),
        ("dmPelsHeight", ctypes.c_long),
        ("dmDisplayFrequency", ctypes.c_long),
    ]

def get_basic_display_settings():
    hdc = ctypes.windll.user32.GetDC(0)
    refresh_rate = ctypes.windll.gdi32.GetDeviceCaps(hdc, VREFRESH)
    ctypes.windll.user32.ReleaseDC(0, hdc)
    print(f"Current Refresh Rate: {refresh_rate} Hz")
    return refresh_rate


def change_refresh_rate(new_refresh_rate):
    refresh_rate = get_basic_display_settings()

    devmode = DEVMODE()
    devmode.dmSize = ctypes.sizeof(devmode)
      
    devmode.dmDisplayFrequency = new_refresh_rate
    devmode.dmFields = DM_DISPLAYFREQUENCY

    flags = CDS_GLOBAL | CDS_UPDATEREGISTRY 

    result = ctypes.windll.user32.ChangeDisplaySettingsW(ctypes.byref(devmode), flags)


    if result != 0:
        print(f"New Refresh Rate: {new_refresh_rate} Hz")
    else:
        print(f"\nFailed to test display settings. Error code: {result}")

if __name__ == "__main__":
    change_refresh_rate(48)
