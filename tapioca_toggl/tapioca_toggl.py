# -*- coding: utf-8 -*-

from tapioca import (
    JSONAdapterMixin,
    TapiocaAdapter,
    generate_wrapper_from_adapter,
)

from requests.auth import HTTPBasicAuth

from .resource_mapping import RESOURCE_MAPPING


class TogglClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://www.toggl.com/api/v8/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(TogglClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )

        access_token = api_params.get('access_token')

        if access_token:
            params['auth'] = HTTPBasicAuth(access_token, 'api_token')
        else:
            params['auth'] = HTTPBasicAuth(
                api_params.get('user'),
                api_params.get('password')
            )

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Toggl = generate_wrapper_from_adapter(TogglClientAdapter)
