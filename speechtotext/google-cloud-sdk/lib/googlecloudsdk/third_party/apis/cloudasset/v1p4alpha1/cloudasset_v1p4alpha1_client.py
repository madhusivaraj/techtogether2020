"""Generated client library for cloudasset version v1p4alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudasset.v1p4alpha1 import cloudasset_v1p4alpha1_messages as messages


class CloudassetV1p4alpha1(base_api.BaseApiClient):
  """Generated client library for service cloudasset version v1p4alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudasset.googleapis.com/'

  _PACKAGE = u'cloudasset'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1p4alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudassetV1p4alpha1'
  _URL_VERSION = u'v1p4alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudasset handle."""
    url = url or self.BASE_URL
    super(CloudassetV1p4alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.v1p4alpha1 = self.V1p4alpha1Service(self)

  class V1p4alpha1Service(base_api.BaseApiService):
    """Service class for the v1p4alpha1 resource."""

    _NAME = u'v1p4alpha1'

    def __init__(self, client):
      super(CloudassetV1p4alpha1.V1p4alpha1Service, self).__init__(client)
      self._upload_configs = {
          }

    def AnalyzeIamPolicy(self, request, global_params=None):
      r"""Analyzes IAM policies based on the specified request. Returns.
a list of IamPolicyAnalysisResult matching the request.

      Args:
        request: (CloudassetAnalyzeIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeIamPolicyResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1p4alpha1/{v1p4alpha1Id}/{v1p4alpha1Id1}:analyzeIamPolicy',
        http_method=u'GET',
        method_id=u'cloudasset.analyzeIamPolicy',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'accessSelector_permissions', u'accessSelector_roles', u'identitySelector_identity', u'options_expandGroups', u'options_expandResources', u'options_expandRoles', u'options_maxFanoutsPerGroup', u'options_maxFanoutsPerResource', u'options_outputGroupEdges', u'options_outputPartialResultBeforeTimeout', u'options_outputResourceEdges', u'resourceSelector_fullResourceName'],
        relative_path=u'v1p4alpha1/{+parent}:analyzeIamPolicy',
        request_field='',
        request_type_name=u'CloudassetAnalyzeIamPolicyRequest',
        response_type_name=u'AnalyzeIamPolicyResponse',
        supports_download=False,
    )