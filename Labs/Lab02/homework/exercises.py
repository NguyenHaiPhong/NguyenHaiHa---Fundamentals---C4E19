from youtube_dl import YoutubeDL
# download_a_vid = YoutubeDL()
# download_a_vid.download(["https://www.youtube.com/watch?v=WHK5p7JL7g4"])

download_vids = YoutubeDL()
download_vids.download(["https://www.youtube.com/watch?v=wNVIn-QS4DE", \
"https://www.youtube.com/watch?v=JZjRrg2rpic"])

options_1 = {
    "format": "bestaudio/audio"
}
download_audio = YoutubeDL(options_1)
download_audio.download(["https://www.youtube.com/watch?v=c3jHlYsnEe0"])

options_2 = {
    "default_search": "ytsearch",
    "max_downloads": 1
}
download_the_1st_vid = YoutubeDL(options_2)
download_the_1st_vid.download(["con điên TAMKA PKL"])

options_3 = {
    "default_search": "ytsearch",
    "max_downloads": 1, 
    "format": "bestaudio/audio"
}
download_the_1st_audio = YoutubeDL(options_3)
download_the_1st_audio.download(["Nhớ mưa sài gòn lam trường"])