# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class StrategyRegistration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, title=None, strategy_id=None, instruments_mapping=None, instance_id=None, parameters=None):
        """
        StrategyRegistration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'title': 'str',
            'strategy_id': 'str',
            'instruments_mapping': 'list[InstrumentMapping]',
            'instance_id': 'str',
            'parameters': 'dict(str, str)'
        }

        self.attribute_map = {
            'title': 'title',
            'strategy_id': 'strategyId',
            'instruments_mapping': 'instrumentsMapping',
            'instance_id': 'instanceId',
            'parameters': 'parameters'
        }

        self._title = title
        self._strategy_id = strategy_id
        self._instruments_mapping = instruments_mapping
        self._instance_id = instance_id
        self._parameters = parameters


    @property
    def title(self):
        """
        Gets the title of this StrategyRegistration.


        :return: The title of this StrategyRegistration.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this StrategyRegistration.


        :param title: The title of this StrategyRegistration.
        :type: str
        """

        self._title = title

    @property
    def strategy_id(self):
        """
        Gets the strategy_id of this StrategyRegistration.


        :return: The strategy_id of this StrategyRegistration.
        :rtype: str
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        """
        Sets the strategy_id of this StrategyRegistration.


        :param strategy_id: The strategy_id of this StrategyRegistration.
        :type: str
        """

        self._strategy_id = strategy_id

    @property
    def instruments_mapping(self):
        """
        Gets the instruments_mapping of this StrategyRegistration.


        :return: The instruments_mapping of this StrategyRegistration.
        :rtype: list[InstrumentMapping]
        """
        return self._instruments_mapping

    @instruments_mapping.setter
    def instruments_mapping(self, instruments_mapping):
        """
        Sets the instruments_mapping of this StrategyRegistration.


        :param instruments_mapping: The instruments_mapping of this StrategyRegistration.
        :type: list[InstrumentMapping]
        """

        self._instruments_mapping = instruments_mapping

    @property
    def instance_id(self):
        """
        Gets the instance_id of this StrategyRegistration.


        :return: The instance_id of this StrategyRegistration.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this StrategyRegistration.


        :param instance_id: The instance_id of this StrategyRegistration.
        :type: str
        """

        self._instance_id = instance_id

    @property
    def parameters(self):
        """
        Gets the parameters of this StrategyRegistration.


        :return: The parameters of this StrategyRegistration.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this StrategyRegistration.


        :param parameters: The parameters of this StrategyRegistration.
        :type: dict(str, str)
        """

        self._parameters = parameters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
