import speedtest

teste = speedtest.Speedtest()

down = teste.download()
upload = teste.upload()

print(float(down)/8)
print(float(upload)/8)