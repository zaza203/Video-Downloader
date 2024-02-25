from django.shortcuts import render, redirect
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
