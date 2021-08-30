import unittest

from fds.analyticsapi.engines.api.unlinked_pa_templates_api import UnlinkedPATemplatesApi
from fds.analyticsapi.engines.model.unlinked_pa_template_parameters_root import UnlinkedPATemplateParametersRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_parameters import UnlinkedPATemplateParameters
from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
from fds.analyticsapi.engines.model.pa_calculation_column import PACalculationColumn
from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
from fds.analyticsapi.engines.model.pa_calculation_group import PACalculationGroup
from fds.analyticsapi.engines.model.template_content_types import TemplateContentTypes
from fds.analyticsapi.engines.model.unlinked_pa_template_summary import UnlinkedPATemplateSummary
from fds.analyticsapi.engines.model.unlinked_pa_template_update_parameters import UnlinkedPATemplateUpdateParameters
from fds.analyticsapi.engines.model.unlinked_pa_template_update_parameters_root import UnlinkedPATemplateUpdateParametersRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_root import UnlinkedPATemplateRoot
from fds.analyticsapi.engines.model.unlinked_pa_template import UnlinkedPATemplate
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type import UnlinkedPATemplateCategoryAndType
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type_root import UnlinkedPATemplateCategoryAndTypeRoot
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type_details import UnlinkedPATemplateCategoryAndTypeDetails
from fds.analyticsapi.engines.model.unlinked_pa_template_category_and_type_details_root import UnlinkedPATemplateCategoryAndTypeDetailsRoot

from common_functions import CommonFunctions

class TestUnlinkedPaTemplatesApi(unittest.TestCase):

    def setUp(self):
        self.unlinked_pa_templates_api = UnlinkedPATemplatesApi(CommonFunctions.build_api_client())

    def test_a_create_unlinked_pa_template(self):
        unlinked_pa_template_parameters = UnlinkedPATemplateParameters(
            directory="Personal:UnlinkedPATemplates/",
            template_type_id="996E90B981AEE83F14029ED3D309FB3F03EC6E2ACC7FD42C22CBD5D279502CFD",
            description="This is an unlinked PA template that only returns security level data",
            accounts = [
                PAIdentifier(
                    id = "SPN:SP50",
                    holdingsmode = "B&H"),
                PAIdentifier(
                    id = "MSCI_USA:984000",
                    holdingsmode = "B&H")],
            benchmarks = [
                PAIdentifier(
                    id = "SPN:SP50",
                    holdingsmode = "B&H"),
                PAIdentifier(
                    id = "DJGX:AMERICAS",
                    holdingsmode = "B&H")],
            columns = [
                PACalculationColumn(
                    id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                    statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
            dates = PADateParameters(
                startdate = "20200101",
                enddate = "20201215",
                frequency = "Monthly"),
            groups = [
                PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
            currencyisocode = "USD",
            componentdetail = "GROUPS",
            content = TemplateContentTypes(
                mandatory = ["accounts", "benchmarks"],
                optional = ["groups", "columns", "currencyisocode", "componentdetail"],
                locked = ["dates"])
        )

        unlinked_pa_template_parameters_root = UnlinkedPATemplateParametersRoot(
            data = unlinked_pa_template_parameters
        )

        response = self.unlinked_pa_templates_api.create_unlinked_pa_templates(
            unlinked_pa_template_parameters_root = unlinked_pa_template_parameters_root)

        firsttemplate = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 201, "Response should be 201 - Success")
        self.assertEqual(type(response[0].data), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0].data[firsttemplate]),
            UnlinkedPATemplateSummary, "Response should be of UnlinkedPATemplateSummary type.")
        self.assertGreater(len(response[0].data), 0, "Response result should not be an empty list.")

    def test_b_get_all_unlinked_pa_templates_by_directory(self):
        response = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            directory = "Personal:UnlinkedPATemplates/"
        )

        firsttemplate = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0].data[firsttemplate]),
            UnlinkedPATemplateSummary, "Response should be of UnlinkedPATemplateSummary type.")
        self.assertGreater(len(response[0].data), 0, "Response result should not be an empty list.")

    def test_c_get_all_unlinked_pa_templates_by_category(self):
        response = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            category = "Weights"
        )

        firsttemplate = list(response[0].data.keys())[0]
        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0].data[firsttemplate]),
            UnlinkedPATemplateSummary, "Response should be of UnlinkedPATemplateSummary type.")
        self.assertGreater(len(response[0].data), 0, "Response result should not be an empty list.")

    def test_d_update_unlinked_pa_template(self):
        templates = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            directory = "Personal:UnlinkedPATemplates/"
        )
        template_id = list(templates[0].data.keys())[0]

        unlinked_pa_template_update_parameters = UnlinkedPATemplateUpdateParameters(
            description="This is an updated unlinked PA template that only returns security level data",
            accounts = [
                PAIdentifier(
                    id = "SPN:SP50",
                    holdingsmode = "B&H"),
                PAIdentifier(
                    id = "MSCI_USA:984000",
                    holdingsmode = "B&H")],
            benchmarks = [
                PAIdentifier(
                    id = "SPN:SP50",
                    holdingsmode = "B&H"),
                PAIdentifier(
                    id = "DJGX:AMERICAS",
                    holdingsmode = "B&H")],
            columns = [
                PACalculationColumn(
                    id = "BD1720474AB8A80BDD79777F5B9CA594F4151C0554E30F9C916BA73BFAFC1FE0",
                    statistics = ["eb9d6d91416e4224bacadc261787e56f"])],
            dates = PADateParameters(
                startdate = "20200101",
                enddate = "20201215",
                frequency = "Monthly"),
            groups = [
                PACalculationGroup(id = "5BCFFD17598FAEBD88EB4934EFB5FEF53849867D607ECEF232CD42D3369BBBCA")],
            currencyisocode = "USD",
            componentdetail = "GROUPS",
            content = TemplateContentTypes(
                mandatory = ["accounts", "benchmarks"],
                optional = ["columns", "groups", "currencyisocode", "componentdetail"],
                locked = ["dates"])
        )

        unlinked_pa_template_update_parameters_root = UnlinkedPATemplateUpdateParametersRoot(
            data = unlinked_pa_template_update_parameters
        )
        response = self.unlinked_pa_templates_api.update_unlinked_pa_templates(
            id = template_id, unlinked_pa_template_update_parameters_root=unlinked_pa_template_update_parameters_root
        )

        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0].data), dict, "Response should be of Dictionary type.")
        self.assertEqual(type(response[0].data[template_id]),
            UnlinkedPATemplateSummary, "Response should be of UnlinkedPATemplateSummary type.")
        self.assertGreater(len(response[0].data), 0, "Response result should not be an empty list.")

    def test_e_get_unlinked_pa_template_by_id(self):
        templates = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            directory = "Personal:UnlinkedPATemplates/"
        )
        template_id = list(templates[0].data.keys())[0]

        response = self.unlinked_pa_templates_api.get_unlinked_pa_templates_by_id(
            id = template_id
        )

        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]), UnlinkedPATemplateRoot, "Response should be of UnlinkedPATemplateRoot type.")
        self.assertEqual(type(response[0].data),
            UnlinkedPATemplate, "Response should be of UnlinkedPATemplate type.")

    def test_f_get_default_unlinked_pa_template_types(self):
        response = self.unlinked_pa_templates_api.get_default_unlinked_pa_template_types()
        firsttemplatetype = list(response[0].data.keys())[0]

        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]),
            UnlinkedPATemplateCategoryAndTypeRoot, "Response should be of UnlinkedPATemplateCategoryAndTypeRoot type.")
        self.assertEqual(type(response[0].data[firsttemplatetype]),
            UnlinkedPATemplateCategoryAndType, "Response should be of UnlinkedPATemplateCategoryAndType type.")

    def test_g_get_unlinked_pa_type_details_by_id(self):
        templatetypes = self.unlinked_pa_templates_api.get_default_unlinked_pa_template_types()
        template_type_id = list(templatetypes[0].data.keys())[0]

        response = self.unlinked_pa_templates_api.get_details_type(template_type_id)

        self.assertEqual(response[1], 200, "Response should be 200 - Success")
        self.assertEqual(type(response[0]),
            UnlinkedPATemplateCategoryAndTypeDetailsRoot, "Response should be of UnlinkedPATemplateCategoryAndTypeDetailsRoot type.")
        self.assertEqual(type(response[0].data),
            UnlinkedPATemplateCategoryAndTypeDetails, "Response should be of UnlinkedPATemplateCategoryAndTypeDetails type.")
   
    def test_h_delete_unlinked_pa_template(self):
        templates = self.unlinked_pa_templates_api.get_unlinked_pa_templates(
            directory = "Personal:UnlinkedPATemplates/"
        )
        template_id = list(templates[0].data.keys())[0]

        response = self.unlinked_pa_templates_api.delete_unlinked_pa_templates(
            id = template_id
        )

        self.assertEqual(response[1], 204, "Response should be 204 - Success")

if __name__ == '__main__':
    unittest.main()
