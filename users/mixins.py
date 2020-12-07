from django.shortcuts import redirect


class IsStaff(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)