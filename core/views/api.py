import json
from django.shortcuts import HttpResponse
from chronam.core.models import FundingSource, Type

def newspaper_types():
    data = []
    for t in Type.objects.all():
        type_data = dict(id = t.id, name = t.name)
        data.append(type_data)
    return HttpResponse(json.dumps(data), content_type='application/json')

def funding_sources():
    data = []
    for s in FundingSource.objects.all():
        source_data = dict(id = s.id, slug = s.slug, name = s.name)
        data.append(source_data)
    return HttpResponse(json.dumps(data), content_type='application/json')