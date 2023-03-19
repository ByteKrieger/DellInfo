import subprocess
import platform
import tkinter as tk
import webbrowser

def get_dell_info():
    os_name = platform.system()
    if os_name == 'Windows':
        cmd = 'wmic bios get serialnumber, smbiosbiosversion'
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        service_tag, asset_tag = output.strip().split('\n')[1].split()
    elif os_name == 'Linux':
        cmd = 'sudo dmidecode -s system-serial-number; sudo dmidecode -s baseboard-asset-tag'
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        service_tag, asset_tag = output.strip().split('\n')
    else:
        raise Exception('Unsupported OS')
    with open('dellinfo.txt', 'w') as f:
        f.write(f'Service Tag: {service_tag}\n')
        f.write(f'Asset Tag: {asset_tag}\n')
    return service_tag

def open_dell_website():
    service_tag = get_dell_info()
    answer = tk.messagebox.askquestion(title='Dell Support', message=f'Do you want to open Dell Support website for Service Tag {service_tag}?')
    if answer == 'yes':
        url = f'https://www.dell.com/support/contents/de-de/category/product-support/self-support-knowledgebase/locate-service-tag/{service_tag}'
        webbrowser.open_new(url)
    else:
        tk.messagebox.showinfo(title='Dell Info', message='Thank you for using the program.\nDeveloped by ByteKrieger.de')

if __name__ == '__main__':
    open_dell_website()
