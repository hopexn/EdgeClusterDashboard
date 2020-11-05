from django.shortcuts import render


def default(request):
    return render(request, "index.html")


def index(request, page_name):
    return render(request, page_name)


def camera_list(request):
    url_tpl = "http://219.223.186.25:{}"
    cam_urls = []
    for i in range(14):
        port = 10001 + i
        cam_urls.append(url_tpl.format(port))
    
    params = {"cam_urls": cam_urls}
    return render(request, "camera_list.html", params)


def get_camera(request, cam_no):
    cam_no = int(cam_no)
    url_tpl = "http://219.223.186.25:{}"
    cam_url = url_tpl.format(10001 + cam_no)
    params = {"cam_url": cam_url, "cam_no": cam_no}
    return render(request, "get_camera.html", params)
