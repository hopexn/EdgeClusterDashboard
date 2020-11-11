from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

ipset = {
    "edgecluster": "192.168.1.1"
}


def default(request):
    return render(request, "index.html")


def index(request, page_name):
    return render(request, page_name)


def camera_list(request):
    if "edgecluster" in ipset:
        url_tpl = "http://" + ipset["edgecluster"] + ":{}/substream"
        base_no = 10001
    else:
        url_tpl = "http://192.168.1.{}:8081/substream"
        base_no = 201
    
    cam_urls = []
    for i in range(14):
        port = base_no + i
        cam_urls.append(url_tpl.format(port))
    
    params = {"cam_urls": cam_urls}
    return render(request, "camera_list.html", params)


def get_camera(request, cam_no):
    if "edgecluster" in ipset:
        url_tpl = "http://" + ipset["edgecluster"] + ":{}/substream"
        base_no = 10000
    else:
        url_tpl = "http://192.168.1.{}:8081/substream"
        base_no = 200
    cam_no = int(cam_no)
    
    cam_url = url_tpl.format(base_no + cam_no)
    params = {"cam_url": cam_url, "cam_no": cam_no}
    return render(request, "get_camera.html", params)


def update_ip(request: HttpRequest, hostname):
    global ipset
    remote_addr = request.META.get("REMOTE_ADDR", None)
    if remote_addr is not None:
        ipset[hostname] = remote_addr
    return HttpResponse("update {}: {}".format(hostname, ipset.get(hostname, None)))


def get_ip(request, hostname):
    global ipset
    target_ip = ipset.get(hostname, None)
    if target_ip is not None:
        return HttpResponse(target_ip)
    else:
        return HttpResponse("{}".format(ipset))
