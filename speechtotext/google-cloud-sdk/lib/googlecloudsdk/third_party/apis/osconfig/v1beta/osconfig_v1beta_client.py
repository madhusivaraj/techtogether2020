"""Generated client library for osconfig version v1beta."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.osconfig.v1beta import osconfig_v1beta_messages as messages


class OsconfigV1beta(base_api.BaseApiClient):
  """Generated client library for service osconfig version v1beta."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://osconfig.googleapis.com/'

  _PACKAGE = u'osconfig'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'OsconfigV1beta'
  _URL_VERSION = u'v1beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new osconfig handle."""
    url = url or self.BASE_URL
    super(OsconfigV1beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_guestPolicies = self.ProjectsGuestPoliciesService(self)
    self.projects_patchDeployments = self.ProjectsPatchDeploymentsService(self)
    self.projects_patchJobs_instanceDetails = self.ProjectsPatchJobsInstanceDetailsService(self)
    self.projects_patchJobs = self.ProjectsPatchJobsService(self)
    self.projects_zones_instances = self.ProjectsZonesInstancesService(self)
    self.projects_zones = self.ProjectsZonesService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsGuestPoliciesService(base_api.BaseApiService):
    """Service class for the projects_guestPolicies resource."""

    _NAME = u'projects_guestPolicies'

    def __init__(self, client):
      super(OsconfigV1beta.ProjectsGuestPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS Config guest policy.

      Args:
        request: (OsconfigProjectsGuestPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/guestPolicies',
        http_method=u'POST',
        method_id=u'osconfig.projects.guestPolicies.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'guestPolicyId'],
        relative_path=u'v1beta/{+parent}/guestPolicies',
        request_field=u'guestPolicy',
        request_type_name=u'OsconfigProjectsGuestPoliciesCreateRequest',
        response_type_name=u'GuestPolicy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an OS Config guest policy.

      Args:
        request: (OsconfigProjectsGuestPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/guestPolicies/{guestPoliciesId}',
        http_method=u'DELETE',
        method_id=u'osconfig.projects.guestPolicies.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta/{+name}',
        request_field='',
        request_type_name=u'OsconfigProjectsGuestPoliciesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an OS Config guest policy.

      Args:
        request: (OsconfigProjectsGuestPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/guestPolicies/{guestPoliciesId}',
        http_method=u'GET',
        method_id=u'osconfig.projects.guestPolicies.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta/{+name}',
        request_field='',
        request_type_name=u'OsconfigProjectsGuestPoliciesGetRequest',
        response_type_name=u'GuestPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of OS Config guest policies.

      Args:
        request: (OsconfigProjectsGuestPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGuestPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/guestPolicies',
        http_method=u'GET',
        method_id=u'osconfig.projects.guestPolicies.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta/{+parent}/guestPolicies',
        request_field='',
        request_type_name=u'OsconfigProjectsGuestPoliciesListRequest',
        response_type_name=u'ListGuestPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an OS Config guest policy.

      Args:
        request: (OsconfigProjectsGuestPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/guestPolicies/{guestPoliciesId}',
        http_method=u'PATCH',
        method_id=u'osconfig.projects.guestPolicies.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1beta/{+name}',
        request_field=u'guestPolicy',
        request_type_name=u'OsconfigProjectsGuestPoliciesPatchRequest',
        response_type_name=u'GuestPolicy',
        supports_download=False,
    )

  class ProjectsPatchDeploymentsService(base_api.BaseApiService):
    """Service class for the projects_patchDeployments resource."""

    _NAME = u'projects_patchDeployments'

    def __init__(self, client):
      super(OsconfigV1beta.ProjectsPatchDeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS Config patch deployment.

      Args:
        request: (OsconfigProjectsPatchDeploymentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchDeployment) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchDeployments',
        http_method=u'POST',
        method_id=u'osconfig.projects.patchDeployments.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'patchDeploymentId'],
        relative_path=u'v1beta/{+parent}/patchDeployments',
        request_field=u'patchDeployment',
        request_type_name=u'OsconfigProjectsPatchDeploymentsCreateRequest',
        response_type_name=u'PatchDeployment',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an OS Config patch deployment.

      Args:
        request: (OsconfigProjectsPatchDeploymentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchDeployments/{patchDeploymentsId}',
        http_method=u'DELETE',
        method_id=u'osconfig.projects.patchDeployments.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta/{+name}',
        request_field='',
        request_type_name=u'OsconfigProjectsPatchDeploymentsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an OS Config patch deployment.

      Args:
        request: (OsconfigProjectsPatchDeploymentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchDeployment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchDeployments/{patchDeploymentsId}',
        http_method=u'GET',
        method_id=u'osconfig.projects.patchDeployments.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta/{+name}',
        request_field='',
        request_type_name=u'OsconfigProjectsPatchDeploymentsGetRequest',
        response_type_name=u'PatchDeployment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of OS Config patch deployments.

      Args:
        request: (OsconfigProjectsPatchDeploymentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPatchDeploymentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchDeployments',
        http_method=u'GET',
        method_id=u'osconfig.projects.patchDeployments.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta/{+parent}/patchDeployments',
        request_field='',
        request_type_name=u'OsconfigProjectsPatchDeploymentsListRequest',
        response_type_name=u'ListPatchDeploymentsResponse',
        supports_download=False,
    )

  class ProjectsPatchJobsInstanceDetailsService(base_api.BaseApiService):
    """Service class for the projects_patchJobs_instanceDetails resource."""

    _NAME = u'projects_patchJobs_instanceDetails'

    def __init__(self, client):
      super(OsconfigV1beta.ProjectsPatchJobsInstanceDetailsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Get a list of instance details for a given patch job.

      Args:
        request: (OsconfigProjectsPatchJobsInstanceDetailsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPatchJobInstanceDetailsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchJobs/{patchJobsId}/instanceDetails',
        http_method=u'GET',
        method_id=u'osconfig.projects.patchJobs.instanceDetails.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta/{+parent}/instanceDetails',
        request_field='',
        request_type_name=u'OsconfigProjectsPatchJobsInstanceDetailsListRequest',
        response_type_name=u'ListPatchJobInstanceDetailsResponse',
        supports_download=False,
    )

  class ProjectsPatchJobsService(base_api.BaseApiService):
    """Service class for the projects_patchJobs resource."""

    _NAME = u'projects_patchJobs'

    def __init__(self, client):
      super(OsconfigV1beta.ProjectsPatchJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Cancel a patch job. The patch job must be active. Canceled patch jobs.
cannot be restarted.

      Args:
        request: (OsconfigProjectsPatchJobsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchJob) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchJobs/{patchJobsId}:cancel',
        http_method=u'POST',
        method_id=u'osconfig.projects.patchJobs.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta/{+name}:cancel',
        request_field=u'cancelPatchJobRequest',
        request_type_name=u'OsconfigProjectsPatchJobsCancelRequest',
        response_type_name=u'PatchJob',
        supports_download=False,
    )

    def Execute(self, request, global_params=None):
      r"""Patch VM instances by creating and running a patch job.

      Args:
        request: (OsconfigProjectsPatchJobsExecuteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchJob) The response message.
      """
      config = self.GetMethodConfig('Execute')
      return self._RunMethod(
          config, request, global_params=global_params)

    Execute.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchJobs:execute',
        http_method=u'POST',
        method_id=u'osconfig.projects.patchJobs.execute',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta/{+parent}/patchJobs:execute',
        request_field=u'executePatchJobRequest',
        request_type_name=u'OsconfigProjectsPatchJobsExecuteRequest',
        response_type_name=u'PatchJob',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get the patch job. This can be used to track the progress of an.
ongoing patch job or review the details of completed jobs.

      Args:
        request: (OsconfigProjectsPatchJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchJob) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchJobs/{patchJobsId}',
        http_method=u'GET',
        method_id=u'osconfig.projects.patchJobs.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta/{+name}',
        request_field='',
        request_type_name=u'OsconfigProjectsPatchJobsGetRequest',
        response_type_name=u'PatchJob',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a list of patch jobs.

      Args:
        request: (OsconfigProjectsPatchJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPatchJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/patchJobs',
        http_method=u'GET',
        method_id=u'osconfig.projects.patchJobs.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta/{+parent}/patchJobs',
        request_field='',
        request_type_name=u'OsconfigProjectsPatchJobsListRequest',
        response_type_name=u'ListPatchJobsResponse',
        supports_download=False,
    )

  class ProjectsZonesInstancesService(base_api.BaseApiService):
    """Service class for the projects_zones_instances resource."""

    _NAME = u'projects_zones_instances'

    def __init__(self, client):
      super(OsconfigV1beta.ProjectsZonesInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def LookupEffectiveGuestPolicy(self, request, global_params=None):
      r"""Lookup the effective guest policy that applies to a VM instance. This.
lookup merges all policies that are assigned to the instance ancestry.

      Args:
        request: (OsconfigProjectsZonesInstancesLookupEffectiveGuestPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (EffectiveGuestPolicy) The response message.
      """
      config = self.GetMethodConfig('LookupEffectiveGuestPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    LookupEffectiveGuestPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta/projects/{projectsId}/zones/{zonesId}/instances/{instancesId}:lookupEffectiveGuestPolicy',
        http_method=u'POST',
        method_id=u'osconfig.projects.zones.instances.lookupEffectiveGuestPolicy',
        ordered_params=[u'instance'],
        path_params=[u'instance'],
        query_params=[],
        relative_path=u'v1beta/{+instance}:lookupEffectiveGuestPolicy',
        request_field=u'lookupEffectiveGuestPolicyRequest',
        request_type_name=u'OsconfigProjectsZonesInstancesLookupEffectiveGuestPolicyRequest',
        response_type_name=u'EffectiveGuestPolicy',
        supports_download=False,
    )

  class ProjectsZonesService(base_api.BaseApiService):
    """Service class for the projects_zones resource."""

    _NAME = u'projects_zones'

    def __init__(self, client):
      super(OsconfigV1beta.ProjectsZonesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(OsconfigV1beta.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
