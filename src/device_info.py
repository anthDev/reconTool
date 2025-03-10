import usb.core
import usb.util
import re
import subprocess

# Script teste with a disabled SIP (from recovery mode using csrutil disable command) 
def find_iphone():
    # crosscheck Apple's Vendor ID (VID) -> 0x05AC
    VENDOR_ID = 0x05AC  # possible to change depending the device vendor.

    # Scan for USB devices
    devices = usb.core.find(find_all=True)

    for dev in devices:
        if dev.idVendor == VENDOR_ID:
            print(f"[+] Found iPhone (VID: {dev.idVendor}, PID: {dev.idProduct})")
            return dev

    print("[-] No iDevice detected.")
    return None

if __name__ == "__main__":
    find_iphone()

device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb")
devices = []
for i in df.split(b'\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
            devices.append(dinfo)
            
print(devices)