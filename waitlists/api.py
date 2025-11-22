from ninja import Router
from .schema import *
from .models import WaitListEntry
from typing import List
from django.shortcuts import get_object_or_404
from .forms import WaitListEntryCreateForm
import helpers
import json

router = Router()


@router.get("", response=List[WaitListEntryListSchema], auth=helpers.api_auth_user_required)
def list_waitlist_entries(request):
    qs = WaitListEntry.objects.filter(user=request.user)
    return qs

@router.get("{entry_id}/", response=WaitListEntryDetailSchema, auth=helpers.api_auth_user_required)
def get_wishlist_entry(request, entry_id:int):
    obj = get_object_or_404(WaitListEntry, id=entry_id, user=request.user)
    return obj

@router.post("", response={
    200: WaitListEntryDetailSchema,
    400:  ErrorWaitListEntryCreateSchema
    }, auth=helpers.api_auth_user_or_annon)
def create_waitlist_entry(request, data:WaitListEntryCreateSchema):
    form = WaitListEntryCreateForm(data.dict())
    if not form.is_valid():
        form_errors = json.loads(form.errors.as_json())
        print(form_errors)
        return 400, form_errors
    obj = form.save(commit=False)
    if request.user.is_authenticated:
        obj.user = request.user
    obj.save()
    return obj

@router.put("{entry_id}/", response=WaitListEntryDetailSchema, auth=helpers.api_auth_user_required)
def update_wailist_entry(request, 
    entry_id:int, 
    payload:WaitlistEntryUpdateSchema
    ):
    print(entry_id)
    obj = get_object_or_404(
        WaitListEntry, 
        id=entry_id,
        user=request.user)
    payload_dict = payload.dict()
    for k,v in payload_dict.items():
        setattr(obj, k, v)
    obj.save()
    return obj

# http DELETE
@router.delete("{entry_id}/delete/", response=WaitListEntryDetailSchema, auth=helpers.api_auth_user_required)
def delete_wailist_entry(request, entry_id:int):
    obj = get_object_or_404(
        WaitListEntry, 
        id=entry_id,
        user=request.user)
    obj.delete()
    return obj