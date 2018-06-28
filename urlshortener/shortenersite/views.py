from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from shortenersite.models import Urls
from urlshortener.settings import SITE_URL
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.template.context_processors import csrf
from django.shortcuts import render
from django.utils import timezone
from shortenersite.lib.customparser import get_text_from_page

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('shortenersite/index.html', c)

def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id) # get object, if not        found return 404 error
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)

def shorten_url(request):
    url = request.POST.get("url", '')
    user_short_url = request.POST.get("user_short_url", '')
    if not (url == ''):
        if not (user_short_url == ''):
            short_id = user_short_url
        else:
            short_id = get_short_code()
        text = get_text_from_page(url)
        b = Urls(httpurl=url, short_id=short_id, text=text)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")

def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id

def urls_list(request):
    urls = Urls.objects.order_by('pub_date')
    return render(request, 'shortenersite/allurls.html', {'urls': urls, 'site_url': SITE_URL})
