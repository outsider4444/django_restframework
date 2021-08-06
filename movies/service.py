def get_client_ip(request):
    """Получение Ip пользователя"""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get("Remote_ADDR")
    return ip
