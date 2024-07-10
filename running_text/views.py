from django.http import FileResponse, HttpResponse
from .create_running_text_video import create_running_text_video


def run_text(request):
    text = request.GET.get("text", "")
    if text.strip() == "":
        return HttpResponse("<h1>Для создания видео введите текст в параметр \"text\" адресной строки!</h1>")
    create_running_text_video(text)
    return FileResponse(open("video.mp4", "rb"), as_attachment=True)
