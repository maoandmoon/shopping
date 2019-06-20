from django import forms
from .models import Order
from django.forms import formsets



class CheckoutForm(forms.Form):
    pass


class OrderItemForm(forms.Form):
    pass

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', )
        # fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

# class CollectionTitleForm(forms.ModelForm):
#
#     class Meta:
#         model = CollectionTitle
#         exclude = ()
#
# CollectionTitleFormSet = inlineformset_factory(
#     Collection, CollectionTitle, form=CollectionTitleForm,
#     fields=['name', 'language'], extra=1, can_delete=True
#     )
#
# Next, we add this formset to a CollectionCreate view.
#
# views.py:
#
# from .models import *
# from .forms import *
# from django.views.generic.edit import CreateView, UpdateView
# from django.urls import reverse_lazy
# from django.db import transaction
#
# class CollectionCreate(CreateView):
#     model = Collection
#     template_name = 'mycollections/collection_create.html'
#     form_class = CollectionForm
#     success_url = None
#
#     def get_context_data(self, **kwargs):
#         data = super(CollectionCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['titles'] = CollectionTitleFormSet(self.request.POST)
#         else:
#             data['titles'] = CollectionTitleFormSet()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         titles = context['titles']
#         with transaction.atomic():
#             form.instance.created_by = self.request.user
#             self.object = form.save()
#             if titles.is_valid():
#                 titles.instance = self.object
#                 titles.save()
#         return super(CollectionCreate, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('mycollections:collection_detail', kwargs={'pk': self.object.pk})
#
