"""
    Engines API

    Allow clients to fetch Analytics through API.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
    Contact: api@factset.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fds.analyticsapi.engines.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from fds.analyticsapi.engines.model.pa_calculation_column import PACalculationColumn
    from fds.analyticsapi.engines.model.pa_calculation_data_sources import PACalculationDataSources
    from fds.analyticsapi.engines.model.pa_calculation_group import PACalculationGroup
    from fds.analyticsapi.engines.model.pa_date_parameters import PADateParameters
    from fds.analyticsapi.engines.model.pa_identifier import PAIdentifier
    from fds.analyticsapi.engines.model.template_content_types import TemplateContentTypes
    globals()['PACalculationColumn'] = PACalculationColumn
    globals()['PACalculationDataSources'] = PACalculationDataSources
    globals()['PACalculationGroup'] = PACalculationGroup
    globals()['PADateParameters'] = PADateParameters
    globals()['PAIdentifier'] = PAIdentifier
    globals()['TemplateContentTypes'] = TemplateContentTypes


class UnlinkedPATemplateParameters(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'directory': (str,),  # noqa: E501
            'template_type_id': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'accounts': ([PAIdentifier],),  # noqa: E501
            'benchmarks': ([PAIdentifier],),  # noqa: E501
            'columns': ([PACalculationColumn],),  # noqa: E501
            'dates': (PADateParameters,),  # noqa: E501
            'groups': ([PACalculationGroup],),  # noqa: E501
            'datasources': (PACalculationDataSources,),  # noqa: E501
            'currencyisocode': (str,),  # noqa: E501
            'componentdetail': (str,),  # noqa: E501
            'content': (TemplateContentTypes,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'directory': 'directory',  # noqa: E501
        'template_type_id': 'templateTypeId',  # noqa: E501
        'description': 'description',  # noqa: E501
        'accounts': 'accounts',  # noqa: E501
        'benchmarks': 'benchmarks',  # noqa: E501
        'columns': 'columns',  # noqa: E501
        'dates': 'dates',  # noqa: E501
        'groups': 'groups',  # noqa: E501
        'datasources': 'datasources',  # noqa: E501
        'currencyisocode': 'currencyisocode',  # noqa: E501
        'componentdetail': 'componentdetail',  # noqa: E501
        'content': 'content',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, directory, template_type_id, *args, **kwargs):  # noqa: E501
        """UnlinkedPATemplateParameters - a model defined in OpenAPI

        Args:
            directory (str): The directory to create an unlinked PA template
            template_type_id (str): Template type id

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str): Template description. [optional]  # noqa: E501
            accounts ([PAIdentifier]): List of accounts. [optional]  # noqa: E501
            benchmarks ([PAIdentifier]): List of benchmarks. [optional]  # noqa: E501
            columns ([PACalculationColumn]): List of columns for the PA calculation. [optional]  # noqa: E501
            dates (PADateParameters): [optional]  # noqa: E501
            groups ([PACalculationGroup]): List of groupings for the PA calculation. [optional]  # noqa: E501
            datasources (PACalculationDataSources): [optional]  # noqa: E501
            currencyisocode (str): Currency ISO code for calculation.. [optional]  # noqa: E501
            componentdetail (str): PA storage type. It can be GROUPS or GROUPSALL or TOTALS or SECURITIES.. [optional]  # noqa: E501
            content (TemplateContentTypes): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.directory = directory
        self.template_type_id = template_type_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
