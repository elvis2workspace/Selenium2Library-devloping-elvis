set process=westone.md.enterprisecontracts

@adb shell dumpsys meminfo %process% | findstr "Pss"

:m

@adb shell dumpsys meminfo %process% | findstr "TOTAL"

@ping -n 5 127.1 > nul

@goto m