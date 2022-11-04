import pytube
link = input("Enter the YouTube video URL: ")
dn = pytube.YouTube(link)
dn.streams.first().download()
print("Your Video Has Been Downloaded", link)