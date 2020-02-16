import ftplib


def is_file(ftp, filename):
    current = ftp.pwd()
    try:
        ftp.cwd(filename)
    except:
        ftp.cwd(current)
        return True
    ftp.cwd(current)
    return False


FTP_SERVER = "127.0.0.1"
FTP_PORT = 6500
FTP_ID = "ftp_user"
FTP_PASS = "comnet@@"

ftp = ftplib.FTP()
ftp.encoding = 'euc-kr'
ftp.connect(FTP_SERVER, FTP_PORT)
print(ftp.login(FTP_ID, FTP_PASS))

while True:

    current = ftp.pwd()
    cmd = input("FTP {}> ".format(current))
    args = cmd.split(" ")
    if len(args) <= 0:
        continue

    command = args[0]
    del args[0]

    if command == "exit":
        break
    if command == "dir" or command == "ls":
        lists = ftp.nlst()
        for l in lists:
            if is_file(ftp, l):
                print(l)
            else:
                print("{}{}/".format(current, l))
    elif command == "cd":
        target = args[0]
        if not is_file(ftp, target):
            ftp.cwd(target)
    elif command == "mkdir" or command == "md":
        target = args[0]
        ftp.mkd(target)
    elif command == "delete" or "del":
        target = args[0]
        ftp.delete(target)
    elif command == "up":
        target = args[0]
        filename = target.split("\\")[-1]
        with open(target, "rb") as file:
            ftp.storbinary("STOR " + filename, file, 2048)
    elif command == "down":
        target = args[0]
        with open(target, "wb") as file:
            def callback(data):
                file.write(data)
            ftp.retrbinary("RETR " + target, callback=callback)


ftp.close()
