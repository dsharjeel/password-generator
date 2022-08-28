import urllib.request

images = [
    "https://blog.6clicks.com/hubfs/growth%20acceptance.png",
    "https://www.6clicks.com/hubfs/People%20Pics/Team%20Photos/no-background-team.png",
    "https://www.6clicks.com/hs-fs/hubfs/2-2.png",
    "https://blog.6clicks.com/hubfs/Digitally%20transforming%20service%20delivery%20for%20IRM%20advisors%20and%20MSPs.png",
    "https://www.6clicks.com/hubfs/Digitally%20transforming%20service%20delivery%20for%20IRM%20advisors%20and%20MSPs.png",
    "https://www.6clicks.com/hubfs/Marketplace%20Item%20Logos/FedRAMP-LOGO-square.png",
    "https://www.6clicks.com/hubfs/Logos/6clicks%20Logos/6clicks%20Blue%20with%20White%20BG%20PNG.png"
    ]

for idx in range(len(images)):
    img = images[idx]
    n = img.split("/")[-1]
    name = n.replace("%20", " ")
    urllib.request.urlretrieve(str(img), str(name))
    print(idx, "Done")
