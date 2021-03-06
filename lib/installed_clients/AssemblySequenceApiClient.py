# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class AssemblySequenceAPI(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def get_dna_sequences(self, params, context=None):
        """
        :param params: instance of type "GetDNASequencesParams" -> structure:
           parameter "assembly_ref" of type "Assembly_ref" (Reference to an
           Assembly object in the workspace @id ws
           KBaseGenomeAnnotations.Assembly), parameter "contigset_ref" of
           type "ContigSet_ref" (Reference to a ContigSet object containing
           the contigs for this genome in the workspace @id ws
           KBaseGenomes.ContigSet), parameter "requested_features" of mapping
           from String to type "Location" -> list of tuple of size 4:
           parameter "contig_id" of String, parameter "start" of Long,
           parameter "strand" of String, parameter "length" of Long
        :returns: instance of type "GetDNASequencesOutput" -> structure:
           parameter "dna_sequences" of mapping from String to String
        """
        return self._client.run_job('AssemblySequenceAPI.get_dna_sequences',
                                    [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.run_job('AssemblySequenceAPI.status',
                                    [], self._service_ver, context)
