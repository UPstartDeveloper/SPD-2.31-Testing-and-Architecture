# by Kami Bigdely
# Remove control flag
# Reference: https://searchcode.com/file/92870153/frameworkconsole/framework.py/

MESSAGE = "Puts the Android Agent inside an Android App APK. \
    The application runs normally, with extra functionality."


def backdoor_srcmethod():
    print(MESSAGE)
    inputfile = input("APK to Backdoor: ").strip()
    while (inputfile == "") is False:
        print("doing other stuff.")
        print(MESSAGE)
        inputfile = input("APK to Backdoor: ").strip()


backdoor_srcmethod()
