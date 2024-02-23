from django.shortcuts import render, redirect
from django.views import View
from pytube import YouTube, Playlist

def home(request):
    return render(request, 'home.html')

def get_video(request):
    url = request.GET['url']
    print(url)

    if not url:
        return render(request, 'home.html', {'message': "Please enter a valid URL"})
    
    try:
        yt = YouTube(url)
        title = yt.title
        print(title)
        watch_url = yt.watch_url
        embed = yt.embed_url
        print(embed)
        watch_url = yt.watch_url
        print(watch_url)
        streams = yt.streams.filter(progressive=True)
        print(streams)

    
    except Exception as e:
        return render(request, 'home.html', {"message": f'error fetching video: {e}'})

    
    return render(request, 'list.html', {'watch_url':watch_url, 'streams': streams, 'title': title, 'embed': embed})



def download_video(request, arg):
    path = '../../Downlaods'
    watch_url = arg[:43]
    print(watch_url)
    quality = arg[43:]
    print(quality)

    try:
        yt = YouTube(watch_url)
        streams = yt.streams.filter(progressive=True).get_by_resolution(quality).download(path)
        print("Videos downloaded successfully")

    except Exception as e:
        return render(request, 'home.html', {'message': f'Error downloading video: {e}'})

    return redirect('home.html')



# def home(request):
#     return render(request, "home.html")

# def get_video(request):
#     url = request.GET['url']

#     if not url:
#         return render(request, "home.html", {"message": "Please provide a URL"})
    
#     try:
#         yt = YouTube(url)
#         embed = yt.embed_url
#         title = yt.title
#         streams = yt.streams.filter(progressive=True)
            

#     except Exception as e:
#         return render(request, 'home.html', {'message': f'Error fetching videos: {e}'})
    
#     return render(request, "list.html", {"streams": streams, "embed": embed, "url": url, "title": title})


# def get_playlist(request):
#     url = request.GET['play-url']

#     if not url:
#         return render(request, "home.html", {"message": "Please provide a URL"})
    
#     try:
#         playlist = Playlist(url)
#         title = playlist.title
#         videos = []
#         embed = []
#         for video_url in playlist.video_urls:
#             yt = YouTube(video_url)
#             videos.append({"id": yt.video_id, "title": yt.title, "resolution": [stream.resolution for stream in yt.streams.filter(progressive=True)]})
#             embed.append(yt.embed_url)
#     except Exception as e:
#         return render(request, 'home.html', {'message': f'Error fetching videos: {e}'})
    

#     return render(request, "list.html", {"embed": embed, "videos": videos,"url": url, "title": title})

# def download_video(request, url):
#     path = "../../Downloads"
#     yt = YouTube(url)
#     url2 = yt.watch_url
#     obj = YouTube(url2)
#     obj.streams.filter(progressive=True).get_by_resolution(quality).download(path)
#     print("Video downloaded successfully")

#     return redirect("home.html")




# https://youtube.com/playlist?list=PLU1ICX1TLRrD1VMWAnlaO2lIZ6wy5RxCw&si=w66MH0vZR7pLsU66

# https://youtu.be/UD-MkihnOXg?si=0Sc7F-3V8sfR4t5U