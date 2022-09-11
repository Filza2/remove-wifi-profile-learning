import os,subprocess
res=subprocess.run(["nmcli","-t","-f","TYPE,UUID","con"],capture_output=True,text=True).stdout.split('\n')
for TweakPY in res:
    parts=TweakPY.split(":")
    if (parts[0]=="802-11-wireless"):
        print('\n')
        os.system("nmcli connection delete uuid "+ parts[1])
print("\n[+] Done\n")
os.system("nmcli connection")
