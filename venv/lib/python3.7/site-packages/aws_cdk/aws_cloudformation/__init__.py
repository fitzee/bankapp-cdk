import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_sns
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-cloudformation", "1.8.0", __name__, "aws-cloudformation@1.8.0.jsii.tgz")
class CfnCustomResource(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnCustomResource"):
    """A CloudFormation ``AWS::CloudFormation::CustomResource``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFormation::CustomResource
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, service_token: str) -> None:
        """Create a new ``AWS::CloudFormation::CustomResource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param service_token: ``AWS::CloudFormation::CustomResource.ServiceToken``.
        """
        props = CfnCustomResourceProps(service_token=service_token)

        jsii.create(CfnCustomResource, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> str:
        """``AWS::CloudFormation::CustomResource.ServiceToken``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
        """
        return jsii.get(self, "serviceToken")

    @service_token.setter
    def service_token(self, value: str):
        return jsii.set(self, "serviceToken", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnCustomResourceProps", jsii_struct_bases=[], name_mapping={'service_token': 'serviceToken'})
class CfnCustomResourceProps():
    def __init__(self, *, service_token: str):
        """Properties for defining a ``AWS::CloudFormation::CustomResource``.

        :param service_token: ``AWS::CloudFormation::CustomResource.ServiceToken``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
        """
        self._values = {
            'service_token': service_token,
        }

    @property
    def service_token(self) -> str:
        """``AWS::CloudFormation::CustomResource.ServiceToken``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
        """
        return self._values.get('service_token')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnCustomResourceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnMacro(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnMacro"):
    """A CloudFormation ``AWS::CloudFormation::Macro``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFormation::Macro
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, function_name: str, name: str, description: typing.Optional[str]=None, log_group_name: typing.Optional[str]=None, log_role_arn: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::CloudFormation::Macro``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param function_name: ``AWS::CloudFormation::Macro.FunctionName``.
        :param name: ``AWS::CloudFormation::Macro.Name``.
        :param description: ``AWS::CloudFormation::Macro.Description``.
        :param log_group_name: ``AWS::CloudFormation::Macro.LogGroupName``.
        :param log_role_arn: ``AWS::CloudFormation::Macro.LogRoleARN``.
        """
        props = CfnMacroProps(function_name=function_name, name=name, description=description, log_group_name=log_group_name, log_role_arn=log_role_arn)

        jsii.create(CfnMacro, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> str:
        """``AWS::CloudFormation::Macro.FunctionName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        """
        return jsii.get(self, "functionName")

    @function_name.setter
    def function_name(self, value: str):
        return jsii.set(self, "functionName", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::CloudFormation::Macro.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.LogGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        """
        return jsii.get(self, "logGroupName")

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "logGroupName", value)

    @property
    @jsii.member(jsii_name="logRoleArn")
    def log_role_arn(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.LogRoleARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        """
        return jsii.get(self, "logRoleArn")

    @log_role_arn.setter
    def log_role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "logRoleArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnMacroProps", jsii_struct_bases=[], name_mapping={'function_name': 'functionName', 'name': 'name', 'description': 'description', 'log_group_name': 'logGroupName', 'log_role_arn': 'logRoleArn'})
class CfnMacroProps():
    def __init__(self, *, function_name: str, name: str, description: typing.Optional[str]=None, log_group_name: typing.Optional[str]=None, log_role_arn: typing.Optional[str]=None):
        """Properties for defining a ``AWS::CloudFormation::Macro``.

        :param function_name: ``AWS::CloudFormation::Macro.FunctionName``.
        :param name: ``AWS::CloudFormation::Macro.Name``.
        :param description: ``AWS::CloudFormation::Macro.Description``.
        :param log_group_name: ``AWS::CloudFormation::Macro.LogGroupName``.
        :param log_role_arn: ``AWS::CloudFormation::Macro.LogRoleARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
        """
        self._values = {
            'function_name': function_name,
            'name': name,
        }
        if description is not None: self._values["description"] = description
        if log_group_name is not None: self._values["log_group_name"] = log_group_name
        if log_role_arn is not None: self._values["log_role_arn"] = log_role_arn

    @property
    def function_name(self) -> str:
        """``AWS::CloudFormation::Macro.FunctionName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        """
        return self._values.get('function_name')

    @property
    def name(self) -> str:
        """``AWS::CloudFormation::Macro.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
        """
        return self._values.get('name')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        """
        return self._values.get('description')

    @property
    def log_group_name(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.LogGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        """
        return self._values.get('log_group_name')

    @property
    def log_role_arn(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.LogRoleARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        """
        return self._values.get('log_role_arn')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMacroProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnStack(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnStack"):
    """A CloudFormation ``AWS::CloudFormation::Stack``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFormation::Stack
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, template_url: str, notification_arns: typing.Optional[typing.List[str]]=None, parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, timeout_in_minutes: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::CloudFormation::Stack``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param template_url: ``AWS::CloudFormation::Stack.TemplateURL``.
        :param notification_arns: ``AWS::CloudFormation::Stack.NotificationARNs``.
        :param parameters: ``AWS::CloudFormation::Stack.Parameters``.
        :param tags: ``AWS::CloudFormation::Stack.Tags``.
        :param timeout_in_minutes: ``AWS::CloudFormation::Stack.TimeoutInMinutes``.
        """
        props = CfnStackProps(template_url=template_url, notification_arns=notification_arns, parameters=parameters, tags=tags, timeout_in_minutes=timeout_in_minutes)

        jsii.create(CfnStack, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::CloudFormation::Stack.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> str:
        """``AWS::CloudFormation::Stack.TemplateURL``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
        """
        return jsii.get(self, "templateUrl")

    @template_url.setter
    def template_url(self, value: str):
        return jsii.set(self, "templateUrl", value)

    @property
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::CloudFormation::Stack.NotificationARNs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
        """
        return jsii.get(self, "notificationArns")

    @notification_arns.setter
    def notification_arns(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "notificationArns", value)

    @property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]:
        """``AWS::CloudFormation::Stack.Parameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
        """
        return jsii.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]):
        return jsii.set(self, "parameters", value)

    @property
    @jsii.member(jsii_name="timeoutInMinutes")
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        """``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
        """
        return jsii.get(self, "timeoutInMinutes")

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "timeoutInMinutes", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnStackProps", jsii_struct_bases=[], name_mapping={'template_url': 'templateUrl', 'notification_arns': 'notificationArns', 'parameters': 'parameters', 'tags': 'tags', 'timeout_in_minutes': 'timeoutInMinutes'})
class CfnStackProps():
    def __init__(self, *, template_url: str, notification_arns: typing.Optional[typing.List[str]]=None, parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, timeout_in_minutes: typing.Optional[jsii.Number]=None):
        """Properties for defining a ``AWS::CloudFormation::Stack``.

        :param template_url: ``AWS::CloudFormation::Stack.TemplateURL``.
        :param notification_arns: ``AWS::CloudFormation::Stack.NotificationARNs``.
        :param parameters: ``AWS::CloudFormation::Stack.Parameters``.
        :param tags: ``AWS::CloudFormation::Stack.Tags``.
        :param timeout_in_minutes: ``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
        """
        self._values = {
            'template_url': template_url,
        }
        if notification_arns is not None: self._values["notification_arns"] = notification_arns
        if parameters is not None: self._values["parameters"] = parameters
        if tags is not None: self._values["tags"] = tags
        if timeout_in_minutes is not None: self._values["timeout_in_minutes"] = timeout_in_minutes

    @property
    def template_url(self) -> str:
        """``AWS::CloudFormation::Stack.TemplateURL``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
        """
        return self._values.get('template_url')

    @property
    def notification_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::CloudFormation::Stack.NotificationARNs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
        """
        return self._values.get('notification_arns')

    @property
    def parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]:
        """``AWS::CloudFormation::Stack.Parameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
        """
        return self._values.get('parameters')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::CloudFormation::Stack.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
        """
        return self._values.get('tags')

    @property
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        """``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
        """
        return self._values.get('timeout_in_minutes')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnStackProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnWaitCondition(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnWaitCondition"):
    """A CloudFormation ``AWS::CloudFormation::WaitCondition``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFormation::WaitCondition
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, count: typing.Optional[jsii.Number]=None, handle: typing.Optional[str]=None, timeout: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::CloudFormation::WaitCondition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param count: ``AWS::CloudFormation::WaitCondition.Count``.
        :param handle: ``AWS::CloudFormation::WaitCondition.Handle``.
        :param timeout: ``AWS::CloudFormation::WaitCondition.Timeout``.
        """
        props = CfnWaitConditionProps(count=count, handle=handle, timeout=timeout)

        jsii.create(CfnWaitCondition, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrData")
    def attr_data(self) -> aws_cdk.core.IResolvable:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Data
        """
        return jsii.get(self, "attrData")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        """``AWS::CloudFormation::WaitCondition.Count``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
        """
        return jsii.get(self, "count")

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "count", value)

    @property
    @jsii.member(jsii_name="handle")
    def handle(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::WaitCondition.Handle``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
        """
        return jsii.get(self, "handle")

    @handle.setter
    def handle(self, value: typing.Optional[str]):
        return jsii.set(self, "handle", value)

    @property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::WaitCondition.Timeout``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
        """
        return jsii.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: typing.Optional[str]):
        return jsii.set(self, "timeout", value)


class CfnWaitConditionHandle(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnWaitConditionHandle"):
    """A CloudFormation ``AWS::CloudFormation::WaitConditionHandle``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html
    cloudformationResource:
    :cloudformationResource:: AWS::CloudFormation::WaitConditionHandle
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str) -> None:
        """Create a new ``AWS::CloudFormation::WaitConditionHandle``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        """
        jsii.create(CfnWaitConditionHandle, self, [scope, id])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")


@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnWaitConditionProps", jsii_struct_bases=[], name_mapping={'count': 'count', 'handle': 'handle', 'timeout': 'timeout'})
class CfnWaitConditionProps():
    def __init__(self, *, count: typing.Optional[jsii.Number]=None, handle: typing.Optional[str]=None, timeout: typing.Optional[str]=None):
        """Properties for defining a ``AWS::CloudFormation::WaitCondition``.

        :param count: ``AWS::CloudFormation::WaitCondition.Count``.
        :param handle: ``AWS::CloudFormation::WaitCondition.Handle``.
        :param timeout: ``AWS::CloudFormation::WaitCondition.Timeout``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
        """
        self._values = {
        }
        if count is not None: self._values["count"] = count
        if handle is not None: self._values["handle"] = handle
        if timeout is not None: self._values["timeout"] = timeout

    @property
    def count(self) -> typing.Optional[jsii.Number]:
        """``AWS::CloudFormation::WaitCondition.Count``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
        """
        return self._values.get('count')

    @property
    def handle(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::WaitCondition.Handle``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
        """
        return self._values.get('handle')

    @property
    def timeout(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::WaitCondition.Timeout``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
        """
        return self._values.get('timeout')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnWaitConditionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-cloudformation.CloudFormationCapabilities")
class CloudFormationCapabilities(enum.Enum):
    """Capabilities that affect whether CloudFormation is allowed to change IAM resources."""
    NONE = "NONE"
    """No IAM Capabilities.

    Pass this capability if you wish to block the creation IAM resources.

    link:
    :link:: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    """
    ANONYMOUS_IAM = "ANONYMOUS_IAM"
    """Capability to create anonymous IAM resources.

    Pass this capability if you're only creating anonymous resources.

    link:
    :link:: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    """
    NAMED_IAM = "NAMED_IAM"
    """Capability to create named IAM resources.

    Pass this capability if you're creating IAM resources that have physical
    names.

    ``CloudFormationCapabilities.NamedIAM`` implies ``CloudFormationCapabilities.IAM``; you don't have to pass both.

    link:
    :link:: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    """
    AUTO_EXPAND = "AUTO_EXPAND"
    """Capability to run CloudFormation macros.

    Pass this capability if your template includes macros, for example AWS::Include or AWS::Serverless.

    link:
    :link:: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html
    """

class CustomResource(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CustomResource"):
    """Custom resource that is implemented using a Lambda.

    As a custom resource author, you should be publishing a subclass of this class
    that hides the choice of provider, and accepts a strongly-typed properties
    object with the properties your provider accepts.
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, provider: "CustomResourceProvider", properties: typing.Optional[typing.Mapping[str,typing.Any]]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None, resource_type: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param provider: The provider which implements the custom resource.
        :param properties: Properties to pass to the Lambda. Default: - No properties.
        :param removal_policy: The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy
        :param resource_type: For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name. For example, you can use "Custom::MyCustomResourceTypeName". Custom resource type names must begin with "Custom::" and can include alphanumeric characters and the following characters: _@-. You can specify a custom resource type name up to a maximum length of 60 characters. You cannot change the type during an update. Using your own resource type names helps you quickly differentiate the types of custom resources in your stack. For example, if you had two custom resources that conduct two different ping tests, you could name their type as Custom::PingTester to make them easily identifiable as ping testers (instead of using AWS::CloudFormation::CustomResource). Default: - AWS::CloudFormation::CustomResource
        """
        props = CustomResourceProps(provider=provider, properties=properties, removal_policy=removal_policy, resource_type=resource_type)

        jsii.create(CustomResource, self, [scope, id, props])

    @jsii.member(jsii_name="getAtt")
    def get_att(self, attribute_name: str) -> aws_cdk.core.IResolvable:
        """An attribute of this custom resource.

        :param attribute_name: the attribute name.
        """
        return jsii.invoke(self, "getAtt", [attribute_name])

    @property
    @jsii.member(jsii_name="ref")
    def ref(self) -> str:
        """The physical name of this custom resource."""
        return jsii.get(self, "ref")


@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CustomResourceProps", jsii_struct_bases=[], name_mapping={'provider': 'provider', 'properties': 'properties', 'removal_policy': 'removalPolicy', 'resource_type': 'resourceType'})
class CustomResourceProps():
    def __init__(self, *, provider: "CustomResourceProvider", properties: typing.Optional[typing.Mapping[str,typing.Any]]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None, resource_type: typing.Optional[str]=None):
        """Properties to provide a Lambda-backed custom resource.

        :param provider: The provider which implements the custom resource.
        :param properties: Properties to pass to the Lambda. Default: - No properties.
        :param removal_policy: The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy
        :param resource_type: For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name. For example, you can use "Custom::MyCustomResourceTypeName". Custom resource type names must begin with "Custom::" and can include alphanumeric characters and the following characters: _@-. You can specify a custom resource type name up to a maximum length of 60 characters. You cannot change the type during an update. Using your own resource type names helps you quickly differentiate the types of custom resources in your stack. For example, if you had two custom resources that conduct two different ping tests, you could name their type as Custom::PingTester to make them easily identifiable as ping testers (instead of using AWS::CloudFormation::CustomResource). Default: - AWS::CloudFormation::CustomResource
        """
        self._values = {
            'provider': provider,
        }
        if properties is not None: self._values["properties"] = properties
        if removal_policy is not None: self._values["removal_policy"] = removal_policy
        if resource_type is not None: self._values["resource_type"] = resource_type

    @property
    def provider(self) -> "CustomResourceProvider":
        """The provider which implements the custom resource.

        Example::
            CustomResourceProvider.topic(myTopic)
        """
        return self._values.get('provider')

    @property
    def properties(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """Properties to pass to the Lambda.

        default
        :default: - No properties.
        """
        return self._values.get('properties')

    @property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        """The policy to apply when this resource is removed from the application.

        default
        :default: cdk.RemovalPolicy.Destroy
        """
        return self._values.get('removal_policy')

    @property
    def resource_type(self) -> typing.Optional[str]:
        """For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name.

        For example, you can use "Custom::MyCustomResourceTypeName".

        Custom resource type names must begin with "Custom::" and can include
        alphanumeric characters and the following characters: _@-. You can specify
        a custom resource type name up to a maximum length of 60 characters. You
        cannot change the type during an update.

        Using your own resource type names helps you quickly differentiate the
        types of custom resources in your stack. For example, if you had two custom
        resources that conduct two different ping tests, you could name their type
        as Custom::PingTester to make them easily identifiable as ping testers
        (instead of using AWS::CloudFormation::CustomResource).

        default
        :default: - AWS::CloudFormation::CustomResource

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#aws-cfn-resource-type-name
        """
        return self._values.get('resource_type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CustomResourceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CustomResourceProvider(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CustomResourceProvider"):
    @jsii.member(jsii_name="lambda")
    @classmethod
    def lambda_(cls, handler: aws_cdk.aws_lambda.IFunction) -> "CustomResourceProvider":
        """The Lambda provider that implements this custom resource.

        We recommend using a lambda.SingletonFunction for this.

        :param handler: -
        """
        return jsii.sinvoke(cls, "lambda", [handler])

    @jsii.member(jsii_name="topic")
    @classmethod
    def topic(cls, topic: aws_cdk.aws_sns.ITopic) -> "CustomResourceProvider":
        """The SNS Topic for the provider that implements this custom resource.

        :param topic: -
        """
        return jsii.sinvoke(cls, "topic", [topic])

    @property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> str:
        return jsii.get(self, "serviceToken")


__all__ = ["CfnCustomResource", "CfnCustomResourceProps", "CfnMacro", "CfnMacroProps", "CfnStack", "CfnStackProps", "CfnWaitCondition", "CfnWaitConditionHandle", "CfnWaitConditionProps", "CloudFormationCapabilities", "CustomResource", "CustomResourceProps", "CustomResourceProvider", "__jsii_assembly__"]

publication.publish()
