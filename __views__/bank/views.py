from kernel.http import Response

def fetch_info(request):
    """
    @description: This function fetches the info of the user
    """ 
    res = Response(request=request)
    return res.success()