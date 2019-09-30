import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_cloudwatch
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-stepfunctions", "1.7.0", __name__, "aws-stepfunctions@1.7.0.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.ActivityProps", jsii_struct_bases=[], name_mapping={'activity_name': 'activityName'})
class ActivityProps():
    def __init__(self, *, activity_name: typing.Optional[str]=None):
        """
        :param activity_name: The name for this activity. Default: If not supplied, a name is generated

        stability
        :stability: experimental
        """
        self._values = {
        }
        if activity_name is not None: self._values["activity_name"] = activity_name

    @property
    def activity_name(self) -> typing.Optional[str]:
        """The name for this activity.

        default
        :default: If not supplied, a name is generated

        stability
        :stability: experimental
        """
        return self._values.get('activity_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ActivityProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.AfterwardsOptions", jsii_struct_bases=[], name_mapping={'include_error_handlers': 'includeErrorHandlers', 'include_otherwise': 'includeOtherwise'})
class AfterwardsOptions():
    def __init__(self, *, include_error_handlers: typing.Optional[bool]=None, include_otherwise: typing.Optional[bool]=None):
        """Options for selecting the choice paths.

        :param include_error_handlers: Whether to include error handling states. If this is true, all states which are error handlers (added through 'onError') and states reachable via error handlers will be included as well. Default: false
        :param include_otherwise: Whether to include the default/otherwise transition for the current Choice state. If this is true and the current Choice does not have a default outgoing transition, one will be added included when .next() is called on the chain. Default: false

        stability
        :stability: experimental
        """
        self._values = {
        }
        if include_error_handlers is not None: self._values["include_error_handlers"] = include_error_handlers
        if include_otherwise is not None: self._values["include_otherwise"] = include_otherwise

    @property
    def include_error_handlers(self) -> typing.Optional[bool]:
        """Whether to include error handling states.

        If this is true, all states which are error handlers (added through 'onError')
        and states reachable via error handlers will be included as well.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('include_error_handlers')

    @property
    def include_otherwise(self) -> typing.Optional[bool]:
        """Whether to include the default/otherwise transition for the current Choice state.

        If this is true and the current Choice does not have a default outgoing
        transition, one will be added included when .next() is called on the chain.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('include_otherwise')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AfterwardsOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.CatchProps", jsii_struct_bases=[], name_mapping={'errors': 'errors', 'result_path': 'resultPath'})
class CatchProps():
    def __init__(self, *, errors: typing.Optional[typing.List[str]]=None, result_path: typing.Optional[str]=None):
        """Error handler details.

        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value DISCARD, which will cause the error data to be discarded. Default: $

        stability
        :stability: experimental
        """
        self._values = {
        }
        if errors is not None: self._values["errors"] = errors
        if result_path is not None: self._values["result_path"] = result_path

    @property
    def errors(self) -> typing.Optional[typing.List[str]]:
        """Errors to recover from by going to the given state.

        A list of error strings to retry, which can be either predefined errors
        (for example Errors.NoChoiceMatched) or a self-defined error.

        default
        :default: All errors

        stability
        :stability: experimental
        """
        return self._values.get('errors')

    @property
    def result_path(self) -> typing.Optional[str]:
        """JSONPath expression to indicate where to inject the error data.

        May also be the special value DISCARD, which will cause the error
        data to be discarded.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('result_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CatchProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnActivity(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.CfnActivity"):
    """A CloudFormation ``AWS::StepFunctions::Activity``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html
    cloudformationResource:
    :cloudformationResource:: AWS::StepFunctions::Activity
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, tags: typing.Optional[typing.List["TagsEntryProperty"]]=None) -> None:
        """Create a new ``AWS::StepFunctions::Activity``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param name: ``AWS::StepFunctions::Activity.Name``.
        :param tags: ``AWS::StepFunctions::Activity.Tags``.
        """
        props = CfnActivityProps(name=name, tags=tags)

        jsii.create(CfnActivity, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::StepFunctions::Activity.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::StepFunctions::Activity.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.CfnActivity.TagsEntryProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class TagsEntryProperty():
        def __init__(self, *, key: str, value: str):
            """
            :param key: ``CfnActivity.TagsEntryProperty.Key``.
            :param value: ``CfnActivity.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @property
        def key(self) -> str:
            """``CfnActivity.TagsEntryProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-key
            """
            return self._values.get('key')

        @property
        def value(self) -> str:
            """``CfnActivity.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagsEntryProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.CfnActivityProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'tags': 'tags'})
class CfnActivityProps():
    def __init__(self, *, name: str, tags: typing.Optional[typing.List["CfnActivity.TagsEntryProperty"]]=None):
        """Properties for defining a ``AWS::StepFunctions::Activity``.

        :param name: ``AWS::StepFunctions::Activity.Name``.
        :param tags: ``AWS::StepFunctions::Activity.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html
        """
        self._values = {
            'name': name,
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def name(self) -> str:
        """``AWS::StepFunctions::Activity.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name
        """
        return self._values.get('name')

    @property
    def tags(self) -> typing.Optional[typing.List["CfnActivity.TagsEntryProperty"]]:
        """``AWS::StepFunctions::Activity.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnActivityProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnStateMachine(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.CfnStateMachine"):
    """A CloudFormation ``AWS::StepFunctions::StateMachine``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html
    cloudformationResource:
    :cloudformationResource:: AWS::StepFunctions::StateMachine
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, definition_string: str, role_arn: str, state_machine_name: typing.Optional[str]=None, tags: typing.Optional[typing.List["TagsEntryProperty"]]=None) -> None:
        """Create a new ``AWS::StepFunctions::StateMachine``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param definition_string: ``AWS::StepFunctions::StateMachine.DefinitionString``.
        :param role_arn: ``AWS::StepFunctions::StateMachine.RoleArn``.
        :param state_machine_name: ``AWS::StepFunctions::StateMachine.StateMachineName``.
        :param tags: ``AWS::StepFunctions::StateMachine.Tags``.
        """
        props = CfnStateMachineProps(definition_string=definition_string, role_arn=role_arn, state_machine_name=state_machine_name, tags=tags)

        jsii.create(CfnStateMachine, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::StepFunctions::StateMachine.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="definitionString")
    def definition_string(self) -> str:
        """``AWS::StepFunctions::StateMachine.DefinitionString``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
        """
        return jsii.get(self, "definitionString")

    @definition_string.setter
    def definition_string(self, value: str):
        return jsii.set(self, "definitionString", value)

    @property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> str:
        """``AWS::StepFunctions::StateMachine.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: str):
        return jsii.set(self, "roleArn", value)

    @property
    @jsii.member(jsii_name="stateMachineName")
    def state_machine_name(self) -> typing.Optional[str]:
        """``AWS::StepFunctions::StateMachine.StateMachineName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
        """
        return jsii.get(self, "stateMachineName")

    @state_machine_name.setter
    def state_machine_name(self, value: typing.Optional[str]):
        return jsii.set(self, "stateMachineName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.CfnStateMachine.TagsEntryProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class TagsEntryProperty():
        def __init__(self, *, key: str, value: str):
            """
            :param key: ``CfnStateMachine.TagsEntryProperty.Key``.
            :param value: ``CfnStateMachine.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @property
        def key(self) -> str:
            """``CfnStateMachine.TagsEntryProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-key
            """
            return self._values.get('key')

        @property
        def value(self) -> str:
            """``CfnStateMachine.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagsEntryProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.CfnStateMachineProps", jsii_struct_bases=[], name_mapping={'definition_string': 'definitionString', 'role_arn': 'roleArn', 'state_machine_name': 'stateMachineName', 'tags': 'tags'})
class CfnStateMachineProps():
    def __init__(self, *, definition_string: str, role_arn: str, state_machine_name: typing.Optional[str]=None, tags: typing.Optional[typing.List["CfnStateMachine.TagsEntryProperty"]]=None):
        """Properties for defining a ``AWS::StepFunctions::StateMachine``.

        :param definition_string: ``AWS::StepFunctions::StateMachine.DefinitionString``.
        :param role_arn: ``AWS::StepFunctions::StateMachine.RoleArn``.
        :param state_machine_name: ``AWS::StepFunctions::StateMachine.StateMachineName``.
        :param tags: ``AWS::StepFunctions::StateMachine.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html
        """
        self._values = {
            'definition_string': definition_string,
            'role_arn': role_arn,
        }
        if state_machine_name is not None: self._values["state_machine_name"] = state_machine_name
        if tags is not None: self._values["tags"] = tags

    @property
    def definition_string(self) -> str:
        """``AWS::StepFunctions::StateMachine.DefinitionString``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
        """
        return self._values.get('definition_string')

    @property
    def role_arn(self) -> str:
        """``AWS::StepFunctions::StateMachine.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
        """
        return self._values.get('role_arn')

    @property
    def state_machine_name(self) -> typing.Optional[str]:
        """``AWS::StepFunctions::StateMachine.StateMachineName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
        """
        return self._values.get('state_machine_name')

    @property
    def tags(self) -> typing.Optional[typing.List["CfnStateMachine.TagsEntryProperty"]]:
        """``AWS::StepFunctions::StateMachine.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnStateMachineProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.ChoiceProps", jsii_struct_bases=[], name_mapping={'comment': 'comment', 'input_path': 'inputPath', 'output_path': 'outputPath'})
class ChoiceProps():
    def __init__(self, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None):
        """Properties for defining a Choice state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $

        stability
        :stability: experimental
        """
        self._values = {
        }
        if comment is not None: self._values["comment"] = comment
        if input_path is not None: self._values["input_path"] = input_path
        if output_path is not None: self._values["output_path"] = output_path

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the input to this state.

        May also be the special value DISCARD, which will cause the effective
        input to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('input_path')

    @property
    def output_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the output to this state.

        May also be the special value DISCARD, which will cause the effective
        output to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('output_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ChoiceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Condition(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-stepfunctions.Condition"):
    """A Condition for use in a Choice state branch.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ConditionProxy

    def __init__(self) -> None:
        jsii.create(Condition, self, [])

    @jsii.member(jsii_name="and")
    @classmethod
    def and_(cls, *conditions: "Condition") -> "Condition":
        """Combine two or more conditions with a logical AND.

        :param conditions: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "and", [*conditions])

    @jsii.member(jsii_name="booleanEquals")
    @classmethod
    def boolean_equals(cls, variable: str, value: bool) -> "Condition":
        """Matches if a boolean field has the given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "booleanEquals", [variable, value])

    @jsii.member(jsii_name="not")
    @classmethod
    def not_(cls, condition: "Condition") -> "Condition":
        """Negate a condition.

        :param condition: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "not", [condition])

    @jsii.member(jsii_name="numberEquals")
    @classmethod
    def number_equals(cls, variable: str, value: jsii.Number) -> "Condition":
        """Matches if a numeric field has the given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "numberEquals", [variable, value])

    @jsii.member(jsii_name="numberGreaterThan")
    @classmethod
    def number_greater_than(cls, variable: str, value: jsii.Number) -> "Condition":
        """Matches if a numeric field is greater than the given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "numberGreaterThan", [variable, value])

    @jsii.member(jsii_name="numberGreaterThanEquals")
    @classmethod
    def number_greater_than_equals(cls, variable: str, value: jsii.Number) -> "Condition":
        """Matches if a numeric field is greater than or equal to the given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "numberGreaterThanEquals", [variable, value])

    @jsii.member(jsii_name="numberLessThan")
    @classmethod
    def number_less_than(cls, variable: str, value: jsii.Number) -> "Condition":
        """Matches if a numeric field is less than the given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "numberLessThan", [variable, value])

    @jsii.member(jsii_name="numberLessThanEquals")
    @classmethod
    def number_less_than_equals(cls, variable: str, value: jsii.Number) -> "Condition":
        """Matches if a numeric field is less than or equal to the given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "numberLessThanEquals", [variable, value])

    @jsii.member(jsii_name="or")
    @classmethod
    def or_(cls, *conditions: "Condition") -> "Condition":
        """Combine two or more conditions with a logical OR.

        :param conditions: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "or", [*conditions])

    @jsii.member(jsii_name="stringEquals")
    @classmethod
    def string_equals(cls, variable: str, value: str) -> "Condition":
        """Matches if a string field has the given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "stringEquals", [variable, value])

    @jsii.member(jsii_name="stringGreaterThan")
    @classmethod
    def string_greater_than(cls, variable: str, value: str) -> "Condition":
        """Matches if a string field sorts after a given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "stringGreaterThan", [variable, value])

    @jsii.member(jsii_name="stringGreaterThanEquals")
    @classmethod
    def string_greater_than_equals(cls, variable: str, value: str) -> "Condition":
        """Matches if a string field sorts after or equal to a given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "stringGreaterThanEquals", [variable, value])

    @jsii.member(jsii_name="stringLessThan")
    @classmethod
    def string_less_than(cls, variable: str, value: str) -> "Condition":
        """Matches if a string field sorts before a given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "stringLessThan", [variable, value])

    @jsii.member(jsii_name="stringLessThanEquals")
    @classmethod
    def string_less_than_equals(cls, variable: str, value: str) -> "Condition":
        """Matches if a string field sorts equal to or before a given value.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "stringLessThanEquals", [variable, value])

    @jsii.member(jsii_name="timestampEquals")
    @classmethod
    def timestamp_equals(cls, variable: str, value: str) -> "Condition":
        """Matches if a timestamp field is the same time as the given timestamp.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "timestampEquals", [variable, value])

    @jsii.member(jsii_name="timestampGreaterThan")
    @classmethod
    def timestamp_greater_than(cls, variable: str, value: str) -> "Condition":
        """Matches if a timestamp field is after the given timestamp.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "timestampGreaterThan", [variable, value])

    @jsii.member(jsii_name="timestampGreaterThanEquals")
    @classmethod
    def timestamp_greater_than_equals(cls, variable: str, value: str) -> "Condition":
        """Matches if a timestamp field is after or equal to the given timestamp.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "timestampGreaterThanEquals", [variable, value])

    @jsii.member(jsii_name="timestampLessThan")
    @classmethod
    def timestamp_less_than(cls, variable: str, value: str) -> "Condition":
        """Matches if a timestamp field is before the given timestamp.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "timestampLessThan", [variable, value])

    @jsii.member(jsii_name="timestampLessThanEquals")
    @classmethod
    def timestamp_less_than_equals(cls, variable: str, value: str) -> "Condition":
        """Matches if a timestamp field is before or equal to the given timestamp.

        :param variable: -
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "timestampLessThanEquals", [variable, value])

    @jsii.member(jsii_name="renderCondition")
    @abc.abstractmethod
    def render_condition(self) -> typing.Any:
        """Render Amazon States Language JSON for the condition.

        stability
        :stability: experimental
        """
        ...


class _ConditionProxy(Condition):
    @jsii.member(jsii_name="renderCondition")
    def render_condition(self) -> typing.Any:
        """Render Amazon States Language JSON for the condition.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderCondition", [])


class Context(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Context"):
    """Extract a field from the State Machine Context data.

    see
    :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#wait-token-contextobject
    stability
    :stability: experimental
    """
    @jsii.member(jsii_name="numberAt")
    @classmethod
    def number_at(cls, path: str) -> jsii.Number:
        """Instead of using a literal number, get the value from a JSON path.

        :param path: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "numberAt", [path])

    @jsii.member(jsii_name="stringAt")
    @classmethod
    def string_at(cls, path: str) -> str:
        """Instead of using a literal string, get the value from a JSON path.

        :param path: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "stringAt", [path])

    @classproperty
    @jsii.member(jsii_name="entireContext")
    def entire_context(cls) -> str:
        """Use the entire context data structure.

        Will be an object at invocation time, but is represented in the CDK
        application as a string.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "entireContext")

    @classproperty
    @jsii.member(jsii_name="taskToken")
    def task_token(cls) -> str:
        """Return the Task Token field.

        External actions will need this token to report step completion
        back to StepFunctions using the ``SendTaskSuccess`` or ``SendTaskFailure``
        calls.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "taskToken")


class Data(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Data"):
    """Extract a field from the State Machine data that gets passed around between states.

    stability
    :stability: experimental
    """
    @jsii.member(jsii_name="isJsonPathString")
    @classmethod
    def is_json_path_string(cls, value: str) -> bool:
        """
        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "isJsonPathString", [value])

    @jsii.member(jsii_name="listAt")
    @classmethod
    def list_at(cls, path: str) -> typing.List[str]:
        """Instead of using a literal string list, get the value from a JSON path.

        :param path: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "listAt", [path])

    @jsii.member(jsii_name="numberAt")
    @classmethod
    def number_at(cls, path: str) -> jsii.Number:
        """Instead of using a literal number, get the value from a JSON path.

        :param path: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "numberAt", [path])

    @jsii.member(jsii_name="stringAt")
    @classmethod
    def string_at(cls, path: str) -> str:
        """Instead of using a literal string, get the value from a JSON path.

        :param path: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "stringAt", [path])

    @classproperty
    @jsii.member(jsii_name="entirePayload")
    def entire_payload(cls) -> str:
        """Use the entire data structure.

        Will be an object at invocation time, but is represented in the CDK
        application as a string.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "entirePayload")


class Errors(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Errors"):
    """Predefined error strings.

    stability
    :stability: experimental
    """
    def __init__(self) -> None:
        jsii.create(Errors, self, [])

    @classproperty
    @jsii.member(jsii_name="ALL")
    def ALL(cls) -> str:
        """Matches any Error.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "ALL")

    @classproperty
    @jsii.member(jsii_name="BRANCH_FAILED")
    def BRANCH_FAILED(cls) -> str:
        """A branch of a Parallel state failed.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "BRANCH_FAILED")

    @classproperty
    @jsii.member(jsii_name="NO_CHOICE_MATCHED")
    def NO_CHOICE_MATCHED(cls) -> str:
        """A Choice state failed to find a match for the condition field extracted from its input.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "NO_CHOICE_MATCHED")

    @classproperty
    @jsii.member(jsii_name="PERMISSIONS")
    def PERMISSIONS(cls) -> str:
        """A Task State failed because it had insufficient privileges to execute the specified code.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "PERMISSIONS")

    @classproperty
    @jsii.member(jsii_name="RESULT_PATH_MATCH_FAILURE")
    def RESULT_PATH_MATCH_FAILURE(cls) -> str:
        """A Task State’s “ResultPath” field cannot be applied to the input the state received.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "RESULT_PATH_MATCH_FAILURE")

    @classproperty
    @jsii.member(jsii_name="TASKS_FAILED")
    def TASKS_FAILED(cls) -> str:
        """A Task State failed during the execution.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "TASKS_FAILED")

    @classproperty
    @jsii.member(jsii_name="TIMEOUT")
    def TIMEOUT(cls) -> str:
        """A Task State either ran longer than the “TimeoutSeconds” value, or failed to heartbeat for a time longer than the “HeartbeatSeconds” value.

        stability
        :stability: experimental
        """
        return jsii.sget(cls, "TIMEOUT")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.FailProps", jsii_struct_bases=[], name_mapping={'cause': 'cause', 'comment': 'comment', 'error': 'error'})
class FailProps():
    def __init__(self, *, cause: typing.Optional[str]=None, comment: typing.Optional[str]=None, error: typing.Optional[str]=None):
        """Properties for defining a Fail state.

        :param cause: A description for the cause of the failure. Default: No description
        :param comment: An optional description for this state. Default: No comment
        :param error: Error code used to represent this failure. Default: No error code

        stability
        :stability: experimental
        """
        self._values = {
        }
        if cause is not None: self._values["cause"] = cause
        if comment is not None: self._values["comment"] = comment
        if error is not None: self._values["error"] = error

    @property
    def cause(self) -> typing.Optional[str]:
        """A description for the cause of the failure.

        default
        :default: No description

        stability
        :stability: experimental
        """
        return self._values.get('cause')

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def error(self) -> typing.Optional[str]:
        """Error code used to represent this failure.

        default
        :default: No error code

        stability
        :stability: experimental
        """
        return self._values.get('error')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'FailProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class FieldUtils(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.FieldUtils"):
    """Helper functions to work with structures containing fields.

    stability
    :stability: experimental
    """
    @jsii.member(jsii_name="containsTaskToken")
    @classmethod
    def contains_task_token(cls, obj: typing.Optional[typing.Mapping[str,typing.Any]]=None) -> bool:
        """Returns whether the given task structure contains the TaskToken field anywhere.

        The field is considered included if the field itself or one of its containing
        fields occurs anywhere in the payload.

        :param obj: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "containsTaskToken", [obj])

    @jsii.member(jsii_name="findReferencedPaths")
    @classmethod
    def find_referenced_paths(cls, obj: typing.Optional[typing.Mapping[str,typing.Any]]=None) -> typing.List[str]:
        """Return all JSON paths used in the given structure.

        :param obj: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "findReferencedPaths", [obj])

    @jsii.member(jsii_name="renderObject")
    @classmethod
    def render_object(cls, obj: typing.Optional[typing.Mapping[str,typing.Any]]=None) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """Render a JSON structure containing fields to the right StepFunctions structure.

        :param obj: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "renderObject", [obj])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.FindStateOptions", jsii_struct_bases=[], name_mapping={'include_error_handlers': 'includeErrorHandlers'})
class FindStateOptions():
    def __init__(self, *, include_error_handlers: typing.Optional[bool]=None):
        """Options for finding reachable states.

        :param include_error_handlers: Whether or not to follow error-handling transitions. Default: false

        stability
        :stability: experimental
        """
        self._values = {
        }
        if include_error_handlers is not None: self._values["include_error_handlers"] = include_error_handlers

    @property
    def include_error_handlers(self) -> typing.Optional[bool]:
        """Whether or not to follow error-handling transitions.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('include_error_handlers')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'FindStateOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-stepfunctions.IActivity")
class IActivity(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IActivityProxy

    @property
    @jsii.member(jsii_name="activityArn")
    def activity_arn(self) -> str:
        """The ARN of the activity.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="activityName")
    def activity_name(self) -> str:
        """The name of the activity.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...


class _IActivityProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-stepfunctions.IActivity"
    @property
    @jsii.member(jsii_name="activityArn")
    def activity_arn(self) -> str:
        """The ARN of the activity.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "activityArn")

    @property
    @jsii.member(jsii_name="activityName")
    def activity_name(self) -> str:
        """The name of the activity.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "activityName")


@jsii.implements(IActivity)
class Activity(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Activity"):
    """Define a new StepFunctions activity.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, activity_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param activity_name: The name for this activity. Default: If not supplied, a name is generated

        stability
        :stability: experimental
        """
        props = ActivityProps(activity_name=activity_name)

        jsii.create(Activity, self, [scope, id, props])

    @jsii.member(jsii_name="fromActivityArn")
    @classmethod
    def from_activity_arn(cls, scope: aws_cdk.core.Construct, id: str, activity_arn: str) -> "IActivity":
        """Construct an Activity from an existing Activity ARN.

        :param scope: -
        :param id: -
        :param activity_arn: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromActivityArn", [scope, id, activity_arn])

    @jsii.member(jsii_name="fromActivityName")
    @classmethod
    def from_activity_name(cls, scope: aws_cdk.core.Construct, id: str, activity_name: str) -> "IActivity":
        """Construct an Activity from an existing Activity Name.

        :param scope: -
        :param id: -
        :param activity_name: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromActivityName", [scope, id, activity_name])

    @jsii.member(jsii_name="metric")
    def metric(self, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for this Activity.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity fails.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricFailed", [props])

    @jsii.member(jsii_name="metricHeartbeatTimedOut")
    def metric_heartbeat_timed_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times the heartbeat times out for this activity.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricHeartbeatTimedOut", [props])

    @jsii.member(jsii_name="metricRunTime")
    def metric_run_time(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The interval, in milliseconds, between the time the activity starts and the time it closes.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricRunTime", [props])

    @jsii.member(jsii_name="metricScheduled")
    def metric_scheduled(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity is scheduled.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricScheduled", [props])

    @jsii.member(jsii_name="metricScheduleTime")
    def metric_schedule_time(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The interval, in milliseconds, for which the activity stays in the schedule state.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricScheduleTime", [props])

    @jsii.member(jsii_name="metricStarted")
    def metric_started(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity is started.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricStarted", [props])

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity succeeds.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricSucceeded", [props])

    @jsii.member(jsii_name="metricTime")
    def metric_time(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The interval, in milliseconds, between the time the activity is scheduled and the time it closes.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTime", [props])

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity times out.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTimedOut", [props])

    @property
    @jsii.member(jsii_name="activityArn")
    def activity_arn(self) -> str:
        """The ARN of the activity.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "activityArn")

    @property
    @jsii.member(jsii_name="activityName")
    def activity_name(self) -> str:
        """The name of the activity.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "activityName")


@jsii.interface(jsii_type="@aws-cdk/aws-stepfunctions.IChainable")
class IChainable(jsii.compat.Protocol):
    """Interface for objects that can be used in a Chain.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IChainableProxy

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """The chainable end state(s) of this chainable.

        stability
        :stability: experimental
        """
        ...

    @property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """Descriptive identifier for this chainable.

        stability
        :stability: experimental
        """
        ...

    @property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        """The start state of this chainable.

        stability
        :stability: experimental
        """
        ...


class _IChainableProxy():
    """Interface for objects that can be used in a Chain.

    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-stepfunctions.IChainable"
    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """The chainable end state(s) of this chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")

    @property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """Descriptive identifier for this chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "id")

    @property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        """The start state of this chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "startState")


@jsii.implements(IChainable)
class Chain(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Chain"):
    """A collection of states to chain onto.

    A Chain has a start and zero or more chainable ends. If there are
    zero ends, calling next() on the Chain will fail.

    stability
    :stability: experimental
    """
    @jsii.member(jsii_name="custom")
    @classmethod
    def custom(cls, start_state: "State", end_states: typing.List["INextable"], last_added: "IChainable") -> "Chain":
        """Make a Chain with specific start and end states, and a last-added Chainable.

        :param start_state: -
        :param end_states: -
        :param last_added: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "custom", [start_state, end_states, last_added])

    @jsii.member(jsii_name="sequence")
    @classmethod
    def sequence(cls, start: "IChainable", next: "IChainable") -> "Chain":
        """Make a Chain with the start from one chain and the ends from another.

        :param start: -
        :param next: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "sequence", [start, next])

    @jsii.member(jsii_name="start")
    @classmethod
    def start(cls, state: "IChainable") -> "Chain":
        """Begin a new Chain from one chainable.

        :param state: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "start", [state])

    @jsii.member(jsii_name="next")
    def next(self, next: "IChainable") -> "Chain":
        """Continue normal execution with the given state.

        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "next", [next])

    @jsii.member(jsii_name="toSingleState")
    def to_single_state(self, id: str, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result_path: typing.Optional[str]=None) -> "Parallel":
        """Return a single state that encompasses all states in the chain.

        This can be used to add error handling to a sequence of states.

        Be aware that this changes the result of the inner state machine
        to be an array with the result of the state machine in it. Adjust
        your paths accordingly. For example, change 'outputPath' to
        '$[0]'.

        :param id: -
        :param props: -
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        props = ParallelProps(comment=comment, input_path=input_path, output_path=output_path, result_path=result_path)

        return jsii.invoke(self, "toSingleState", [id, props])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """The chainable end state(s) of this chain.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")

    @property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """Identify this Chain.

        stability
        :stability: experimental
        """
        return jsii.get(self, "id")

    @property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        """The start state of this chain.

        stability
        :stability: experimental
        """
        return jsii.get(self, "startState")


@jsii.interface(jsii_type="@aws-cdk/aws-stepfunctions.INextable")
class INextable(jsii.compat.Protocol):
    """Interface for states that can have 'next' states.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _INextableProxy

    @jsii.member(jsii_name="next")
    def next(self, state: "IChainable") -> "Chain":
        """Go to the indicated state after this state.

        :param state: -

        return
        :return: The chain of states built up

        stability
        :stability: experimental
        """
        ...


class _INextableProxy():
    """Interface for states that can have 'next' states.

    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-stepfunctions.INextable"
    @jsii.member(jsii_name="next")
    def next(self, state: "IChainable") -> "Chain":
        """Go to the indicated state after this state.

        :param state: -

        return
        :return: The chain of states built up

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "next", [state])


@jsii.interface(jsii_type="@aws-cdk/aws-stepfunctions.IStateMachine")
class IStateMachine(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A State Machine.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IStateMachineProxy

    @property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> str:
        """The ARN of the state machine.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...


class _IStateMachineProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A State Machine.

    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-stepfunctions.IStateMachine"
    @property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> str:
        """The ARN of the state machine.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "stateMachineArn")


@jsii.interface(jsii_type="@aws-cdk/aws-stepfunctions.IStepFunctionsTask")
class IStepFunctionsTask(jsii.compat.Protocol):
    """Interface for resources that can be used as tasks.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IStepFunctionsTaskProxy

    @jsii.member(jsii_name="bind")
    def bind(self, task: "Task") -> "StepFunctionsTaskConfig":
        """Called when the task object is used in a workflow.

        :param task: -

        stability
        :stability: experimental
        """
        ...


class _IStepFunctionsTaskProxy():
    """Interface for resources that can be used as tasks.

    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-stepfunctions.IStepFunctionsTask"
    @jsii.member(jsii_name="bind")
    def bind(self, task: "Task") -> "StepFunctionsTaskConfig":
        """Called when the task object is used in a workflow.

        :param task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [task])


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions.InputType")
class InputType(enum.Enum):
    """The type of task input.

    stability
    :stability: experimental
    """
    TEXT = "TEXT"
    """
    stability
    :stability: experimental
    """
    OBJECT = "OBJECT"
    """
    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.ParallelProps", jsii_struct_bases=[], name_mapping={'comment': 'comment', 'input_path': 'inputPath', 'output_path': 'outputPath', 'result_path': 'resultPath'})
class ParallelProps():
    def __init__(self, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result_path: typing.Optional[str]=None):
        """Properties for defining a Parallel state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        self._values = {
        }
        if comment is not None: self._values["comment"] = comment
        if input_path is not None: self._values["input_path"] = input_path
        if output_path is not None: self._values["output_path"] = output_path
        if result_path is not None: self._values["result_path"] = result_path

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the input to this state.

        May also be the special value DISCARD, which will cause the effective
        input to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('input_path')

    @property
    def output_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the output to this state.

        May also be the special value DISCARD, which will cause the effective
        output to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('output_path')

    @property
    def result_path(self) -> typing.Optional[str]:
        """JSONPath expression to indicate where to inject the state's output.

        May also be the special value DISCARD, which will cause the state's
        input to become its output.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('result_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ParallelProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.PassProps", jsii_struct_bases=[], name_mapping={'comment': 'comment', 'input_path': 'inputPath', 'output_path': 'outputPath', 'result': 'result', 'result_path': 'resultPath'})
class PassProps():
    def __init__(self, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result: typing.Optional["Result"]=None, result_path: typing.Optional[str]=None):
        """Properties for defining a Pass state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result: If given, treat as the result of this operation. Can be used to inject or replace the current execution state. Default: No injected result
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        self._values = {
        }
        if comment is not None: self._values["comment"] = comment
        if input_path is not None: self._values["input_path"] = input_path
        if output_path is not None: self._values["output_path"] = output_path
        if result is not None: self._values["result"] = result
        if result_path is not None: self._values["result_path"] = result_path

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the input to this state.

        May also be the special value DISCARD, which will cause the effective
        input to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('input_path')

    @property
    def output_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the output to this state.

        May also be the special value DISCARD, which will cause the effective
        output to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('output_path')

    @property
    def result(self) -> typing.Optional["Result"]:
        """If given, treat as the result of this operation.

        Can be used to inject or replace the current execution state.

        default
        :default: No injected result

        stability
        :stability: experimental
        """
        return self._values.get('result')

    @property
    def result_path(self) -> typing.Optional[str]:
        """JSONPath expression to indicate where to inject the state's output.

        May also be the special value DISCARD, which will cause the state's
        input to become its output.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('result_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PassProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Result(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Result"):
    """The result of a Pass operation.

    stability
    :stability: experimental
    """
    def __init__(self, value: typing.Any) -> None:
        """
        :param value: -

        stability
        :stability: experimental
        """
        jsii.create(Result, self, [value])

    @jsii.member(jsii_name="fromArray")
    @classmethod
    def from_array(cls, value: typing.List[typing.Any]) -> "Result":
        """The result of the operation is an array.

        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromArray", [value])

    @jsii.member(jsii_name="fromBoolean")
    @classmethod
    def from_boolean(cls, value: bool) -> "Result":
        """The result of the operation is a boolean.

        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromBoolean", [value])

    @jsii.member(jsii_name="fromNumber")
    @classmethod
    def from_number(cls, value: jsii.Number) -> "Result":
        """The result of the operation is a number.

        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromNumber", [value])

    @jsii.member(jsii_name="fromObject")
    @classmethod
    def from_object(cls, value: typing.Mapping[str,typing.Any]) -> "Result":
        """The result of the operation is an object.

        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromObject", [value])

    @jsii.member(jsii_name="fromString")
    @classmethod
    def from_string(cls, value: str) -> "Result":
        """The result of the operation is a string.

        :param value: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromString", [value])

    @property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "value")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.RetryProps", jsii_struct_bases=[], name_mapping={'backoff_rate': 'backoffRate', 'errors': 'errors', 'interval': 'interval', 'max_attempts': 'maxAttempts'})
class RetryProps():
    def __init__(self, *, backoff_rate: typing.Optional[jsii.Number]=None, errors: typing.Optional[typing.List[str]]=None, interval: typing.Optional[aws_cdk.core.Duration]=None, max_attempts: typing.Optional[jsii.Number]=None):
        """Retry details.

        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3

        stability
        :stability: experimental
        """
        self._values = {
        }
        if backoff_rate is not None: self._values["backoff_rate"] = backoff_rate
        if errors is not None: self._values["errors"] = errors
        if interval is not None: self._values["interval"] = interval
        if max_attempts is not None: self._values["max_attempts"] = max_attempts

    @property
    def backoff_rate(self) -> typing.Optional[jsii.Number]:
        """Multiplication for how much longer the wait interval gets on every retry.

        default
        :default: 2

        stability
        :stability: experimental
        """
        return self._values.get('backoff_rate')

    @property
    def errors(self) -> typing.Optional[typing.List[str]]:
        """Errors to retry.

        A list of error strings to retry, which can be either predefined errors
        (for example Errors.NoChoiceMatched) or a self-defined error.

        default
        :default: All errors

        stability
        :stability: experimental
        """
        return self._values.get('errors')

    @property
    def interval(self) -> typing.Optional[aws_cdk.core.Duration]:
        """How many seconds to wait initially before retrying.

        default
        :default: Duration.seconds(1)

        stability
        :stability: experimental
        """
        return self._values.get('interval')

    @property
    def max_attempts(self) -> typing.Optional[jsii.Number]:
        """How many times to retry this particular error.

        May be 0 to disable retry for specific errors (in case you have
        a catch-all retry policy).

        default
        :default: 3

        stability
        :stability: experimental
        """
        return self._values.get('max_attempts')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RetryProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions.ServiceIntegrationPattern")
class ServiceIntegrationPattern(enum.Enum):
    """Three ways to call an integrated service: Request Response, Run a Job and Wait for a Callback with Task Token.

    default
    :default: FIRE_AND_FORGET

    see
    :see:

    https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html

    Here, they are named as FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN respectly.
    stability
    :stability: experimental
    """
    FIRE_AND_FORGET = "FIRE_AND_FORGET"
    """Call a service and progress to the next state immediately after the API call completes.

    stability
    :stability: experimental
    """
    SYNC = "SYNC"
    """Call a service and wait for a job to complete.

    stability
    :stability: experimental
    """
    WAIT_FOR_TASK_TOKEN = "WAIT_FOR_TASK_TOKEN"
    """Call a service with a task token and wait until that token is returned by SendTaskSuccess/SendTaskFailure with paylaod.

    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.SingleStateOptions", jsii_struct_bases=[ParallelProps], name_mapping={'comment': 'comment', 'input_path': 'inputPath', 'output_path': 'outputPath', 'result_path': 'resultPath', 'prefix_states': 'prefixStates', 'state_id': 'stateId'})
class SingleStateOptions(ParallelProps):
    def __init__(self, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result_path: typing.Optional[str]=None, prefix_states: typing.Optional[str]=None, state_id: typing.Optional[str]=None):
        """Options for creating a single state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $
        :param prefix_states: String to prefix all stateIds in the state machine with. Default: stateId
        :param state_id: ID of newly created containing state. Default: Construct ID of the StateMachineFragment

        stability
        :stability: experimental
        """
        self._values = {
        }
        if comment is not None: self._values["comment"] = comment
        if input_path is not None: self._values["input_path"] = input_path
        if output_path is not None: self._values["output_path"] = output_path
        if result_path is not None: self._values["result_path"] = result_path
        if prefix_states is not None: self._values["prefix_states"] = prefix_states
        if state_id is not None: self._values["state_id"] = state_id

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the input to this state.

        May also be the special value DISCARD, which will cause the effective
        input to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('input_path')

    @property
    def output_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the output to this state.

        May also be the special value DISCARD, which will cause the effective
        output to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('output_path')

    @property
    def result_path(self) -> typing.Optional[str]:
        """JSONPath expression to indicate where to inject the state's output.

        May also be the special value DISCARD, which will cause the state's
        input to become its output.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('result_path')

    @property
    def prefix_states(self) -> typing.Optional[str]:
        """String to prefix all stateIds in the state machine with.

        default
        :default: stateId

        stability
        :stability: experimental
        """
        return self._values.get('prefix_states')

    @property
    def state_id(self) -> typing.Optional[str]:
        """ID of newly created containing state.

        default
        :default: Construct ID of the StateMachineFragment

        stability
        :stability: experimental
        """
        return self._values.get('state_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SingleStateOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IChainable)
class State(aws_cdk.core.Construct, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-stepfunctions.State"):
    """Base class for all other state classes.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _StateProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, result_path: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param comment: A comment describing this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param parameters: Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input. Default: No parameters
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        props = StateProps(comment=comment, input_path=input_path, output_path=output_path, parameters=parameters, result_path=result_path)

        jsii.create(State, self, [scope, id, props])

    @jsii.member(jsii_name="filterNextables")
    @classmethod
    def filter_nextables(cls, states: typing.List["State"]) -> typing.List["INextable"]:
        """Return only the states that allow chaining from an array of states.

        :param states: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "filterNextables", [states])

    @jsii.member(jsii_name="findReachableEndStates")
    @classmethod
    def find_reachable_end_states(cls, start: "State", *, include_error_handlers: typing.Optional[bool]=None) -> typing.List["State"]:
        """Find the set of end states states reachable through transitions from the given start state.

        :param start: -
        :param options: -
        :param include_error_handlers: Whether or not to follow error-handling transitions. Default: false

        stability
        :stability: experimental
        """
        options = FindStateOptions(include_error_handlers=include_error_handlers)

        return jsii.sinvoke(cls, "findReachableEndStates", [start, options])

    @jsii.member(jsii_name="prefixStates")
    @classmethod
    def prefix_states(cls, root: aws_cdk.core.IConstruct, prefix: str) -> None:
        """Add a prefix to the stateId of all States found in a construct tree.

        :param root: -
        :param prefix: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "prefixStates", [root, prefix])

    @jsii.member(jsii_name="addBranch")
    def _add_branch(self, branch: "StateGraph") -> None:
        """Add a paralle branch to this state.

        :param branch: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addBranch", [branch])

    @jsii.member(jsii_name="addChoice")
    def _add_choice(self, condition: "Condition", next: "State") -> None:
        """Add a choice branch to this state.

        :param condition: -
        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addChoice", [condition, next])

    @jsii.member(jsii_name="addPrefix")
    def add_prefix(self, x: str) -> None:
        """Add a prefix to the stateId of this state.

        :param x: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addPrefix", [x])

    @jsii.member(jsii_name="bindToGraph")
    def bind_to_graph(self, graph: "StateGraph") -> None:
        """Register this state as part of the given graph.

        Don't call this. It will be called automatically when you work
        with states normally.

        :param graph: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bindToGraph", [graph])

    @jsii.member(jsii_name="makeDefault")
    def _make_default(self, def_: "State") -> None:
        """Make the indicated state the default choice transition of this state.

        :param def_: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "makeDefault", [def_])

    @jsii.member(jsii_name="makeNext")
    def _make_next(self, next: "State") -> None:
        """Make the indicated state the default transition of this state.

        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "makeNext", [next])

    @jsii.member(jsii_name="renderBranches")
    def _render_branches(self) -> typing.Any:
        """Render parallel branches in ASL JSON format.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderBranches", [])

    @jsii.member(jsii_name="renderChoices")
    def _render_choices(self) -> typing.Any:
        """Render the choices in ASL JSON format.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderChoices", [])

    @jsii.member(jsii_name="renderInputOutput")
    def _render_input_output(self) -> typing.Any:
        """Render InputPath/Parameters/OutputPath in ASL JSON format.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderInputOutput", [])

    @jsii.member(jsii_name="renderNextEnd")
    def _render_next_end(self) -> typing.Any:
        """Render the default next state in ASL JSON format.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderNextEnd", [])

    @jsii.member(jsii_name="renderRetryCatch")
    def _render_retry_catch(self) -> typing.Any:
        """Render error recovery options in ASL JSON format.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "renderRetryCatch", [])

    @jsii.member(jsii_name="toStateJson")
    @abc.abstractmethod
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Render the state as JSON.

        stability
        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="whenBoundToGraph")
    def _when_bound_to_graph(self, graph: "StateGraph") -> None:
        """Called whenever this state is bound to a graph.

        Can be overridden by subclasses.

        :param graph: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "whenBoundToGraph", [graph])

    @property
    @jsii.member(jsii_name="branches")
    def _branches(self) -> typing.List["StateGraph"]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "branches")

    @property
    @jsii.member(jsii_name="endStates")
    @abc.abstractmethod
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        ...

    @property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """Descriptive identifier for this chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "id")

    @property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        """First state of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "startState")

    @property
    @jsii.member(jsii_name="stateId")
    def state_id(self) -> str:
        """Tokenized string that evaluates to the state's ID.

        stability
        :stability: experimental
        """
        return jsii.get(self, "stateId")

    @property
    @jsii.member(jsii_name="comment")
    def _comment(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "comment")

    @property
    @jsii.member(jsii_name="inputPath")
    def _input_path(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "inputPath")

    @property
    @jsii.member(jsii_name="outputPath")
    def _output_path(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "outputPath")

    @property
    @jsii.member(jsii_name="parameters")
    def _parameters(self) -> typing.Optional[typing.Mapping[typing.Any, typing.Any]]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "parameters")

    @property
    @jsii.member(jsii_name="resultPath")
    def _result_path(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "resultPath")

    @property
    @jsii.member(jsii_name="defaultChoice")
    def _default_choice(self) -> typing.Optional["State"]:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "defaultChoice")

    @_default_choice.setter
    def _default_choice(self, value: typing.Optional["State"]):
        return jsii.set(self, "defaultChoice", value)


class _StateProxy(State):
    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Render the state as JSON.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


class Choice(State, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Choice"):
    """Define a Choice in the state machine.

    A choice state can be used to make decisions based on the execution
    state.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $

        stability
        :stability: experimental
        """
        props = ChoiceProps(comment=comment, input_path=input_path, output_path=output_path)

        jsii.create(Choice, self, [scope, id, props])

    @jsii.member(jsii_name="afterwards")
    def afterwards(self, *, include_error_handlers: typing.Optional[bool]=None, include_otherwise: typing.Optional[bool]=None) -> "Chain":
        """Return a Chain that contains all reachable end states from this Choice.

        Use this to combine all possible choice paths back.

        :param options: -
        :param include_error_handlers: Whether to include error handling states. If this is true, all states which are error handlers (added through 'onError') and states reachable via error handlers will be included as well. Default: false
        :param include_otherwise: Whether to include the default/otherwise transition for the current Choice state. If this is true and the current Choice does not have a default outgoing transition, one will be added included when .next() is called on the chain. Default: false

        stability
        :stability: experimental
        """
        options = AfterwardsOptions(include_error_handlers=include_error_handlers, include_otherwise=include_otherwise)

        return jsii.invoke(self, "afterwards", [options])

    @jsii.member(jsii_name="otherwise")
    def otherwise(self, def_: "IChainable") -> "Choice":
        """If none of the given conditions match, continue execution with the given state.

        If no conditions match and no otherwise() has been given, an execution
        error will be raised.

        :param def_: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "otherwise", [def_])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language object for this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @jsii.member(jsii_name="when")
    def when(self, condition: "Condition", next: "IChainable") -> "Choice":
        """If the given condition matches, continue execution with the given state.

        :param condition: -
        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "when", [condition, next])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


class Fail(State, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Fail"):
    """Define a Fail state in the state machine.

    Reaching a Fail state terminates the state execution in failure.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cause: typing.Optional[str]=None, comment: typing.Optional[str]=None, error: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param cause: A description for the cause of the failure. Default: No description
        :param comment: An optional description for this state. Default: No comment
        :param error: Error code used to represent this failure. Default: No error code

        stability
        :stability: experimental
        """
        props = FailProps(cause=cause, comment=comment, error=error)

        jsii.create(Fail, self, [scope, id, props])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language object for this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


@jsii.implements(INextable)
class Parallel(State, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Parallel"):
    """Define a Parallel state in the state machine.

    A Parallel state can be used to run one or more state machines at the same
    time.

    The Result of a Parallel state is an array of the results of its substatemachines.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result_path: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        props = ParallelProps(comment=comment, input_path=input_path, output_path=output_path, result_path=result_path)

        jsii.create(Parallel, self, [scope, id, props])

    @jsii.member(jsii_name="addCatch")
    def add_catch(self, handler: "IChainable", *, errors: typing.Optional[typing.List[str]]=None, result_path: typing.Optional[str]=None) -> "Parallel":
        """Add a recovery handler for this state.

        When a particular error occurs, execution will continue at the error
        handler instead of failing the state machine execution.

        :param handler: -
        :param props: -
        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value DISCARD, which will cause the error data to be discarded. Default: $

        stability
        :stability: experimental
        """
        props = CatchProps(errors=errors, result_path=result_path)

        return jsii.invoke(self, "addCatch", [handler, props])

    @jsii.member(jsii_name="addRetry")
    def add_retry(self, *, backoff_rate: typing.Optional[jsii.Number]=None, errors: typing.Optional[typing.List[str]]=None, interval: typing.Optional[aws_cdk.core.Duration]=None, max_attempts: typing.Optional[jsii.Number]=None) -> "Parallel":
        """Add retry configuration for this state.

        This controls if and how the execution will be retried if a particular
        error occurs.

        :param props: -
        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3

        stability
        :stability: experimental
        """
        props = RetryProps(backoff_rate=backoff_rate, errors=errors, interval=interval, max_attempts=max_attempts)

        return jsii.invoke(self, "addRetry", [props])

    @jsii.member(jsii_name="branch")
    def branch(self, *branches: "IChainable") -> "Parallel":
        """Define one or more branches to run in parallel.

        :param branches: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "branch", [*branches])

    @jsii.member(jsii_name="next")
    def next(self, next: "IChainable") -> "Chain":
        """Continue normal execution with the given state.

        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "next", [next])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language object for this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[str]:
        """Validate this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "validate", [])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


@jsii.implements(INextable)
class Pass(State, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Pass"):
    """Define a Pass in the state machine.

    A Pass state can be used to transform the current exeuction's state.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result: typing.Optional["Result"]=None, result_path: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result: If given, treat as the result of this operation. Can be used to inject or replace the current execution state. Default: No injected result
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        props = PassProps(comment=comment, input_path=input_path, output_path=output_path, result=result, result_path=result_path)

        jsii.create(Pass, self, [scope, id, props])

    @jsii.member(jsii_name="next")
    def next(self, next: "IChainable") -> "Chain":
        """Continue normal execution with the given state.

        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "next", [next])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language object for this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


class StateGraph(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.StateGraph"):
    """A collection of connected states.

    A StateGraph is used to keep track of all states that are connected (have
    transitions between them). It does not include the substatemachines in
    a Parallel's branches: those are their own StateGraphs, but the graphs
    themselves have a hierarchical relationship as well.

    By assigning states to a definintive StateGraph, we verify that no state
    machines are constructed. In particular:

    - Every state object can only ever be in 1 StateGraph, and not inadvertently
      be used in two graphs.
    - Every stateId must be unique across all states in the entire state
      machine.

    All policy statements in all states in all substatemachines are bubbled so
    that the top-level StateMachine instantiation can read them all and add
    them to the IAM Role.

    You do not need to instantiate this class; it is used internally.

    stability
    :stability: experimental
    """
    def __init__(self, start_state: "State", graph_description: str) -> None:
        """
        :param start_state: -
        :param graph_description: -

        stability
        :stability: experimental
        """
        jsii.create(StateGraph, self, [start_state, graph_description])

    @jsii.member(jsii_name="registerPolicyStatement")
    def register_policy_statement(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Register a Policy Statement used by states in this graph.

        :param statement: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "registerPolicyStatement", [statement])

    @jsii.member(jsii_name="registerState")
    def register_state(self, state: "State") -> None:
        """Register a state as part of this graph.

        Called by State.bindToGraph().

        :param state: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "registerState", [state])

    @jsii.member(jsii_name="registerSuperGraph")
    def register_super_graph(self, graph: "StateGraph") -> None:
        """Register this graph as a child of the given graph.

        Resource changes will be bubbled up to the given graph.

        :param graph: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "registerSuperGraph", [graph])

    @jsii.member(jsii_name="toGraphJson")
    def to_graph_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language JSON for this graph.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toGraphJson", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Return a string description of this graph.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @property
    @jsii.member(jsii_name="policyStatements")
    def policy_statements(self) -> typing.List[aws_cdk.aws_iam.PolicyStatement]:
        """The accumulated policy statements.

        stability
        :stability: experimental
        """
        return jsii.get(self, "policyStatements")

    @property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "startState")

    @property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        """Set a timeout to render into the graph JSON.

        Read/write. Only makes sense on the top-level graph, subgraphs
        do not support this feature.

        default
        :default: No timeout

        stability
        :stability: experimental
        """
        return jsii.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: typing.Optional[aws_cdk.core.Duration]):
        return jsii.set(self, "timeout", value)


@jsii.implements(IStateMachine)
class StateMachine(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.StateMachine"):
    """Define a StepFunctions State Machine.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, definition: "IChainable", role: typing.Optional[aws_cdk.aws_iam.IRole]=None, state_machine_name: typing.Optional[str]=None, timeout: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param definition: Definition for this state machine.
        :param role: The execution role for the state machine service. Default: A role is automatically created
        :param state_machine_name: A name for the state machine. Default: A name is automatically generated
        :param timeout: Maximum run time for this state machine. Default: No timeout

        stability
        :stability: experimental
        """
        props = StateMachineProps(definition=definition, role=role, state_machine_name=state_machine_name, timeout=timeout)

        jsii.create(StateMachine, self, [scope, id, props])

    @jsii.member(jsii_name="fromStateMachineArn")
    @classmethod
    def from_state_machine_arn(cls, scope: aws_cdk.core.Construct, id: str, state_machine_arn: str) -> "IStateMachine":
        """Import a state machine.

        :param scope: -
        :param id: -
        :param state_machine_arn: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromStateMachineArn", [scope, id, state_machine_arn])

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Add the given statement to the role's policy.

        :param statement: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addToRolePolicy", [statement])

    @jsii.member(jsii_name="grantStartExecution")
    def grant_start_execution(self, identity: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant the given identity permissions to start an execution of this state machine.

        :param identity: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantStartExecution", [identity])

    @jsii.member(jsii_name="metric")
    def metric(self, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for this State Machine's executions.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricAborted")
    def metric_aborted(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of executions that were aborted.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricAborted", [props])

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of executions that failed.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricFailed", [props])

    @jsii.member(jsii_name="metricStarted")
    def metric_started(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of executions that were started.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricStarted", [props])

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of executions that succeeded.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricSucceeded", [props])

    @jsii.member(jsii_name="metricThrottled")
    def metric_throttled(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of executions that were throttled.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricThrottled", [props])

    @jsii.member(jsii_name="metricTime")
    def metric_time(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the interval, in milliseconds, between the time the execution starts and the time it closes.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTime", [props])

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of executions that succeeded.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTimedOut", [props])

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """Execution role of this state machine.

        stability
        :stability: experimental
        """
        return jsii.get(self, "role")

    @property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> str:
        """The ARN of the state machine.

        stability
        :stability: experimental
        """
        return jsii.get(self, "stateMachineArn")

    @property
    @jsii.member(jsii_name="stateMachineName")
    def state_machine_name(self) -> str:
        """The name of the state machine.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "stateMachineName")


@jsii.implements(IChainable)
class StateMachineFragment(aws_cdk.core.Construct, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-stepfunctions.StateMachineFragment"):
    """Base class for reusable state machine fragments.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _StateMachineFragmentProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str) -> None:
        """Creates a new construct node.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings. If the ID includes a path separator (``/``), then it will be replaced by double dash ``--``.
        """
        jsii.create(StateMachineFragment, self, [scope, id])

    @jsii.member(jsii_name="next")
    def next(self, next: "IChainable") -> "Chain":
        """Continue normal execution with the given state.

        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "next", [next])

    @jsii.member(jsii_name="prefixStates")
    def prefix_states(self, prefix: typing.Optional[str]=None) -> "StateMachineFragment":
        """Prefix the IDs of all states in this state machine fragment.

        Use this to avoid multiple copies of the state machine all having the
        same state IDs.

        :param prefix: The prefix to add. Will use construct ID by default.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "prefixStates", [prefix])

    @jsii.member(jsii_name="toSingleState")
    def to_single_state(self, *, prefix_states: typing.Optional[str]=None, state_id: typing.Optional[str]=None, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result_path: typing.Optional[str]=None) -> "Parallel":
        """Wrap all states in this state machine fragment up into a single state.

        This can be used to add retry or error handling onto this state
        machine fragment.

        Be aware that this changes the result of the inner state machine
        to be an array with the result of the state machine in it. Adjust
        your paths accordingly. For example, change 'outputPath' to
        '$[0]'.

        :param options: -
        :param prefix_states: String to prefix all stateIds in the state machine with. Default: stateId
        :param state_id: ID of newly created containing state. Default: Construct ID of the StateMachineFragment
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        options = SingleStateOptions(prefix_states=prefix_states, state_id=state_id, comment=comment, input_path=input_path, output_path=output_path, result_path=result_path)

        return jsii.invoke(self, "toSingleState", [options])

    @property
    @jsii.member(jsii_name="endStates")
    @abc.abstractmethod
    def end_states(self) -> typing.List["INextable"]:
        """The states to chain onto if this fragment is used.

        stability
        :stability: experimental
        """
        ...

    @property
    @jsii.member(jsii_name="id")
    def id(self) -> str:
        """Descriptive identifier for this chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "id")

    @property
    @jsii.member(jsii_name="startState")
    @abc.abstractmethod
    def start_state(self) -> "State":
        """The start state of this state machine fragment.

        stability
        :stability: experimental
        """
        ...


class _StateMachineFragmentProxy(StateMachineFragment):
    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """The states to chain onto if this fragment is used.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")

    @property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        """The start state of this state machine fragment.

        stability
        :stability: experimental
        """
        return jsii.get(self, "startState")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.StateMachineProps", jsii_struct_bases=[], name_mapping={'definition': 'definition', 'role': 'role', 'state_machine_name': 'stateMachineName', 'timeout': 'timeout'})
class StateMachineProps():
    def __init__(self, *, definition: "IChainable", role: typing.Optional[aws_cdk.aws_iam.IRole]=None, state_machine_name: typing.Optional[str]=None, timeout: typing.Optional[aws_cdk.core.Duration]=None):
        """Properties for defining a State Machine.

        :param definition: Definition for this state machine.
        :param role: The execution role for the state machine service. Default: A role is automatically created
        :param state_machine_name: A name for the state machine. Default: A name is automatically generated
        :param timeout: Maximum run time for this state machine. Default: No timeout

        stability
        :stability: experimental
        """
        self._values = {
            'definition': definition,
        }
        if role is not None: self._values["role"] = role
        if state_machine_name is not None: self._values["state_machine_name"] = state_machine_name
        if timeout is not None: self._values["timeout"] = timeout

    @property
    def definition(self) -> "IChainable":
        """Definition for this state machine.

        stability
        :stability: experimental
        """
        return self._values.get('definition')

    @property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """The execution role for the state machine service.

        default
        :default: A role is automatically created

        stability
        :stability: experimental
        """
        return self._values.get('role')

    @property
    def state_machine_name(self) -> typing.Optional[str]:
        """A name for the state machine.

        default
        :default: A name is automatically generated

        stability
        :stability: experimental
        """
        return self._values.get('state_machine_name')

    @property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        """Maximum run time for this state machine.

        default
        :default: No timeout

        stability
        :stability: experimental
        """
        return self._values.get('timeout')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StateMachineProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.StateProps", jsii_struct_bases=[], name_mapping={'comment': 'comment', 'input_path': 'inputPath', 'output_path': 'outputPath', 'parameters': 'parameters', 'result_path': 'resultPath'})
class StateProps():
    def __init__(self, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, result_path: typing.Optional[str]=None):
        """Properties shared by all states.

        :param comment: A comment describing this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param parameters: Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input. Default: No parameters
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $

        stability
        :stability: experimental
        """
        self._values = {
        }
        if comment is not None: self._values["comment"] = comment
        if input_path is not None: self._values["input_path"] = input_path
        if output_path is not None: self._values["output_path"] = output_path
        if parameters is not None: self._values["parameters"] = parameters
        if result_path is not None: self._values["result_path"] = result_path

    @property
    def comment(self) -> typing.Optional[str]:
        """A comment describing this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the input to this state.

        May also be the special value DISCARD, which will cause the effective
        input to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('input_path')

    @property
    def output_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the output to this state.

        May also be the special value DISCARD, which will cause the effective
        output to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('output_path')

    @property
    def parameters(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input.

        default
        :default: No parameters

        see
        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters
        stability
        :stability: experimental
        """
        return self._values.get('parameters')

    @property
    def result_path(self) -> typing.Optional[str]:
        """JSONPath expression to indicate where to inject the state's output.

        May also be the special value DISCARD, which will cause the state's
        input to become its output.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('result_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StateProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class StateTransitionMetric(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.StateTransitionMetric"):
    """Metrics on the rate limiting performed on state machine execution.

    These rate limits are shared across all state machines.

    stability
    :stability: experimental
    """
    def __init__(self) -> None:
        jsii.create(StateTransitionMetric, self, [])

    @jsii.member(jsii_name="metric")
    @classmethod
    def metric(cls, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for the service's state transition metrics.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricConsumedCapacity")
    @classmethod
    def metric_consumed_capacity(cls, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of available state transitions per second.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricConsumedCapacity", [props])

    @jsii.member(jsii_name="metricProvisionedBucketSize")
    @classmethod
    def metric_provisioned_bucket_size(cls, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of available state transitions.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricProvisionedBucketSize", [props])

    @jsii.member(jsii_name="metricProvisionedRefillRate")
    @classmethod
    def metric_provisioned_refill_rate(cls, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the provisioned steady-state execution rate.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricProvisionedRefillRate", [props])

    @jsii.member(jsii_name="metricThrottledEvents")
    @classmethod
    def metric_throttled_events(cls, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of throttled state transitions.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricThrottledEvents", [props])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.StepFunctionsTaskConfig", jsii_struct_bases=[], name_mapping={'resource_arn': 'resourceArn', 'heartbeat': 'heartbeat', 'metric_dimensions': 'metricDimensions', 'metric_prefix_plural': 'metricPrefixPlural', 'metric_prefix_singular': 'metricPrefixSingular', 'parameters': 'parameters', 'policy_statements': 'policyStatements'})
class StepFunctionsTaskConfig():
    def __init__(self, *, resource_arn: str, heartbeat: typing.Optional[aws_cdk.core.Duration]=None, metric_dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, metric_prefix_plural: typing.Optional[str]=None, metric_prefix_singular: typing.Optional[str]=None, parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, policy_statements: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]=None):
        """Properties that define what kind of task should be created.

        :param resource_arn: The resource that represents the work to be executed. Either the ARN of a Lambda Function or Activity, or a special ARN.
        :param heartbeat: Maximum time between heart beats. If the time between heart beats takes longer than this, a 'Timeout' error is raised. This is only relevant when using an Activity type as resource. Default: No heart beat timeout
        :param metric_dimensions: The dimensions to attach to metrics. Default: No metrics
        :param metric_prefix_plural: Prefix for plural metric names of activity actions. Default: No such metrics
        :param metric_prefix_singular: Prefix for singular metric names of activity actions. Default: No such metrics
        :param parameters: Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input. What is passed here will be merged with any default parameters configured by the ``resource``. For example, a DynamoDB table target will Default: No parameters
        :param policy_statements: Additional policy statements to add to the execution role. Default: No policy roles

        stability
        :stability: experimental
        """
        self._values = {
            'resource_arn': resource_arn,
        }
        if heartbeat is not None: self._values["heartbeat"] = heartbeat
        if metric_dimensions is not None: self._values["metric_dimensions"] = metric_dimensions
        if metric_prefix_plural is not None: self._values["metric_prefix_plural"] = metric_prefix_plural
        if metric_prefix_singular is not None: self._values["metric_prefix_singular"] = metric_prefix_singular
        if parameters is not None: self._values["parameters"] = parameters
        if policy_statements is not None: self._values["policy_statements"] = policy_statements

    @property
    def resource_arn(self) -> str:
        """The resource that represents the work to be executed.

        Either the ARN of a Lambda Function or Activity, or a special
        ARN.

        stability
        :stability: experimental
        """
        return self._values.get('resource_arn')

    @property
    def heartbeat(self) -> typing.Optional[aws_cdk.core.Duration]:
        """Maximum time between heart beats.

        If the time between heart beats takes longer than this, a 'Timeout' error is raised.

        This is only relevant when using an Activity type as resource.

        default
        :default: No heart beat timeout

        stability
        :stability: experimental
        """
        return self._values.get('heartbeat')

    @property
    def metric_dimensions(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """The dimensions to attach to metrics.

        default
        :default: No metrics

        stability
        :stability: experimental
        """
        return self._values.get('metric_dimensions')

    @property
    def metric_prefix_plural(self) -> typing.Optional[str]:
        """Prefix for plural metric names of activity actions.

        default
        :default: No such metrics

        stability
        :stability: experimental
        """
        return self._values.get('metric_prefix_plural')

    @property
    def metric_prefix_singular(self) -> typing.Optional[str]:
        """Prefix for singular metric names of activity actions.

        default
        :default: No such metrics

        stability
        :stability: experimental
        """
        return self._values.get('metric_prefix_singular')

    @property
    def parameters(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input.

        What is passed here will be merged with any default parameters
        configured by the ``resource``. For example, a DynamoDB table target
        will

        default
        :default: No parameters

        see
        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters
        stability
        :stability: experimental
        """
        return self._values.get('parameters')

    @property
    def policy_statements(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        """Additional policy statements to add to the execution role.

        default
        :default: No policy roles

        stability
        :stability: experimental
        """
        return self._values.get('policy_statements')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StepFunctionsTaskConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Succeed(State, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Succeed"):
    """Define a Succeed state in the state machine.

    Reaching a Succeed state terminates the state execution in success.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $

        stability
        :stability: experimental
        """
        props = SucceedProps(comment=comment, input_path=input_path, output_path=output_path)

        jsii.create(Succeed, self, [scope, id, props])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language object for this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.SucceedProps", jsii_struct_bases=[], name_mapping={'comment': 'comment', 'input_path': 'inputPath', 'output_path': 'outputPath'})
class SucceedProps():
    def __init__(self, *, comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None):
        """Properties for defining a Succeed state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $

        stability
        :stability: experimental
        """
        self._values = {
        }
        if comment is not None: self._values["comment"] = comment
        if input_path is not None: self._values["input_path"] = input_path
        if output_path is not None: self._values["output_path"] = output_path

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the input to this state.

        May also be the special value DISCARD, which will cause the effective
        input to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('input_path')

    @property
    def output_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the output to this state.

        May also be the special value DISCARD, which will cause the effective
        output to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('output_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SucceedProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(INextable)
class Task(State, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Task"):
    """Define a Task state in the state machine.

    Reaching a Task state causes some work to be executed, represented by the
    Task's resource property. Task constructs represent a generic Amazon
    States Language Task.

    For some resource types, more specific subclasses of Task may be available
    which are more convenient to use.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, task: "IStepFunctionsTask", comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result_path: typing.Optional[str]=None, timeout: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param task: Actual task to be invoked in this workflow.
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $
        :param timeout: Maximum run time of this state. If the state takes longer than this amount of time to complete, a 'Timeout' error is raised. Default: 60

        stability
        :stability: experimental
        """
        props = TaskProps(task=task, comment=comment, input_path=input_path, output_path=output_path, result_path=result_path, timeout=timeout)

        jsii.create(Task, self, [scope, id, props])

    @jsii.member(jsii_name="addCatch")
    def add_catch(self, handler: "IChainable", *, errors: typing.Optional[typing.List[str]]=None, result_path: typing.Optional[str]=None) -> "Task":
        """Add a recovery handler for this state.

        When a particular error occurs, execution will continue at the error
        handler instead of failing the state machine execution.

        :param handler: -
        :param props: -
        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value DISCARD, which will cause the error data to be discarded. Default: $

        stability
        :stability: experimental
        """
        props = CatchProps(errors=errors, result_path=result_path)

        return jsii.invoke(self, "addCatch", [handler, props])

    @jsii.member(jsii_name="addRetry")
    def add_retry(self, *, backoff_rate: typing.Optional[jsii.Number]=None, errors: typing.Optional[typing.List[str]]=None, interval: typing.Optional[aws_cdk.core.Duration]=None, max_attempts: typing.Optional[jsii.Number]=None) -> "Task":
        """Add retry configuration for this state.

        This controls if and how the execution will be retried if a particular
        error occurs.

        :param props: -
        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3

        stability
        :stability: experimental
        """
        props = RetryProps(backoff_rate=backoff_rate, errors=errors, interval=interval, max_attempts=max_attempts)

        return jsii.invoke(self, "addRetry", [props])

    @jsii.member(jsii_name="metric")
    def metric(self, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for this Task.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity fails.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricFailed", [props])

    @jsii.member(jsii_name="metricHeartbeatTimedOut")
    def metric_heartbeat_timed_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times the heartbeat times out for this activity.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricHeartbeatTimedOut", [props])

    @jsii.member(jsii_name="metricRunTime")
    def metric_run_time(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The interval, in milliseconds, between the time the Task starts and the time it closes.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricRunTime", [props])

    @jsii.member(jsii_name="metricScheduled")
    def metric_scheduled(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity is scheduled.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricScheduled", [props])

    @jsii.member(jsii_name="metricScheduleTime")
    def metric_schedule_time(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The interval, in milliseconds, for which the activity stays in the schedule state.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricScheduleTime", [props])

    @jsii.member(jsii_name="metricStarted")
    def metric_started(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity is started.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricStarted", [props])

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity succeeds.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricSucceeded", [props])

    @jsii.member(jsii_name="metricTime")
    def metric_time(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The interval, in milliseconds, between the time the activity is scheduled and the time it closes.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTime", [props])

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the number of times this activity times out.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTimedOut", [props])

    @jsii.member(jsii_name="next")
    def next(self, next: "IChainable") -> "Chain":
        """Continue normal execution with the given state.

        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "next", [next])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language object for this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @jsii.member(jsii_name="whenBoundToGraph")
    def _when_bound_to_graph(self, graph: "StateGraph") -> None:
        """Called whenever this state is bound to a graph.

        Can be overridden by subclasses.

        :param graph: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "whenBoundToGraph", [graph])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


class TaskInput(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.TaskInput"):
    """Type union for task classes that accept multiple types of payload.

    stability
    :stability: experimental
    """
    @jsii.member(jsii_name="fromContextAt")
    @classmethod
    def from_context_at(cls, path: str) -> "TaskInput":
        """Use a part of the task context as task input.

        Use this when you want to use a subobject or string from
        the current task context as complete payload
        to a task.

        :param path: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromContextAt", [path])

    @jsii.member(jsii_name="fromDataAt")
    @classmethod
    def from_data_at(cls, path: str) -> "TaskInput":
        """Use a part of the execution data as task input.

        Use this when you want to use a subobject or string from
        the current state machine execution as complete payload
        to a task.

        :param path: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromDataAt", [path])

    @jsii.member(jsii_name="fromObject")
    @classmethod
    def from_object(cls, obj: typing.Mapping[str,typing.Any]) -> "TaskInput":
        """Use an object as task input.

        This object may contain Data and Context fields
        as object values, if desired.

        :param obj: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromObject", [obj])

    @jsii.member(jsii_name="fromText")
    @classmethod
    def from_text(cls, text: str) -> "TaskInput":
        """Use a literal string as task input.

        This might be a JSON-encoded object, or just a text.

        :param text: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromText", [text])

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> "InputType":
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "type")

    @property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "value")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.TaskProps", jsii_struct_bases=[], name_mapping={'task': 'task', 'comment': 'comment', 'input_path': 'inputPath', 'output_path': 'outputPath', 'result_path': 'resultPath', 'timeout': 'timeout'})
class TaskProps():
    def __init__(self, *, task: "IStepFunctionsTask", comment: typing.Optional[str]=None, input_path: typing.Optional[str]=None, output_path: typing.Optional[str]=None, result_path: typing.Optional[str]=None, timeout: typing.Optional[aws_cdk.core.Duration]=None):
        """Props that are common to all tasks.

        :param task: Actual task to be invoked in this workflow.
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value DISCARD, which will cause the state's input to become its output. Default: $
        :param timeout: Maximum run time of this state. If the state takes longer than this amount of time to complete, a 'Timeout' error is raised. Default: 60

        stability
        :stability: experimental
        """
        self._values = {
            'task': task,
        }
        if comment is not None: self._values["comment"] = comment
        if input_path is not None: self._values["input_path"] = input_path
        if output_path is not None: self._values["output_path"] = output_path
        if result_path is not None: self._values["result_path"] = result_path
        if timeout is not None: self._values["timeout"] = timeout

    @property
    def task(self) -> "IStepFunctionsTask":
        """Actual task to be invoked in this workflow.

        stability
        :stability: experimental
        """
        return self._values.get('task')

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the input to this state.

        May also be the special value DISCARD, which will cause the effective
        input to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('input_path')

    @property
    def output_path(self) -> typing.Optional[str]:
        """JSONPath expression to select part of the state to be the output to this state.

        May also be the special value DISCARD, which will cause the effective
        output to be the empty object {}.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('output_path')

    @property
    def result_path(self) -> typing.Optional[str]:
        """JSONPath expression to indicate where to inject the state's output.

        May also be the special value DISCARD, which will cause the state's
        input to become its output.

        default
        :default: $

        stability
        :stability: experimental
        """
        return self._values.get('result_path')

    @property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        """Maximum run time of this state.

        If the state takes longer than this amount of time to complete, a 'Timeout' error is raised.

        default
        :default: 60

        stability
        :stability: experimental
        """
        return self._values.get('timeout')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(INextable)
class Wait(State, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.Wait"):
    """Define a Wait state in the state machine.

    A Wait state can be used to delay execution of the state machine for a while.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, time: "WaitTime", comment: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param time: Wait duration.
        :param comment: An optional description for this state. Default: No comment

        stability
        :stability: experimental
        """
        props = WaitProps(time=time, comment=comment)

        jsii.create(Wait, self, [scope, id, props])

    @jsii.member(jsii_name="next")
    def next(self, next: "IChainable") -> "Chain":
        """Continue normal execution with the given state.

        :param next: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "next", [next])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        """Return the Amazon States Language object for this state.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "toStateJson", [])

    @property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        """Continuable states of this Chainable.

        stability
        :stability: experimental
        """
        return jsii.get(self, "endStates")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions.WaitProps", jsii_struct_bases=[], name_mapping={'time': 'time', 'comment': 'comment'})
class WaitProps():
    def __init__(self, *, time: "WaitTime", comment: typing.Optional[str]=None):
        """Properties for defining a Wait state.

        :param time: Wait duration.
        :param comment: An optional description for this state. Default: No comment

        stability
        :stability: experimental
        """
        self._values = {
            'time': time,
        }
        if comment is not None: self._values["comment"] = comment

    @property
    def time(self) -> "WaitTime":
        """Wait duration.

        stability
        :stability: experimental
        """
        return self._values.get('time')

    @property
    def comment(self) -> typing.Optional[str]:
        """An optional description for this state.

        default
        :default: No comment

        stability
        :stability: experimental
        """
        return self._values.get('comment')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WaitProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class WaitTime(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions.WaitTime"):
    """
    stability
    :stability: experimental
    """
    @jsii.member(jsii_name="duration")
    @classmethod
    def duration(cls, duration: aws_cdk.core.Duration) -> "WaitTime":
        """Wait a fixed amount of time.

        :param duration: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "duration", [duration])

    @jsii.member(jsii_name="secondsPath")
    @classmethod
    def seconds_path(cls, path: str) -> "WaitTime":
        """Wait for a number of seconds stored in the state object.

        :param path: -

        stability
        :stability: experimental

        Example::
            $.waitSeconds
        """
        return jsii.sinvoke(cls, "secondsPath", [path])

    @jsii.member(jsii_name="timestamp")
    @classmethod
    def timestamp(cls, timestamp: str) -> "WaitTime":
        """Wait until the given ISO8601 timestamp.

        :param timestamp: -

        stability
        :stability: experimental

        Example::
            2016-03-14T01:59:00Z
        """
        return jsii.sinvoke(cls, "timestamp", [timestamp])

    @jsii.member(jsii_name="timestampPath")
    @classmethod
    def timestamp_path(cls, path: str) -> "WaitTime":
        """Wait until a timestamp found in the state object.

        :param path: -

        stability
        :stability: experimental

        Example::
            $.waitTimestamp
        """
        return jsii.sinvoke(cls, "timestampPath", [path])


__all__ = ["Activity", "ActivityProps", "AfterwardsOptions", "CatchProps", "CfnActivity", "CfnActivityProps", "CfnStateMachine", "CfnStateMachineProps", "Chain", "Choice", "ChoiceProps", "Condition", "Context", "Data", "Errors", "Fail", "FailProps", "FieldUtils", "FindStateOptions", "IActivity", "IChainable", "INextable", "IStateMachine", "IStepFunctionsTask", "InputType", "Parallel", "ParallelProps", "Pass", "PassProps", "Result", "RetryProps", "ServiceIntegrationPattern", "SingleStateOptions", "State", "StateGraph", "StateMachine", "StateMachineFragment", "StateMachineProps", "StateProps", "StateTransitionMetric", "StepFunctionsTaskConfig", "Succeed", "SucceedProps", "Task", "TaskInput", "TaskProps", "Wait", "WaitProps", "WaitTime", "__jsii_assembly__"]

publication.publish()
