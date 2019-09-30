import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.aws_logs
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-kinesis", "1.8.0", __name__, "aws-kinesis@1.8.0.jsii.tgz")
class CfnStream(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesis.CfnStream"):
    """A CloudFormation ``AWS::Kinesis::Stream``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html
    cloudformationResource:
    :cloudformationResource:: AWS::Kinesis::Stream
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, shard_count: jsii.Number, name: typing.Optional[str]=None, retention_period_hours: typing.Optional[jsii.Number]=None, stream_encryption: typing.Optional[typing.Union[typing.Optional["StreamEncryptionProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::Kinesis::Stream``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param shard_count: ``AWS::Kinesis::Stream.ShardCount``.
        :param name: ``AWS::Kinesis::Stream.Name``.
        :param retention_period_hours: ``AWS::Kinesis::Stream.RetentionPeriodHours``.
        :param stream_encryption: ``AWS::Kinesis::Stream.StreamEncryption``.
        :param tags: ``AWS::Kinesis::Stream.Tags``.
        """
        props = CfnStreamProps(shard_count=shard_count, name=name, retention_period_hours=retention_period_hours, stream_encryption=stream_encryption, tags=tags)

        jsii.create(CfnStream, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Arn
        """
        return jsii.get(self, "attrArn")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::Kinesis::Stream.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="shardCount")
    def shard_count(self) -> jsii.Number:
        """``AWS::Kinesis::Stream.ShardCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-shardcount
        """
        return jsii.get(self, "shardCount")

    @shard_count.setter
    def shard_count(self, value: jsii.Number):
        return jsii.set(self, "shardCount", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Kinesis::Stream.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="retentionPeriodHours")
    def retention_period_hours(self) -> typing.Optional[jsii.Number]:
        """``AWS::Kinesis::Stream.RetentionPeriodHours``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-retentionperiodhours
        """
        return jsii.get(self, "retentionPeriodHours")

    @retention_period_hours.setter
    def retention_period_hours(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "retentionPeriodHours", value)

    @property
    @jsii.member(jsii_name="streamEncryption")
    def stream_encryption(self) -> typing.Optional[typing.Union[typing.Optional["StreamEncryptionProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Kinesis::Stream.StreamEncryption``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-streamencryption
        """
        return jsii.get(self, "streamEncryption")

    @stream_encryption.setter
    def stream_encryption(self, value: typing.Optional[typing.Union[typing.Optional["StreamEncryptionProperty"], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "streamEncryption", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesis.CfnStream.StreamEncryptionProperty", jsii_struct_bases=[], name_mapping={'encryption_type': 'encryptionType', 'key_id': 'keyId'})
    class StreamEncryptionProperty():
        def __init__(self, *, encryption_type: str, key_id: str):
            """
            :param encryption_type: ``CfnStream.StreamEncryptionProperty.EncryptionType``.
            :param key_id: ``CfnStream.StreamEncryptionProperty.KeyId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html
            """
            self._values = {
                'encryption_type': encryption_type,
                'key_id': key_id,
            }

        @property
        def encryption_type(self) -> str:
            """``CfnStream.StreamEncryptionProperty.EncryptionType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html#cfn-kinesis-stream-streamencryption-encryptiontype
            """
            return self._values.get('encryption_type')

        @property
        def key_id(self) -> str:
            """``CfnStream.StreamEncryptionProperty.KeyId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html#cfn-kinesis-stream-streamencryption-keyid
            """
            return self._values.get('key_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StreamEncryptionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



class CfnStreamConsumer(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesis.CfnStreamConsumer"):
    """A CloudFormation ``AWS::Kinesis::StreamConsumer``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html
    cloudformationResource:
    :cloudformationResource:: AWS::Kinesis::StreamConsumer
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, consumer_name: str, stream_arn: str) -> None:
        """Create a new ``AWS::Kinesis::StreamConsumer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param consumer_name: ``AWS::Kinesis::StreamConsumer.ConsumerName``.
        :param stream_arn: ``AWS::Kinesis::StreamConsumer.StreamARN``.
        """
        props = CfnStreamConsumerProps(consumer_name=consumer_name, stream_arn=stream_arn)

        jsii.create(CfnStreamConsumer, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrConsumerArn")
    def attr_consumer_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ConsumerARN
        """
        return jsii.get(self, "attrConsumerArn")

    @property
    @jsii.member(jsii_name="attrConsumerCreationTimestamp")
    def attr_consumer_creation_timestamp(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ConsumerCreationTimestamp
        """
        return jsii.get(self, "attrConsumerCreationTimestamp")

    @property
    @jsii.member(jsii_name="attrConsumerName")
    def attr_consumer_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ConsumerName
        """
        return jsii.get(self, "attrConsumerName")

    @property
    @jsii.member(jsii_name="attrConsumerStatus")
    def attr_consumer_status(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ConsumerStatus
        """
        return jsii.get(self, "attrConsumerStatus")

    @property
    @jsii.member(jsii_name="attrStreamArn")
    def attr_stream_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: StreamARN
        """
        return jsii.get(self, "attrStreamArn")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="consumerName")
    def consumer_name(self) -> str:
        """``AWS::Kinesis::StreamConsumer.ConsumerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html#cfn-kinesis-streamconsumer-consumername
        """
        return jsii.get(self, "consumerName")

    @consumer_name.setter
    def consumer_name(self, value: str):
        return jsii.set(self, "consumerName", value)

    @property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> str:
        """``AWS::Kinesis::StreamConsumer.StreamARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html#cfn-kinesis-streamconsumer-streamarn
        """
        return jsii.get(self, "streamArn")

    @stream_arn.setter
    def stream_arn(self, value: str):
        return jsii.set(self, "streamArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesis.CfnStreamConsumerProps", jsii_struct_bases=[], name_mapping={'consumer_name': 'consumerName', 'stream_arn': 'streamArn'})
class CfnStreamConsumerProps():
    def __init__(self, *, consumer_name: str, stream_arn: str):
        """Properties for defining a ``AWS::Kinesis::StreamConsumer``.

        :param consumer_name: ``AWS::Kinesis::StreamConsumer.ConsumerName``.
        :param stream_arn: ``AWS::Kinesis::StreamConsumer.StreamARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html
        """
        self._values = {
            'consumer_name': consumer_name,
            'stream_arn': stream_arn,
        }

    @property
    def consumer_name(self) -> str:
        """``AWS::Kinesis::StreamConsumer.ConsumerName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html#cfn-kinesis-streamconsumer-consumername
        """
        return self._values.get('consumer_name')

    @property
    def stream_arn(self) -> str:
        """``AWS::Kinesis::StreamConsumer.StreamARN``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html#cfn-kinesis-streamconsumer-streamarn
        """
        return self._values.get('stream_arn')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnStreamConsumerProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesis.CfnStreamProps", jsii_struct_bases=[], name_mapping={'shard_count': 'shardCount', 'name': 'name', 'retention_period_hours': 'retentionPeriodHours', 'stream_encryption': 'streamEncryption', 'tags': 'tags'})
class CfnStreamProps():
    def __init__(self, *, shard_count: jsii.Number, name: typing.Optional[str]=None, retention_period_hours: typing.Optional[jsii.Number]=None, stream_encryption: typing.Optional[typing.Union[typing.Optional["CfnStream.StreamEncryptionProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::Kinesis::Stream``.

        :param shard_count: ``AWS::Kinesis::Stream.ShardCount``.
        :param name: ``AWS::Kinesis::Stream.Name``.
        :param retention_period_hours: ``AWS::Kinesis::Stream.RetentionPeriodHours``.
        :param stream_encryption: ``AWS::Kinesis::Stream.StreamEncryption``.
        :param tags: ``AWS::Kinesis::Stream.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html
        """
        self._values = {
            'shard_count': shard_count,
        }
        if name is not None: self._values["name"] = name
        if retention_period_hours is not None: self._values["retention_period_hours"] = retention_period_hours
        if stream_encryption is not None: self._values["stream_encryption"] = stream_encryption
        if tags is not None: self._values["tags"] = tags

    @property
    def shard_count(self) -> jsii.Number:
        """``AWS::Kinesis::Stream.ShardCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-shardcount
        """
        return self._values.get('shard_count')

    @property
    def name(self) -> typing.Optional[str]:
        """``AWS::Kinesis::Stream.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-name
        """
        return self._values.get('name')

    @property
    def retention_period_hours(self) -> typing.Optional[jsii.Number]:
        """``AWS::Kinesis::Stream.RetentionPeriodHours``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-retentionperiodhours
        """
        return self._values.get('retention_period_hours')

    @property
    def stream_encryption(self) -> typing.Optional[typing.Union[typing.Optional["CfnStream.StreamEncryptionProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Kinesis::Stream.StreamEncryption``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-streamencryption
        """
        return self._values.get('stream_encryption')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::Kinesis::Stream.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnStreamProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-kinesis.IStream")
class IStream(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IStreamProxy

    @property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> str:
        """The ARN of the stream.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> str:
        """The name of the stream.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """Optional KMS encryption key associated with this stream.

        stability
        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant read permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to ues the key to decrypt the
        contents of the stream will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants read/write permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to use the key for
        encrypt/decrypt will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant write permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to ues the key to encrypt the
        contents of the stream will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        ...


class _IStreamProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-kinesis.IStream"
    @property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> str:
        """The ARN of the stream.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "streamArn")

    @property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> str:
        """The name of the stream.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "streamName")

    @property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """Optional KMS encryption key associated with this stream.

        stability
        :stability: experimental
        """
        return jsii.get(self, "encryptionKey")

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant read permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to ues the key to decrypt the
        contents of the stream will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants read/write permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to use the key for
        encrypt/decrypt will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantReadWrite", [grantee])

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant write permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to ues the key to encrypt the
        contents of the stream will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantWrite", [grantee])


@jsii.implements(IStream)
class Stream(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesis.Stream"):
    """A Kinesis stream.

    Can be encrypted with a KMS key.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, encryption: typing.Optional["StreamEncryption"]=None, encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None, retention_period_hours: typing.Optional[jsii.Number]=None, shard_count: typing.Optional[jsii.Number]=None, stream_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param encryption: The kind of server-side encryption to apply to this stream. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryption key is not specified, a key will automatically be created. Default: Unencrypted
        :param encryption_key: External KMS key to use for stream encryption. The 'encryption' property must be set to "Kms". Default: If encryption is set to "Kms" and this property is undefined, a new KMS key will be created and associated with this stream.
        :param retention_period_hours: The number of hours for the data records that are stored in shards to remain accessible. Default: 24
        :param shard_count: The number of shards for the stream. Default: 1
        :param stream_name: Enforces a particular physical stream name. Default: 

        stability
        :stability: experimental
        """
        props = StreamProps(encryption=encryption, encryption_key=encryption_key, retention_period_hours=retention_period_hours, shard_count=shard_count, stream_name=stream_name)

        jsii.create(Stream, self, [scope, id, props])

    @jsii.member(jsii_name="fromStreamArn")
    @classmethod
    def from_stream_arn(cls, scope: aws_cdk.core.Construct, id: str, stream_arn: str) -> "IStream":
        """
        :param scope: -
        :param id: -
        :param stream_arn: -

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromStreamArn", [scope, id, stream_arn])

    @jsii.member(jsii_name="fromStreamAttributes")
    @classmethod
    def from_stream_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, stream_arn: str, encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None) -> "IStream":
        """Creates a Stream construct that represents an external stream.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param attrs: Stream import properties.
        :param stream_arn: The ARN of the stream.
        :param encryption_key: The KMS key securing the contents of the stream if encryption is enabled.

        stability
        :stability: experimental
        """
        attrs = StreamAttributes(stream_arn=stream_arn, encryption_key=encryption_key)

        return jsii.sinvoke(cls, "fromStreamAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant write permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to ues the key to decrypt the
        contents of the stream will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @jsii.member(jsii_name="grantReadWrite")
    def grant_read_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants read/write permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to use the key for
        encrypt/decrypt will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantReadWrite", [grantee])

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant read permissions for this stream and its contents to an IAM principal (Role/Group/User).

        If an encryption key is used, permission to ues the key to decrypt the
        contents of the stream will also be granted.

        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantWrite", [grantee])

    @property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> str:
        """The ARN of the stream.

        stability
        :stability: experimental
        """
        return jsii.get(self, "streamArn")

    @property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> str:
        """The name of the stream.

        stability
        :stability: experimental
        """
        return jsii.get(self, "streamName")

    @property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """Optional KMS encryption key associated with this stream.

        stability
        :stability: experimental
        """
        return jsii.get(self, "encryptionKey")


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesis.StreamAttributes", jsii_struct_bases=[], name_mapping={'stream_arn': 'streamArn', 'encryption_key': 'encryptionKey'})
class StreamAttributes():
    def __init__(self, *, stream_arn: str, encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None):
        """A reference to a stream.

        The easiest way to instantiate is to call
        ``stream.export()``. Then, the consumer can use ``Stream.import(this, ref)`` and
        get a ``Stream``.

        :param stream_arn: The ARN of the stream.
        :param encryption_key: The KMS key securing the contents of the stream if encryption is enabled.

        stability
        :stability: experimental
        """
        self._values = {
            'stream_arn': stream_arn,
        }
        if encryption_key is not None: self._values["encryption_key"] = encryption_key

    @property
    def stream_arn(self) -> str:
        """The ARN of the stream.

        stability
        :stability: experimental
        """
        return self._values.get('stream_arn')

    @property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """The KMS key securing the contents of the stream if encryption is enabled.

        stability
        :stability: experimental
        """
        return self._values.get('encryption_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StreamAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-kinesis.StreamEncryption")
class StreamEncryption(enum.Enum):
    """What kind of server-side encryption to apply to this stream.

    stability
    :stability: experimental
    """
    UNENCRYPTED = "UNENCRYPTED"
    """Records in the stream are not encrypted.

    stability
    :stability: experimental
    """
    KMS = "KMS"
    """Server-side encryption with a KMS key managed by the user. If ``encryptionKey`` is specified, this key will be used, otherwise, one will be defined.

    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-kinesis.StreamProps", jsii_struct_bases=[], name_mapping={'encryption': 'encryption', 'encryption_key': 'encryptionKey', 'retention_period_hours': 'retentionPeriodHours', 'shard_count': 'shardCount', 'stream_name': 'streamName'})
class StreamProps():
    def __init__(self, *, encryption: typing.Optional["StreamEncryption"]=None, encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None, retention_period_hours: typing.Optional[jsii.Number]=None, shard_count: typing.Optional[jsii.Number]=None, stream_name: typing.Optional[str]=None):
        """
        :param encryption: The kind of server-side encryption to apply to this stream. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryption key is not specified, a key will automatically be created. Default: Unencrypted
        :param encryption_key: External KMS key to use for stream encryption. The 'encryption' property must be set to "Kms". Default: If encryption is set to "Kms" and this property is undefined, a new KMS key will be created and associated with this stream.
        :param retention_period_hours: The number of hours for the data records that are stored in shards to remain accessible. Default: 24
        :param shard_count: The number of shards for the stream. Default: 1
        :param stream_name: Enforces a particular physical stream name. Default: 

        stability
        :stability: experimental
        """
        self._values = {
        }
        if encryption is not None: self._values["encryption"] = encryption
        if encryption_key is not None: self._values["encryption_key"] = encryption_key
        if retention_period_hours is not None: self._values["retention_period_hours"] = retention_period_hours
        if shard_count is not None: self._values["shard_count"] = shard_count
        if stream_name is not None: self._values["stream_name"] = stream_name

    @property
    def encryption(self) -> typing.Optional["StreamEncryption"]:
        """The kind of server-side encryption to apply to this stream.

        If you choose KMS, you can specify a KMS key via ``encryptionKey``. If
        encryption key is not specified, a key will automatically be created.

        default
        :default: Unencrypted

        stability
        :stability: experimental
        """
        return self._values.get('encryption')

    @property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """External KMS key to use for stream encryption.

        The 'encryption' property must be set to "Kms".

        default
        :default:

        If encryption is set to "Kms" and this property is undefined, a
        new KMS key will be created and associated with this stream.

        stability
        :stability: experimental
        """
        return self._values.get('encryption_key')

    @property
    def retention_period_hours(self) -> typing.Optional[jsii.Number]:
        """The number of hours for the data records that are stored in shards to remain accessible.

        default
        :default: 24

        stability
        :stability: experimental
        """
        return self._values.get('retention_period_hours')

    @property
    def shard_count(self) -> typing.Optional[jsii.Number]:
        """The number of shards for the stream.

        default
        :default: 1

        stability
        :stability: experimental
        """
        return self._values.get('shard_count')

    @property
    def stream_name(self) -> typing.Optional[str]:
        """Enforces a particular physical stream name.

        default
        :default: 

        stability
        :stability: experimental
        """
        return self._values.get('stream_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StreamProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnStream", "CfnStreamConsumer", "CfnStreamConsumerProps", "CfnStreamProps", "IStream", "Stream", "StreamAttributes", "StreamEncryption", "StreamProps", "__jsii_assembly__"]

publication.publish()
