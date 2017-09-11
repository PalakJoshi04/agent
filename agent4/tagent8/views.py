from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.forms import formset_factory
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Agent
from .forms import *
from django.shortcuts import render


class AgentList(ListView):
    model = Agent


class AgentCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes', 'mobile_number', 'phone_number', 'email_id', 'media_name', "media_path"]


class AgentAddLocCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes', 'mobile_number','phone_number', 'email_id', 'media_name', 'media_path']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddLocCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST)
            data['address'] = AddressFormSet(self.request.POST)
        else:
            data['location'] = LocationFormSet()
            data['address'] = AddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid() and address.is_valid():
                location.instance = self.object
                address.instance = self.object
                location.save()
                address.save()
        return super(AgentAddLocCreate, self).form_valid(form)


class AgentUpdate(UpdateView):
    model = Agent
    success_url = '/'
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes', 'mobile_number', 'phone_number', 'email_id', 'media_name', "media_path"]


class AgentAddLocUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes', 'mobile_number', 'phone_number', 'email_id', 'media_name', "media_path"]

    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddLocUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST, instance=self.object)
            data['address'] = AddressFormSet(self.request.POST, instance=self.object)
        else:
            data['location'] = LocationFormSet(instance=self.object)
            data['address'] = AddressFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid() and address.is_valid():
                location.instance = self.object
                address.instance = self.object
                location.save()
                address.save()
        return super(AgentAddLocUpdate, self).form_valid(form)


class AgentAddLocUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes', 'mobile_number', 'phone_number', 'email_id', 'media_name', "media_path"]
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddLocUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST, instance=self.object)
            data['address'] = AddressFormSet(self.request.POST, instance=self.object)
        else:
            data['location'] = LocationFormSet(instance=self.object)
            data['address'] = AddressFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid() and address.is_valid():
                location.instance = self.object
                address.instance = self.object
                location.save()
                address.save()
        return super(AgentAddLocUpdate, self).form_valid(form)


class AgentDelete(DeleteView):
    model = Agent
    success_url = reverse_lazy('agent-list')
