# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport


import os
from pprint import pformat
from ProkkaAnnotation.Util.ProkkaUtils import ProkkaUtils
from Workspace.WorkspaceClient import Workspace as workspaceService


#END_HEADER


class ProkkaAnnotationMetaGenome:
    '''
    Module Name:
    ProkkaAnnotationMetaGenome

    Module Description:
    A KBase module: ProkkaAnnotationMetaGenome
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        self.ws_client = workspaceService(config["workspace-url"])
        #END_CONSTRUCTOR
        pass


    def run_ProkkaAnnotationMetaGenome(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_ProkkaAnnotationMetaGenome
        print("Input parameters: " + pformat(params))
        object_ref = params['object_ref']
        object_info = self.ws_client.get_object_info_new({"objects": [{"ref": object_ref}],
                                                          "includeMetadata": 1})[0]
        object_type = object_info[2]

        self.config['ctx'] = ctx
        prokka_runner = ProkkaUtils(self.config)

        if "KBaseGenomeAnnotations.Assembly" in object_type:
            return [prokka_runner.annotate_assembly(params, object_info)]
        elif "KBaseGenomes.Genome" in object_type:
            return [prokka_runner.annotate_genome(params)]
        else:
            raise Exception("Unsupported type" + object_type)
        #END run_ProkkaAnnotationMetaGenome

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_ProkkaAnnotationMetaGenome return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
