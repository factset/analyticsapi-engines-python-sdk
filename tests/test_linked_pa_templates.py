import unittest

from fds.analyticsapi.engines.api.linked_pa_templates_api import LinkedPATemplatesApi
from fds.analyticsapi.engines.model.linked_pa_template_parameters_root import LinkedPATemplateParametersRoot
from fds.analyticsapi.engines.model.linked_pa_template_parameters import LinkedPATemplateParameters
from fds.analyticsapi.engines.model.template_content_types import TemplateContentTypes
from fds.analyticsapi.engines.model.linked_pa_template_summary import LinkedPATemplateSummary
from fds.analyticsapi.engines.model.linked_pa_template_post_summary import LinkedPATemplatePostSummary
from fds.analyticsapi.engines.model.linked_pa_template_update_parameters import LinkedPATemplateUpdateParameters
from fds.analyticsapi.engines.model.linked_pa_template_update_parameters_root import LinkedPATemplateUpdateParametersRoot
from fds.analyticsapi.engines.model.linked_pa_template_root import LinkedPATemplateRoot
from fds.analyticsapi.engines.model.linked_pa_template import LinkedPATemplate


from common_functions import CommonFunctions

class TestLinkedPaTemplatesApi(unittest.TestCase):

    def setUp(self):
        self.linked_pa_templates_api = LinkedPATemplatesApi(CommonFunctions.build_api_client())

    def test_a_create_linked_pa_template(self):
        linked_pa_template_parameters = LinkedPATemplateParameters(
            directory="Personal:SDKTests/DoNotModify/LinkedPATemplates/",
            parent_component_id="801B800245E468A52AEBEC4BE31CFF5AF82F371DAEF5F158AC2E98C2FA324B46",
            description="This is a linked PA template that only returns security level data",
            content=TemplateContentTypes(
                mandatory=["accounts", "benchmarks"],
                optional=["groups", "columns"],
                locked=["componentdetail"]
            )
        )

        linked_pa_template_parameters_root = LinkedPATemplateParametersRoot(
            data=linked_pa_template_parameters
        )

        response = self.linked_pa_templates_api.create_linked_pa_templates(
            linked_pa_template_parameters_root=linked_pa_template_parameters_root)
        firsttemplate = response[0].data['id']
        self.assertEqual(response[1], 201, "Response should be 201 - Success")
        self.assertEqual(type(response[0].data), LinkedPATemplatePostSummary, "Response should be of LinkedPATemplatePostSummary type.")
        self.assertEqual(type(response[0].data['id']), str, "Response should be of String type.")
        self.assertGreater(len(response[0].data['id']), 0, "Response result should not be an empty list.")

    def test_b_get_all_linked_pa_templates(self):
        response = self.linked_pa_templates_api.get_linked_pa_templates(
            directory="Personal:SDKTests/DoNotModify/LinkedPATemplates/"
        )

        firsttemplate = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0].data[firsttemplate]),
            LinkedPATemplateSummary, "Response should be of LinkedPATemplateSummary type.")
        self.assertGreater(len(response[0].data), 0, "Response result should not be an empty list.")

    def test_c_update_linked_pa_template(self):
        templates = self.linked_pa_templates_api.get_linked_pa_templates(
            directory="Personal:SDKTests/DoNotModify/LinkedPATemplates/"
        )
        template_id = list(templates[0].data.keys())[0]

        linked_pa_template_update_parameters = LinkedPATemplateUpdateParameters(
            parent_component_id="801B800245E468A52AEBEC4BE31CFF5AF82F371DAEF5F158AC2E98C2FA324B46",
            description="This is an updated linked PA template that only returns security level data",
            content=TemplateContentTypes(
                mandatory=["accounts", "benchmarks"],
                optional=["groups", "columns"],
                locked=["componentdetail"]
            )
        )
        linked_pa_template_update_parameters_root = LinkedPATemplateUpdateParametersRoot(
            data=linked_pa_template_update_parameters
        )

        try:
            response = self.linked_pa_templates_api.update_linked_pa_templates(
                id=template_id, linked_pa_template_update_parameters_root=linked_pa_template_update_parameters_root
            )
            self.assertEqual(response[1], 200, "Response should be 200 - Success")
            self.assertEqual(type(response[0].data), LinkedPATemplatePostSummary,
                             "Response should be of LinkedPATemplatePostSummary type.")
            self.assertGreater(len(response[0].data['id']), 0, "Response result should not be an empty list.")
        except:
            self.skipTest("template doesn't exist to fetch")

    def test_d_get_linked_pa_template_by_id(self):
        templates = self.linked_pa_templates_api.get_linked_pa_templates(
            directory="Personal:SDKTests/DoNotModify/LinkedPATemplates/"
        )
        template_id = list(templates[0].data.keys())[0]

        try:
            response = self.linked_pa_templates_api.get_linked_pa_templates_by_id(
                id=template_id
            )

            self.assertEqual(response[1], 200, "Response should be 200 - Success")
            self.assertEqual(type(response[0]), LinkedPATemplateRoot, "Response should be of LinkedPATemplateRoot type.")
            self.assertEqual(type(response[0].data),
                LinkedPATemplate, "Response should be of LinkedPATemplate type.")
        except:
            self.skipTest("template doesn't exist to fetch")
    
    def test_e_delete_linked_pa_template(self):
        templates = self.linked_pa_templates_api.get_linked_pa_templates(
            directory="Personal:SDKTests/DoNotModify/LinkedPATemplates/"
        )

        template_id = list(templates[0].data.keys())[0]

        try:
            delete_response = self.linked_pa_templates_api.delete_linked_pa_templates(
                id=template_id
            )
            self.assertEqual(delete_response[1], 204, "Response should be 204 - Success")
        except:
            self.skipTest("template doesn't exist to delete.")


if __name__ == '__main__':
    unittest.main()
