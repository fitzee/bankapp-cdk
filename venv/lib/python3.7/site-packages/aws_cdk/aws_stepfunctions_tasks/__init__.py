import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.assets
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_ec2
import aws_cdk.aws_ecr
import aws_cdk.aws_ecr_assets
import aws_cdk.aws_ecs
import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import aws_cdk.aws_stepfunctions
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-stepfunctions-tasks", "1.7.0", __name__, "aws-stepfunctions-tasks@1.7.0.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.AlgorithmSpecification", jsii_struct_bases=[], name_mapping={'algorithm_name': 'algorithmName', 'metric_definitions': 'metricDefinitions', 'training_image': 'trainingImage', 'training_input_mode': 'trainingInputMode'})
class AlgorithmSpecification():
    def __init__(self, *, algorithm_name: typing.Optional[str]=None, metric_definitions: typing.Optional[typing.List["MetricDefinition"]]=None, training_image: typing.Optional["DockerImage"]=None, training_input_mode: typing.Optional["InputMode"]=None):
        """
        :param algorithm_name: Name of the algorithm resource to use for the training job.
        :param metric_definitions: List of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs.
        :param training_image: Registry path of the Docker image that contains the training algorithm.
        :param training_input_mode: Input mode that the algorithm supports. Default: is 'File' mode

        stability
        :stability: experimental
        """
        self._values = {
        }
        if algorithm_name is not None: self._values["algorithm_name"] = algorithm_name
        if metric_definitions is not None: self._values["metric_definitions"] = metric_definitions
        if training_image is not None: self._values["training_image"] = training_image
        if training_input_mode is not None: self._values["training_input_mode"] = training_input_mode

    @property
    def algorithm_name(self) -> typing.Optional[str]:
        """Name of the algorithm resource to use for the training job.

        stability
        :stability: experimental
        """
        return self._values.get('algorithm_name')

    @property
    def metric_definitions(self) -> typing.Optional[typing.List["MetricDefinition"]]:
        """List of metric definition objects.

        Each object specifies the metric name and regular expressions used to parse algorithm logs.

        stability
        :stability: experimental
        """
        return self._values.get('metric_definitions')

    @property
    def training_image(self) -> typing.Optional["DockerImage"]:
        """Registry path of the Docker image that contains the training algorithm.

        stability
        :stability: experimental
        """
        return self._values.get('training_image')

    @property
    def training_input_mode(self) -> typing.Optional["InputMode"]:
        """Input mode that the algorithm supports.

        default
        :default: is 'File' mode

        stability
        :stability: experimental
        """
        return self._values.get('training_input_mode')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AlgorithmSpecification(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.AssembleWith")
class AssembleWith(enum.Enum):
    """How to assemble the results of the transform job as a single S3 object.

    stability
    :stability: experimental
    """
    NONE = "NONE"
    """Concatenate the results in binary format.

    stability
    :stability: experimental
    """
    LINE = "LINE"
    """Add a newline character at the end of every transformed record.

    stability
    :stability: experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.BatchStrategy")
class BatchStrategy(enum.Enum):
    """Specifies the number of records to include in a mini-batch for an HTTP inference request.

    stability
    :stability: experimental
    """
    MULTI_RECORD = "MULTI_RECORD"
    """Fits multiple records in a mini-batch.

    stability
    :stability: experimental
    """
    SINGLE_RECORD = "SINGLE_RECORD"
    """Use a single record when making an invocation request.

    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.Channel", jsii_struct_bases=[], name_mapping={'channel_name': 'channelName', 'data_source': 'dataSource', 'compression_type': 'compressionType', 'content_type': 'contentType', 'input_mode': 'inputMode', 'record_wrapper_type': 'recordWrapperType', 'shuffle_config': 'shuffleConfig'})
class Channel():
    def __init__(self, *, channel_name: str, data_source: "DataSource", compression_type: typing.Optional["CompressionType"]=None, content_type: typing.Optional[str]=None, input_mode: typing.Optional["InputMode"]=None, record_wrapper_type: typing.Optional["RecordWrapperType"]=None, shuffle_config: typing.Optional["ShuffleConfig"]=None):
        """Describes the training, validation or test dataset and the Amazon S3 location where it is stored.

        :param channel_name: Name of the channel.
        :param data_source: Location of the data channel.
        :param compression_type: Compression type if training data is compressed.
        :param content_type: Content type.
        :param input_mode: Input mode to use for the data channel in a training job.
        :param record_wrapper_type: Record wrapper type.
        :param shuffle_config: Shuffle config option for input data in a channel.

        stability
        :stability: experimental
        """
        self._values = {
            'channel_name': channel_name,
            'data_source': data_source,
        }
        if compression_type is not None: self._values["compression_type"] = compression_type
        if content_type is not None: self._values["content_type"] = content_type
        if input_mode is not None: self._values["input_mode"] = input_mode
        if record_wrapper_type is not None: self._values["record_wrapper_type"] = record_wrapper_type
        if shuffle_config is not None: self._values["shuffle_config"] = shuffle_config

    @property
    def channel_name(self) -> str:
        """Name of the channel.

        stability
        :stability: experimental
        """
        return self._values.get('channel_name')

    @property
    def data_source(self) -> "DataSource":
        """Location of the data channel.

        stability
        :stability: experimental
        """
        return self._values.get('data_source')

    @property
    def compression_type(self) -> typing.Optional["CompressionType"]:
        """Compression type if training data is compressed.

        stability
        :stability: experimental
        """
        return self._values.get('compression_type')

    @property
    def content_type(self) -> typing.Optional[str]:
        """Content type.

        stability
        :stability: experimental
        """
        return self._values.get('content_type')

    @property
    def input_mode(self) -> typing.Optional["InputMode"]:
        """Input mode to use for the data channel in a training job.

        stability
        :stability: experimental
        """
        return self._values.get('input_mode')

    @property
    def record_wrapper_type(self) -> typing.Optional["RecordWrapperType"]:
        """Record wrapper type.

        stability
        :stability: experimental
        """
        return self._values.get('record_wrapper_type')

    @property
    def shuffle_config(self) -> typing.Optional["ShuffleConfig"]:
        """Shuffle config option for input data in a channel.

        stability
        :stability: experimental
        """
        return self._values.get('shuffle_config')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Channel(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.CommonEcsRunTaskProps", jsii_struct_bases=[], name_mapping={'cluster': 'cluster', 'task_definition': 'taskDefinition', 'container_overrides': 'containerOverrides', 'integration_pattern': 'integrationPattern'})
class CommonEcsRunTaskProps():
    def __init__(self, *, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None):
        """Basic properties for ECS Tasks.

        :param cluster: The topic to run the task on.
        :param task_definition: Task Definition used for running tasks in the service. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param integration_pattern: The service integration pattern indicates different ways to call RunTask in ECS. The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        self._values = {
            'cluster': cluster,
            'task_definition': task_definition,
        }
        if container_overrides is not None: self._values["container_overrides"] = container_overrides
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern

    @property
    def cluster(self) -> aws_cdk.aws_ecs.ICluster:
        """The topic to run the task on.

        stability
        :stability: experimental
        """
        return self._values.get('cluster')

    @property
    def task_definition(self) -> aws_cdk.aws_ecs.TaskDefinition:
        """Task Definition used for running tasks in the service.

        Note: this must be TaskDefinition, and not ITaskDefinition,
        as it requires properties that are not known for imported task definitions

        stability
        :stability: experimental
        """
        return self._values.get('task_definition')

    @property
    def container_overrides(self) -> typing.Optional[typing.List["ContainerOverride"]]:
        """Container setting overrides.

        Key is the name of the container to override, value is the
        values you want to override.

        stability
        :stability: experimental
        """
        return self._values.get('container_overrides')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call RunTask in ECS.

        The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CommonEcsRunTaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.CompressionType")
class CompressionType(enum.Enum):
    """Compression type of the data.

    stability
    :stability: experimental
    """
    NONE = "NONE"
    """None compression type.

    stability
    :stability: experimental
    """
    GZIP = "GZIP"
    """Gzip compression type.

    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.ContainerOverride", jsii_struct_bases=[], name_mapping={'container_name': 'containerName', 'command': 'command', 'cpu': 'cpu', 'environment': 'environment', 'memory_limit': 'memoryLimit', 'memory_reservation': 'memoryReservation'})
class ContainerOverride():
    def __init__(self, *, container_name: str, command: typing.Optional[typing.List[str]]=None, cpu: typing.Optional[jsii.Number]=None, environment: typing.Optional[typing.List["TaskEnvironmentVariable"]]=None, memory_limit: typing.Optional[jsii.Number]=None, memory_reservation: typing.Optional[jsii.Number]=None):
        """
        :param container_name: Name of the container inside the task definition.
        :param command: Command to run inside the container. Default: Default command
        :param cpu: The number of cpu units reserved for the container.
        :param environment: Variables to set in the container's environment.
        :param memory_limit: Hard memory limit on the container.
        :param memory_reservation: Soft memory limit on the container.

        stability
        :stability: experimental
        """
        self._values = {
            'container_name': container_name,
        }
        if command is not None: self._values["command"] = command
        if cpu is not None: self._values["cpu"] = cpu
        if environment is not None: self._values["environment"] = environment
        if memory_limit is not None: self._values["memory_limit"] = memory_limit
        if memory_reservation is not None: self._values["memory_reservation"] = memory_reservation

    @property
    def container_name(self) -> str:
        """Name of the container inside the task definition.

        stability
        :stability: experimental
        """
        return self._values.get('container_name')

    @property
    def command(self) -> typing.Optional[typing.List[str]]:
        """Command to run inside the container.

        default
        :default: Default command

        stability
        :stability: experimental
        """
        return self._values.get('command')

    @property
    def cpu(self) -> typing.Optional[jsii.Number]:
        """The number of cpu units reserved for the container.

        stability
        :stability: experimental
        Default:
        :Default:: The default value from the task definition.
        """
        return self._values.get('cpu')

    @property
    def environment(self) -> typing.Optional[typing.List["TaskEnvironmentVariable"]]:
        """Variables to set in the container's environment.

        stability
        :stability: experimental
        """
        return self._values.get('environment')

    @property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        """Hard memory limit on the container.

        stability
        :stability: experimental
        Default:
        :Default:: The default value from the task definition.
        """
        return self._values.get('memory_limit')

    @property
    def memory_reservation(self) -> typing.Optional[jsii.Number]:
        """Soft memory limit on the container.

        stability
        :stability: experimental
        Default:
        :Default:: The default value from the task definition.
        """
        return self._values.get('memory_reservation')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ContainerOverride(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.DataSource", jsii_struct_bases=[], name_mapping={'s3_data_source': 's3DataSource'})
class DataSource():
    def __init__(self, *, s3_data_source: "S3DataSource"):
        """Location of the channel data.

        :param s3_data_source: S3 location of the data source that is associated with a channel.

        stability
        :stability: experimental
        """
        self._values = {
            's3_data_source': s3_data_source,
        }

    @property
    def s3_data_source(self) -> "S3DataSource":
        """S3 location of the data source that is associated with a channel.

        stability
        :stability: experimental
        """
        return self._values.get('s3_data_source')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DataSource(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class DockerImage(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-stepfunctions-tasks.DockerImage"):
    """Creates ``IDockerImage`` instances.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _DockerImageProxy

    def __init__(self) -> None:
        jsii.create(DockerImage, self, [])

    @jsii.member(jsii_name="fromAsset")
    @classmethod
    def from_asset(cls, scope: aws_cdk.core.Construct, id: str, *, directory: str, build_args: typing.Optional[typing.Mapping[str,str]]=None, repository_name: typing.Optional[str]=None, exclude: typing.Optional[typing.List[str]]=None, follow: typing.Optional[aws_cdk.assets.FollowMode]=None) -> "DockerImage":
        """Reference a Docker image that is provided as an Asset in the current app.

        :param scope: the scope in which to create the Asset.
        :param id: the ID for the asset in the construct tree.
        :param props: the configuration props of the asset.
        :param directory: The directory where the Dockerfile is stored.
        :param build_args: Build args to pass to the ``docker build`` command. Default: no build args are passed
        :param repository_name: ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: automatically derived from the asset's ID.
        :param exclude: Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: Never

        stability
        :stability: experimental
        """
        props = aws_cdk.aws_ecr_assets.DockerImageAssetProps(directory=directory, build_args=build_args, repository_name=repository_name, exclude=exclude, follow=follow)

        return jsii.sinvoke(cls, "fromAsset", [scope, id, props])

    @jsii.member(jsii_name="fromEcrRepository")
    @classmethod
    def from_ecr_repository(cls, repository: aws_cdk.aws_ecr.IRepository, tag: typing.Optional[str]=None) -> "DockerImage":
        """Reference a Docker image stored in an ECR repository.

        :param repository: the ECR repository where the image is hosted.
        :param tag: an optional ``tag``.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromEcrRepository", [repository, tag])

    @jsii.member(jsii_name="fromJsonExpression")
    @classmethod
    def from_json_expression(cls, expression: str, allow_any_ecr_image_pull: typing.Optional[bool]=None) -> "DockerImage":
        """Reference a Docker image which URI is obtained from the task's input.

        :param expression: the JSON path expression with the task input.
        :param allow_any_ecr_image_pull: whether ECR access should be permitted (set to ``false`` if the image will never be in ECR).

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromJsonExpression", [expression, allow_any_ecr_image_pull])

    @jsii.member(jsii_name="fromRegistry")
    @classmethod
    def from_registry(cls, image_uri: str) -> "DockerImage":
        """Reference a Docker image by it's URI.

        When referencing ECR images, prefer using ``inEcr``.

        :param image_uri: the URI to the docker image.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromRegistry", [image_uri])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, task: "ISageMakerTask") -> "DockerImageConfig":
        """Called when the image is used by a SageMaker task.

        :param task: -

        stability
        :stability: experimental
        """
        ...


class _DockerImageProxy(DockerImage):
    @jsii.member(jsii_name="bind")
    def bind(self, task: "ISageMakerTask") -> "DockerImageConfig":
        """Called when the image is used by a SageMaker task.

        :param task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [task])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.DockerImageConfig", jsii_struct_bases=[], name_mapping={'image_uri': 'imageUri'})
class DockerImageConfig():
    def __init__(self, *, image_uri: str):
        """Configuration for a using Docker image.

        :param image_uri: The fully qualified URI of the Docker image.

        stability
        :stability: experimental
        """
        self._values = {
            'image_uri': image_uri,
        }

    @property
    def image_uri(self) -> str:
        """The fully qualified URI of the Docker image.

        stability
        :stability: experimental
        """
        return self._values.get('image_uri')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DockerImageConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_ec2.IConnectable, aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class EcsRunTaskBase(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.EcsRunTaskBase"):
    """A StepFunctions Task to run a Task on ECS or Fargate.

    stability
    :stability: experimental
    """
    def __init__(self, *, parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None) -> None:
        """
        :param props: -
        :param parameters: Additional parameters to pass to the base task.
        :param cluster: The topic to run the task on.
        :param task_definition: Task Definition used for running tasks in the service. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param integration_pattern: The service integration pattern indicates different ways to call RunTask in ECS. The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        props = EcsRunTaskBaseProps(parameters=parameters, cluster=cluster, task_definition=task_definition, container_overrides=container_overrides, integration_pattern=integration_pattern)

        jsii.create(EcsRunTaskBase, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [task])

    @jsii.member(jsii_name="configureAwsVpcNetworking")
    def _configure_aws_vpc_networking(self, vpc: aws_cdk.aws_ec2.IVpc, assign_public_ip: typing.Optional[bool]=None, subnet_selection: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None) -> None:
        """
        :param vpc: -
        :param assign_public_ip: -
        :param subnet_selection: -
        :param security_group: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "configureAwsVpcNetworking", [vpc, assign_public_ip, subnet_selection, security_group])

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        """Manage allowed network traffic for this service.

        stability
        :stability: experimental
        """
        return jsii.get(self, "connections")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.EcsRunTaskBaseProps", jsii_struct_bases=[CommonEcsRunTaskProps], name_mapping={'cluster': 'cluster', 'task_definition': 'taskDefinition', 'container_overrides': 'containerOverrides', 'integration_pattern': 'integrationPattern', 'parameters': 'parameters'})
class EcsRunTaskBaseProps(CommonEcsRunTaskProps):
    def __init__(self, *, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None):
        """Construction properties for the BaseRunTaskProps.

        :param cluster: The topic to run the task on.
        :param task_definition: Task Definition used for running tasks in the service. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param integration_pattern: The service integration pattern indicates different ways to call RunTask in ECS. The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET
        :param parameters: Additional parameters to pass to the base task.

        stability
        :stability: experimental
        """
        self._values = {
            'cluster': cluster,
            'task_definition': task_definition,
        }
        if container_overrides is not None: self._values["container_overrides"] = container_overrides
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if parameters is not None: self._values["parameters"] = parameters

    @property
    def cluster(self) -> aws_cdk.aws_ecs.ICluster:
        """The topic to run the task on.

        stability
        :stability: experimental
        """
        return self._values.get('cluster')

    @property
    def task_definition(self) -> aws_cdk.aws_ecs.TaskDefinition:
        """Task Definition used for running tasks in the service.

        Note: this must be TaskDefinition, and not ITaskDefinition,
        as it requires properties that are not known for imported task definitions

        stability
        :stability: experimental
        """
        return self._values.get('task_definition')

    @property
    def container_overrides(self) -> typing.Optional[typing.List["ContainerOverride"]]:
        """Container setting overrides.

        Key is the name of the container to override, value is the
        values you want to override.

        stability
        :stability: experimental
        """
        return self._values.get('container_overrides')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call RunTask in ECS.

        The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def parameters(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """Additional parameters to pass to the base task.

        stability
        :stability: experimental
        """
        return self._values.get('parameters')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'EcsRunTaskBaseProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-stepfunctions-tasks.ISageMakerTask")
class ISageMakerTask(aws_cdk.aws_stepfunctions.IStepFunctionsTask, aws_cdk.aws_iam.IGrantable, jsii.compat.Protocol):
    """
    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ISageMakerTaskProxy

    pass

class _ISageMakerTaskProxy(jsii.proxy_for(aws_cdk.aws_stepfunctions.IStepFunctionsTask), jsii.proxy_for(aws_cdk.aws_iam.IGrantable)):
    """
    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-stepfunctions-tasks.ISageMakerTask"
    pass

@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.InputMode")
class InputMode(enum.Enum):
    """Input mode that the algorithm supports.

    stability
    :stability: experimental
    """
    PIPE = "PIPE"
    """Pipe mode.

    stability
    :stability: experimental
    """
    FILE = "FILE"
    """File mode.

    stability
    :stability: experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.InvocationType")
class InvocationType(enum.Enum):
    """Invocation type of a Lambda.

    stability
    :stability: experimental
    """
    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    """Invoke synchronously.

    The API response includes the function response and additional data.

    stability
    :stability: experimental
    """
    EVENT = "EVENT"
    """Invoke asynchronously.

    Send events that fail multiple times to the function's dead-letter queue (if it's configured).
    The API response only includes a status code.

    stability
    :stability: experimental
    """
    DRY_RUN = "DRY_RUN"
    """TValidate parameter values and verify that the user or role has permission to invoke the function.

    stability
    :stability: experimental
    """

@jsii.implements(aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class InvokeActivity(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.InvokeActivity"):
    """A Step Functions Task to invoke an Activity worker.

    An Activity can be used directly as a Resource.

    stability
    :stability: experimental
    """
    def __init__(self, activity: aws_cdk.aws_stepfunctions.IActivity, *, heartbeat: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        :param activity: -
        :param props: -
        :param heartbeat: Maximum time between heart beats. If the time between heart beats takes longer than this, a 'Timeout' error is raised. Default: No heart beat timeout

        stability
        :stability: experimental
        """
        props = InvokeActivityProps(heartbeat=heartbeat)

        jsii.create(InvokeActivity, self, [activity, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param _task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_task])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.InvokeActivityProps", jsii_struct_bases=[], name_mapping={'heartbeat': 'heartbeat'})
class InvokeActivityProps():
    def __init__(self, *, heartbeat: typing.Optional[aws_cdk.core.Duration]=None):
        """Properties for FunctionTask.

        :param heartbeat: Maximum time between heart beats. If the time between heart beats takes longer than this, a 'Timeout' error is raised. Default: No heart beat timeout

        stability
        :stability: experimental
        """
        self._values = {
        }
        if heartbeat is not None: self._values["heartbeat"] = heartbeat

    @property
    def heartbeat(self) -> typing.Optional[aws_cdk.core.Duration]:
        """Maximum time between heart beats.

        If the time between heart beats takes longer than this, a 'Timeout' error is raised.

        default
        :default: No heart beat timeout

        stability
        :stability: experimental
        """
        return self._values.get('heartbeat')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'InvokeActivityProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class InvokeFunction(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.InvokeFunction"):
    """A Step Functions Task to invoke a Lambda function.

    The Lambda function Arn is defined as Resource in the state machine definition.

    OUTPUT: the output of this task is the return value of the Lambda Function.

    stability
    :stability: experimental
    """
    def __init__(self, lambda_function: aws_cdk.aws_lambda.IFunction, *, payload: typing.Optional[typing.Mapping[str,typing.Any]]=None) -> None:
        """
        :param lambda_function: -
        :param props: -
        :param payload: The JSON that you want to provide to your Lambda function as input. This parameter is named as payload to keep consistent with RunLambdaTask class. Default: - The JSON data indicated by the task's InputPath is used as payload

        stability
        :stability: experimental
        """
        props = InvokeFunctionProps(payload=payload)

        jsii.create(InvokeFunction, self, [lambda_function, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param _task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_task])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.InvokeFunctionProps", jsii_struct_bases=[], name_mapping={'payload': 'payload'})
class InvokeFunctionProps():
    def __init__(self, *, payload: typing.Optional[typing.Mapping[str,typing.Any]]=None):
        """Properties for InvokeFunction.

        :param payload: The JSON that you want to provide to your Lambda function as input. This parameter is named as payload to keep consistent with RunLambdaTask class. Default: - The JSON data indicated by the task's InputPath is used as payload

        stability
        :stability: experimental
        """
        self._values = {
        }
        if payload is not None: self._values["payload"] = payload

    @property
    def payload(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """The JSON that you want to provide to your Lambda function as input.

        This parameter is named as payload to keep consistent with RunLambdaTask class.

        default
        :default: - The JSON data indicated by the task's InputPath is used as payload

        stability
        :stability: experimental
        """
        return self._values.get('payload')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'InvokeFunctionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.MetricDefinition", jsii_struct_bases=[], name_mapping={'name': 'name', 'regex': 'regex'})
class MetricDefinition():
    def __init__(self, *, name: str, regex: str):
        """Specifies the metric name and regular expressions used to parse algorithm logs.

        :param name: Name of the metric.
        :param regex: Regular expression that searches the output of a training job and gets the value of the metric.

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
            'regex': regex,
        }

    @property
    def name(self) -> str:
        """Name of the metric.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @property
    def regex(self) -> str:
        """Regular expression that searches the output of a training job and gets the value of the metric.

        stability
        :stability: experimental
        """
        return self._values.get('regex')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MetricDefinition(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.OutputDataConfig", jsii_struct_bases=[], name_mapping={'s3_output_location': 's3OutputLocation', 'encryption_key': 'encryptionKey'})
class OutputDataConfig():
    def __init__(self, *, s3_output_location: "S3Location", encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None):
        """
        :param s3_output_location: Identifies the S3 path where you want Amazon SageMaker to store the model artifacts.
        :param encryption_key: Optional KMS encryption key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

        stability
        :stability: experimental
        """
        self._values = {
            's3_output_location': s3_output_location,
        }
        if encryption_key is not None: self._values["encryption_key"] = encryption_key

    @property
    def s3_output_location(self) -> "S3Location":
        """Identifies the S3 path where you want Amazon SageMaker to store the model artifacts.

        stability
        :stability: experimental
        """
        return self._values.get('s3_output_location')

    @property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """Optional KMS encryption key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

        stability
        :stability: experimental
        """
        return self._values.get('encryption_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'OutputDataConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class PublishToTopic(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.PublishToTopic"):
    """A Step Functions Task to publish messages to SNS topic.

    A Function can be used directly as a Resource, but this class mirrors
    integration with other AWS services via a specific class instance.

    stability
    :stability: experimental
    """
    def __init__(self, topic: aws_cdk.aws_sns.ITopic, *, message: aws_cdk.aws_stepfunctions.TaskInput, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, message_per_subscription_type: typing.Optional[bool]=None, subject: typing.Optional[str]=None) -> None:
        """
        :param topic: -
        :param props: -
        :param message: The text message to send to the topic.
        :param integration_pattern: The service integration pattern indicates different ways to call Publish to SNS. The valid value is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET
        :param message_per_subscription_type: If true, send a different message to every subscription type. If this is set to true, message must be a JSON object with a "default" key and a key for every subscription type (such as "sqs", "email", etc.) The values are strings representing the messages being sent to every subscription type.
        :param subject: Message subject.

        stability
        :stability: experimental
        """
        props = PublishToTopicProps(message=message, integration_pattern=integration_pattern, message_per_subscription_type=message_per_subscription_type, subject=subject)

        jsii.create(PublishToTopic, self, [topic, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param _task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_task])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.PublishToTopicProps", jsii_struct_bases=[], name_mapping={'message': 'message', 'integration_pattern': 'integrationPattern', 'message_per_subscription_type': 'messagePerSubscriptionType', 'subject': 'subject'})
class PublishToTopicProps():
    def __init__(self, *, message: aws_cdk.aws_stepfunctions.TaskInput, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, message_per_subscription_type: typing.Optional[bool]=None, subject: typing.Optional[str]=None):
        """Properties for PublishTask.

        :param message: The text message to send to the topic.
        :param integration_pattern: The service integration pattern indicates different ways to call Publish to SNS. The valid value is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET
        :param message_per_subscription_type: If true, send a different message to every subscription type. If this is set to true, message must be a JSON object with a "default" key and a key for every subscription type (such as "sqs", "email", etc.) The values are strings representing the messages being sent to every subscription type.
        :param subject: Message subject.

        stability
        :stability: experimental
        """
        self._values = {
            'message': message,
        }
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if message_per_subscription_type is not None: self._values["message_per_subscription_type"] = message_per_subscription_type
        if subject is not None: self._values["subject"] = subject

    @property
    def message(self) -> aws_cdk.aws_stepfunctions.TaskInput:
        """The text message to send to the topic.

        stability
        :stability: experimental
        """
        return self._values.get('message')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call Publish to SNS.

        The valid value is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def message_per_subscription_type(self) -> typing.Optional[bool]:
        """If true, send a different message to every subscription type.

        If this is set to true, message must be a JSON object with a
        "default" key and a key for every subscription type (such as "sqs",
        "email", etc.) The values are strings representing the messages
        being sent to every subscription type.

        see
        :see: https://docs.aws.amazon.com/sns/latest/api/API_Publish.html#API_Publish_RequestParameters
        stability
        :stability: experimental
        """
        return self._values.get('message_per_subscription_type')

    @property
    def subject(self) -> typing.Optional[str]:
        """Message subject.

        stability
        :stability: experimental
        """
        return self._values.get('subject')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PublishToTopicProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.RecordWrapperType")
class RecordWrapperType(enum.Enum):
    """Define the format of the input data.

    stability
    :stability: experimental
    """
    NONE = "NONE"
    """None record wrapper type.

    stability
    :stability: experimental
    """
    RECORD_IO = "RECORD_IO"
    """RecordIO record wrapper type.

    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.ResourceConfig", jsii_struct_bases=[], name_mapping={'instance_count': 'instanceCount', 'instance_type': 'instanceType', 'volume_size_in_gb': 'volumeSizeInGB', 'volume_encryption_key': 'volumeEncryptionKey'})
class ResourceConfig():
    def __init__(self, *, instance_count: jsii.Number, instance_type: aws_cdk.aws_ec2.InstanceType, volume_size_in_gb: jsii.Number, volume_encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None):
        """
        :param instance_count: The number of ML compute instances to use. Default: 1 instance.
        :param instance_type: ML compute instance type. Default: is the 'm4.xlarge' instance type.
        :param volume_size_in_gb: Size of the ML storage volume that you want to provision. Default: 10 GB EBS volume.
        :param volume_encryption_key: KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.

        stability
        :stability: experimental
        """
        self._values = {
            'instance_count': instance_count,
            'instance_type': instance_type,
            'volume_size_in_gb': volume_size_in_gb,
        }
        if volume_encryption_key is not None: self._values["volume_encryption_key"] = volume_encryption_key

    @property
    def instance_count(self) -> jsii.Number:
        """The number of ML compute instances to use.

        default
        :default: 1 instance.

        stability
        :stability: experimental
        """
        return self._values.get('instance_count')

    @property
    def instance_type(self) -> aws_cdk.aws_ec2.InstanceType:
        """ML compute instance type.

        default
        :default: is the 'm4.xlarge' instance type.

        stability
        :stability: experimental
        """
        return self._values.get('instance_type')

    @property
    def volume_size_in_gb(self) -> jsii.Number:
        """Size of the ML storage volume that you want to provision.

        default
        :default: 10 GB EBS volume.

        stability
        :stability: experimental
        """
        return self._values.get('volume_size_in_gb')

    @property
    def volume_encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.

        stability
        :stability: experimental
        """
        return self._values.get('volume_encryption_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ResourceConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class RunEcsEc2Task(EcsRunTaskBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.RunEcsEc2Task"):
    """Run an ECS/EC2 Task in a StepFunctions workflow.

    stability
    :stability: experimental
    """
    def __init__(self, *, placement_constraints: typing.Optional[typing.List[aws_cdk.aws_ecs.PlacementConstraint]]=None, placement_strategies: typing.Optional[typing.List[aws_cdk.aws_ecs.PlacementStrategy]]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None) -> None:
        """
        :param props: -
        :param placement_constraints: Placement constraints. Default: No constraints
        :param placement_strategies: Placement strategies. Default: No strategies
        :param security_group: Existing security group to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnets: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets
        :param cluster: The topic to run the task on.
        :param task_definition: Task Definition used for running tasks in the service. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param integration_pattern: The service integration pattern indicates different ways to call RunTask in ECS. The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        props = RunEcsEc2TaskProps(placement_constraints=placement_constraints, placement_strategies=placement_strategies, security_group=security_group, subnets=subnets, cluster=cluster, task_definition=task_definition, container_overrides=container_overrides, integration_pattern=integration_pattern)

        jsii.create(RunEcsEc2Task, self, [props])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.RunEcsEc2TaskProps", jsii_struct_bases=[CommonEcsRunTaskProps], name_mapping={'cluster': 'cluster', 'task_definition': 'taskDefinition', 'container_overrides': 'containerOverrides', 'integration_pattern': 'integrationPattern', 'placement_constraints': 'placementConstraints', 'placement_strategies': 'placementStrategies', 'security_group': 'securityGroup', 'subnets': 'subnets'})
class RunEcsEc2TaskProps(CommonEcsRunTaskProps):
    def __init__(self, *, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, placement_constraints: typing.Optional[typing.List[aws_cdk.aws_ecs.PlacementConstraint]]=None, placement_strategies: typing.Optional[typing.List[aws_cdk.aws_ecs.PlacementStrategy]]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None):
        """Properties to run an ECS task on EC2 in StepFunctionsan ECS.

        :param cluster: The topic to run the task on.
        :param task_definition: Task Definition used for running tasks in the service. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param integration_pattern: The service integration pattern indicates different ways to call RunTask in ECS. The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET
        :param placement_constraints: Placement constraints. Default: No constraints
        :param placement_strategies: Placement strategies. Default: No strategies
        :param security_group: Existing security group to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnets: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets

        stability
        :stability: experimental
        """
        self._values = {
            'cluster': cluster,
            'task_definition': task_definition,
        }
        if container_overrides is not None: self._values["container_overrides"] = container_overrides
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if placement_constraints is not None: self._values["placement_constraints"] = placement_constraints
        if placement_strategies is not None: self._values["placement_strategies"] = placement_strategies
        if security_group is not None: self._values["security_group"] = security_group
        if subnets is not None: self._values["subnets"] = subnets

    @property
    def cluster(self) -> aws_cdk.aws_ecs.ICluster:
        """The topic to run the task on.

        stability
        :stability: experimental
        """
        return self._values.get('cluster')

    @property
    def task_definition(self) -> aws_cdk.aws_ecs.TaskDefinition:
        """Task Definition used for running tasks in the service.

        Note: this must be TaskDefinition, and not ITaskDefinition,
        as it requires properties that are not known for imported task definitions

        stability
        :stability: experimental
        """
        return self._values.get('task_definition')

    @property
    def container_overrides(self) -> typing.Optional[typing.List["ContainerOverride"]]:
        """Container setting overrides.

        Key is the name of the container to override, value is the
        values you want to override.

        stability
        :stability: experimental
        """
        return self._values.get('container_overrides')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call RunTask in ECS.

        The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def placement_constraints(self) -> typing.Optional[typing.List[aws_cdk.aws_ecs.PlacementConstraint]]:
        """Placement constraints.

        default
        :default: No constraints

        stability
        :stability: experimental
        """
        return self._values.get('placement_constraints')

    @property
    def placement_strategies(self) -> typing.Optional[typing.List[aws_cdk.aws_ecs.PlacementStrategy]]:
        """Placement strategies.

        default
        :default: No strategies

        stability
        :stability: experimental
        """
        return self._values.get('placement_strategies')

    @property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        """Existing security group to use for the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        default
        :default: A new security group is created

        stability
        :stability: experimental
        """
        return self._values.get('security_group')

    @property
    def subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        """In what subnets to place the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        default
        :default: Private subnets

        stability
        :stability: experimental
        """
        return self._values.get('subnets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RunEcsEc2TaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class RunEcsFargateTask(EcsRunTaskBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.RunEcsFargateTask"):
    """Start a service on an ECS cluster.

    stability
    :stability: experimental
    """
    def __init__(self, *, assign_public_ip: typing.Optional[bool]=None, platform_version: typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None) -> None:
        """
        :param props: -
        :param assign_public_ip: Assign public IP addresses to each task. Default: false
        :param platform_version: Fargate platform version to run this service on. Unless you have specific compatibility requirements, you don't need to specify this. Default: Latest
        :param security_group: Existing security group to use for the tasks. Default: A new security group is created
        :param subnets: In what subnets to place the task's ENIs. Default: Private subnet if assignPublicIp, public subnets otherwise
        :param cluster: The topic to run the task on.
        :param task_definition: Task Definition used for running tasks in the service. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param integration_pattern: The service integration pattern indicates different ways to call RunTask in ECS. The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        props = RunEcsFargateTaskProps(assign_public_ip=assign_public_ip, platform_version=platform_version, security_group=security_group, subnets=subnets, cluster=cluster, task_definition=task_definition, container_overrides=container_overrides, integration_pattern=integration_pattern)

        jsii.create(RunEcsFargateTask, self, [props])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.RunEcsFargateTaskProps", jsii_struct_bases=[CommonEcsRunTaskProps], name_mapping={'cluster': 'cluster', 'task_definition': 'taskDefinition', 'container_overrides': 'containerOverrides', 'integration_pattern': 'integrationPattern', 'assign_public_ip': 'assignPublicIp', 'platform_version': 'platformVersion', 'security_group': 'securityGroup', 'subnets': 'subnets'})
class RunEcsFargateTaskProps(CommonEcsRunTaskProps):
    def __init__(self, *, cluster: aws_cdk.aws_ecs.ICluster, task_definition: aws_cdk.aws_ecs.TaskDefinition, container_overrides: typing.Optional[typing.List["ContainerOverride"]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, assign_public_ip: typing.Optional[bool]=None, platform_version: typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion]=None, security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]=None, subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None):
        """Properties to define an ECS service.

        :param cluster: The topic to run the task on.
        :param task_definition: Task Definition used for running tasks in the service. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param integration_pattern: The service integration pattern indicates different ways to call RunTask in ECS. The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET
        :param assign_public_ip: Assign public IP addresses to each task. Default: false
        :param platform_version: Fargate platform version to run this service on. Unless you have specific compatibility requirements, you don't need to specify this. Default: Latest
        :param security_group: Existing security group to use for the tasks. Default: A new security group is created
        :param subnets: In what subnets to place the task's ENIs. Default: Private subnet if assignPublicIp, public subnets otherwise

        stability
        :stability: experimental
        """
        self._values = {
            'cluster': cluster,
            'task_definition': task_definition,
        }
        if container_overrides is not None: self._values["container_overrides"] = container_overrides
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if assign_public_ip is not None: self._values["assign_public_ip"] = assign_public_ip
        if platform_version is not None: self._values["platform_version"] = platform_version
        if security_group is not None: self._values["security_group"] = security_group
        if subnets is not None: self._values["subnets"] = subnets

    @property
    def cluster(self) -> aws_cdk.aws_ecs.ICluster:
        """The topic to run the task on.

        stability
        :stability: experimental
        """
        return self._values.get('cluster')

    @property
    def task_definition(self) -> aws_cdk.aws_ecs.TaskDefinition:
        """Task Definition used for running tasks in the service.

        Note: this must be TaskDefinition, and not ITaskDefinition,
        as it requires properties that are not known for imported task definitions

        stability
        :stability: experimental
        """
        return self._values.get('task_definition')

    @property
    def container_overrides(self) -> typing.Optional[typing.List["ContainerOverride"]]:
        """Container setting overrides.

        Key is the name of the container to override, value is the
        values you want to override.

        stability
        :stability: experimental
        """
        return self._values.get('container_overrides')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call RunTask in ECS.

        The valid value for Lambda is FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def assign_public_ip(self) -> typing.Optional[bool]:
        """Assign public IP addresses to each task.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('assign_public_ip')

    @property
    def platform_version(self) -> typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion]:
        """Fargate platform version to run this service on.

        Unless you have specific compatibility requirements, you don't need to
        specify this.

        default
        :default: Latest

        stability
        :stability: experimental
        """
        return self._values.get('platform_version')

    @property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        """Existing security group to use for the tasks.

        default
        :default: A new security group is created

        stability
        :stability: experimental
        """
        return self._values.get('security_group')

    @property
    def subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        """In what subnets to place the task's ENIs.

        default
        :default: Private subnet if assignPublicIp, public subnets otherwise

        stability
        :stability: experimental
        """
        return self._values.get('subnets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RunEcsFargateTaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class RunLambdaTask(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.RunLambdaTask"):
    """Invoke a Lambda function as a Task.

    OUTPUT: the output of this task is either the return value of Lambda's
    Invoke call, or whatever the Lambda Function posted back using
    ``SendTaskSuccess/SendTaskFailure`` in ``waitForTaskToken`` mode.

    see
    :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html
    stability
    :stability: experimental
    """
    def __init__(self, lambda_function: aws_cdk.aws_lambda.IFunction, *, client_context: typing.Optional[str]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, invocation_type: typing.Optional["InvocationType"]=None, payload: typing.Optional[typing.Mapping[str,typing.Any]]=None, qualifier: typing.Optional[str]=None) -> None:
        """
        :param lambda_function: -
        :param props: -
        :param client_context: Client context to pass to the function. Default: - No context
        :param integration_pattern: The service integration pattern indicates different ways to invoke Lambda function. The valid value for Lambda is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN, it determines whether to pause the workflow until a task token is returned. If this is set to WAIT_FOR_TASK_TOKEN, the Context.taskToken value must be included somewhere in the payload and the Lambda must call ``SendTaskSuccess/SendTaskFailure`` using that token. Default: FIRE_AND_FORGET
        :param invocation_type: Invocation type of the Lambda function. Default: RequestResponse
        :param payload: The JSON that you want to provide to your Lambda function as input.
        :param qualifier: Version or alias of the function to be invoked. Default: - No qualifier

        stability
        :stability: experimental
        """
        props = RunLambdaTaskProps(client_context=client_context, integration_pattern=integration_pattern, invocation_type=invocation_type, payload=payload, qualifier=qualifier)

        jsii.create(RunLambdaTask, self, [lambda_function, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param _task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_task])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.RunLambdaTaskProps", jsii_struct_bases=[], name_mapping={'client_context': 'clientContext', 'integration_pattern': 'integrationPattern', 'invocation_type': 'invocationType', 'payload': 'payload', 'qualifier': 'qualifier'})
class RunLambdaTaskProps():
    def __init__(self, *, client_context: typing.Optional[str]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, invocation_type: typing.Optional["InvocationType"]=None, payload: typing.Optional[typing.Mapping[str,typing.Any]]=None, qualifier: typing.Optional[str]=None):
        """Properties for RunLambdaTask.

        :param client_context: Client context to pass to the function. Default: - No context
        :param integration_pattern: The service integration pattern indicates different ways to invoke Lambda function. The valid value for Lambda is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN, it determines whether to pause the workflow until a task token is returned. If this is set to WAIT_FOR_TASK_TOKEN, the Context.taskToken value must be included somewhere in the payload and the Lambda must call ``SendTaskSuccess/SendTaskFailure`` using that token. Default: FIRE_AND_FORGET
        :param invocation_type: Invocation type of the Lambda function. Default: RequestResponse
        :param payload: The JSON that you want to provide to your Lambda function as input.
        :param qualifier: Version or alias of the function to be invoked. Default: - No qualifier

        stability
        :stability: experimental
        """
        self._values = {
        }
        if client_context is not None: self._values["client_context"] = client_context
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if invocation_type is not None: self._values["invocation_type"] = invocation_type
        if payload is not None: self._values["payload"] = payload
        if qualifier is not None: self._values["qualifier"] = qualifier

    @property
    def client_context(self) -> typing.Optional[str]:
        """Client context to pass to the function.

        default
        :default: - No context

        stability
        :stability: experimental
        """
        return self._values.get('client_context')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to invoke Lambda function.

        The valid value for Lambda is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN,
        it determines whether to pause the workflow until a task token is returned.

        If this is set to WAIT_FOR_TASK_TOKEN, the Context.taskToken value must be included
        somewhere in the payload and the Lambda must call
        ``SendTaskSuccess/SendTaskFailure`` using that token.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def invocation_type(self) -> typing.Optional["InvocationType"]:
        """Invocation type of the Lambda function.

        default
        :default: RequestResponse

        stability
        :stability: experimental
        """
        return self._values.get('invocation_type')

    @property
    def payload(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """The JSON that you want to provide to your Lambda function as input.

        stability
        :stability: experimental
        """
        return self._values.get('payload')

    @property
    def qualifier(self) -> typing.Optional[str]:
        """Version or alias of the function to be invoked.

        default
        :default: - No qualifier

        stability
        :stability: experimental
        """
        return self._values.get('qualifier')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RunLambdaTaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.S3DataDistributionType")
class S3DataDistributionType(enum.Enum):
    """S3 Data Distribution Type.

    stability
    :stability: experimental
    """
    FULLY_REPLICATED = "FULLY_REPLICATED"
    """Fully replicated S3 Data Distribution Type.

    stability
    :stability: experimental
    """
    SHARDED_BY_S3_KEY = "SHARDED_BY_S3_KEY"
    """Sharded By S3 Key Data Distribution Type.

    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.S3DataSource", jsii_struct_bases=[], name_mapping={'s3_location': 's3Location', 'attribute_names': 'attributeNames', 's3_data_distribution_type': 's3DataDistributionType', 's3_data_type': 's3DataType'})
class S3DataSource():
    def __init__(self, *, s3_location: "S3Location", attribute_names: typing.Optional[typing.List[str]]=None, s3_data_distribution_type: typing.Optional["S3DataDistributionType"]=None, s3_data_type: typing.Optional["S3DataType"]=None):
        """S3 location of the channel data.

        :param s3_location: S3 Uri.
        :param attribute_names: List of one or more attribute names to use that are found in a specified augmented manifest file.
        :param s3_data_distribution_type: S3 Data Distribution Type.
        :param s3_data_type: S3 Data Type.

        stability
        :stability: experimental
        """
        self._values = {
            's3_location': s3_location,
        }
        if attribute_names is not None: self._values["attribute_names"] = attribute_names
        if s3_data_distribution_type is not None: self._values["s3_data_distribution_type"] = s3_data_distribution_type
        if s3_data_type is not None: self._values["s3_data_type"] = s3_data_type

    @property
    def s3_location(self) -> "S3Location":
        """S3 Uri.

        stability
        :stability: experimental
        """
        return self._values.get('s3_location')

    @property
    def attribute_names(self) -> typing.Optional[typing.List[str]]:
        """List of one or more attribute names to use that are found in a specified augmented manifest file.

        stability
        :stability: experimental
        """
        return self._values.get('attribute_names')

    @property
    def s3_data_distribution_type(self) -> typing.Optional["S3DataDistributionType"]:
        """S3 Data Distribution Type.

        stability
        :stability: experimental
        """
        return self._values.get('s3_data_distribution_type')

    @property
    def s3_data_type(self) -> typing.Optional["S3DataType"]:
        """S3 Data Type.

        stability
        :stability: experimental
        """
        return self._values.get('s3_data_type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'S3DataSource(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.S3DataType")
class S3DataType(enum.Enum):
    """S3 Data Type.

    stability
    :stability: experimental
    """
    MANIFEST_FILE = "MANIFEST_FILE"
    """Manifest File Data Type.

    stability
    :stability: experimental
    """
    S3_PREFIX = "S3_PREFIX"
    """S3 Prefix Data Type.

    stability
    :stability: experimental
    """
    AUGMENTED_MANIFEST_FILE = "AUGMENTED_MANIFEST_FILE"
    """Augmented Manifest File Data Type.

    stability
    :stability: experimental
    """

class S3Location(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-stepfunctions-tasks.S3Location"):
    """Constructs ``IS3Location`` objects.

    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _S3LocationProxy

    def __init__(self) -> None:
        jsii.create(S3Location, self, [])

    @jsii.member(jsii_name="fromBucket")
    @classmethod
    def from_bucket(cls, bucket: aws_cdk.aws_s3.IBucket, key_prefix: str) -> "S3Location":
        """An ``IS3Location`` built with a determined bucket and key prefix.

        :param bucket: is the bucket where the objects are to be stored.
        :param key_prefix: is the key prefix used by the location.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromBucket", [bucket, key_prefix])

    @jsii.member(jsii_name="fromJsonExpression")
    @classmethod
    def from_json_expression(cls, expression: str) -> "S3Location":
        """An ``IS3Location`` determined fully by a JSON Path from the task input.

        Due to the dynamic nature of those locations, the IAM grants that will be set by ``grantRead`` and ``grantWrite``
        apply to the ``*`` resource.

        :param expression: the JSON expression resolving to an S3 location URI.

        stability
        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromJsonExpression", [expression])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, task: "ISageMakerTask", *, for_reading: typing.Optional[bool]=None, for_writing: typing.Optional[bool]=None) -> "S3LocationConfig":
        """Called when the S3Location is bound to a StepFunctions task.

        :param task: -
        :param opts: -
        :param for_reading: Allow reading from the S3 Location. Default: false
        :param for_writing: Allow writing to the S3 Location. Default: false

        stability
        :stability: experimental
        """
        ...


class _S3LocationProxy(S3Location):
    @jsii.member(jsii_name="bind")
    def bind(self, task: "ISageMakerTask", *, for_reading: typing.Optional[bool]=None, for_writing: typing.Optional[bool]=None) -> "S3LocationConfig":
        """Called when the S3Location is bound to a StepFunctions task.

        :param task: -
        :param opts: -
        :param for_reading: Allow reading from the S3 Location. Default: false
        :param for_writing: Allow writing to the S3 Location. Default: false

        stability
        :stability: experimental
        """
        opts = S3LocationBindOptions(for_reading=for_reading, for_writing=for_writing)

        return jsii.invoke(self, "bind", [task, opts])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.S3LocationBindOptions", jsii_struct_bases=[], name_mapping={'for_reading': 'forReading', 'for_writing': 'forWriting'})
class S3LocationBindOptions():
    def __init__(self, *, for_reading: typing.Optional[bool]=None, for_writing: typing.Optional[bool]=None):
        """Options for binding an S3 Location.

        :param for_reading: Allow reading from the S3 Location. Default: false
        :param for_writing: Allow writing to the S3 Location. Default: false

        stability
        :stability: experimental
        """
        self._values = {
        }
        if for_reading is not None: self._values["for_reading"] = for_reading
        if for_writing is not None: self._values["for_writing"] = for_writing

    @property
    def for_reading(self) -> typing.Optional[bool]:
        """Allow reading from the S3 Location.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('for_reading')

    @property
    def for_writing(self) -> typing.Optional[bool]:
        """Allow writing to the S3 Location.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('for_writing')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'S3LocationBindOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.S3LocationConfig", jsii_struct_bases=[], name_mapping={'uri': 'uri'})
class S3LocationConfig():
    def __init__(self, *, uri: str):
        """
        :param uri: 

        stability
        :stability: experimental
        """
        self._values = {
            'uri': uri,
        }

    @property
    def uri(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('uri')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'S3LocationConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_iam.IGrantable, aws_cdk.aws_ec2.IConnectable, aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class SagemakerTrainTask(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.SagemakerTrainTask"):
    """Class representing the SageMaker Create Training Job task.

    stability
    :stability: experimental
    """
    def __init__(self, *, algorithm_specification: "AlgorithmSpecification", input_data_config: typing.List["Channel"], output_data_config: "OutputDataConfig", training_job_name: str, hyperparameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, resource_config: typing.Optional["ResourceConfig"]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, stopping_condition: typing.Optional["StoppingCondition"]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, vpc_config: typing.Optional["VpcConfig"]=None) -> None:
        """
        :param props: -
        :param algorithm_specification: Identifies the training algorithm to use.
        :param input_data_config: Describes the various datasets (e.g. train, validation, test) and the Amazon S3 location where stored.
        :param output_data_config: Identifies the Amazon S3 location where you want Amazon SageMaker to save the results of model training.
        :param training_job_name: Training Job Name.
        :param hyperparameters: Hyperparameters to be used for the train job.
        :param integration_pattern: The service integration pattern indicates different ways to call SageMaker APIs. The valid value is either FIRE_AND_FORGET or SYNC. Default: FIRE_AND_FORGET
        :param resource_config: Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training.
        :param role: Role for the Training Job. The role must be granted all necessary permissions for the SageMaker training job to be able to operate. See https://docs.aws.amazon.com/fr_fr/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-createtrainingjob-perms Default: - a role with appropriate permissions will be created.
        :param stopping_condition: Sets a time limit for training.
        :param tags: Tags to be applied to the train job.
        :param vpc_config: Specifies the VPC that you want your training job to connect to.

        stability
        :stability: experimental
        """
        props = SagemakerTrainTaskProps(algorithm_specification=algorithm_specification, input_data_config=input_data_config, output_data_config=output_data_config, training_job_name=training_job_name, hyperparameters=hyperparameters, integration_pattern=integration_pattern, resource_config=resource_config, role=role, stopping_condition=stopping_condition, tags=tags, vpc_config=vpc_config)

        jsii.create(SagemakerTrainTask, self, [props])

    @jsii.member(jsii_name="addSecurityGroup")
    def add_security_group(self, security_group: aws_cdk.aws_ec2.ISecurityGroup) -> None:
        """Add the security group to all instances via the launch configuration security groups array.

        :param security_group: : The security group to add.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addSecurityGroup", [security_group])

    @jsii.member(jsii_name="bind")
    def bind(self, task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [task])

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        """Allows specify security group connections for instances of this fleet.

        stability
        :stability: experimental
        """
        return jsii.get(self, "connections")

    @property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        """The principal to grant permissions to.

        stability
        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """The execution role for the Sagemaker training job.

        Only available after task has been added to a state machine.

        stability
        :stability: experimental
        """
        return jsii.get(self, "role")


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.SagemakerTrainTaskProps", jsii_struct_bases=[], name_mapping={'algorithm_specification': 'algorithmSpecification', 'input_data_config': 'inputDataConfig', 'output_data_config': 'outputDataConfig', 'training_job_name': 'trainingJobName', 'hyperparameters': 'hyperparameters', 'integration_pattern': 'integrationPattern', 'resource_config': 'resourceConfig', 'role': 'role', 'stopping_condition': 'stoppingCondition', 'tags': 'tags', 'vpc_config': 'vpcConfig'})
class SagemakerTrainTaskProps():
    def __init__(self, *, algorithm_specification: "AlgorithmSpecification", input_data_config: typing.List["Channel"], output_data_config: "OutputDataConfig", training_job_name: str, hyperparameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, resource_config: typing.Optional["ResourceConfig"]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, stopping_condition: typing.Optional["StoppingCondition"]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, vpc_config: typing.Optional["VpcConfig"]=None):
        """
        :param algorithm_specification: Identifies the training algorithm to use.
        :param input_data_config: Describes the various datasets (e.g. train, validation, test) and the Amazon S3 location where stored.
        :param output_data_config: Identifies the Amazon S3 location where you want Amazon SageMaker to save the results of model training.
        :param training_job_name: Training Job Name.
        :param hyperparameters: Hyperparameters to be used for the train job.
        :param integration_pattern: The service integration pattern indicates different ways to call SageMaker APIs. The valid value is either FIRE_AND_FORGET or SYNC. Default: FIRE_AND_FORGET
        :param resource_config: Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training.
        :param role: Role for the Training Job. The role must be granted all necessary permissions for the SageMaker training job to be able to operate. See https://docs.aws.amazon.com/fr_fr/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-createtrainingjob-perms Default: - a role with appropriate permissions will be created.
        :param stopping_condition: Sets a time limit for training.
        :param tags: Tags to be applied to the train job.
        :param vpc_config: Specifies the VPC that you want your training job to connect to.

        stability
        :stability: experimental
        """
        self._values = {
            'algorithm_specification': algorithm_specification,
            'input_data_config': input_data_config,
            'output_data_config': output_data_config,
            'training_job_name': training_job_name,
        }
        if hyperparameters is not None: self._values["hyperparameters"] = hyperparameters
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if resource_config is not None: self._values["resource_config"] = resource_config
        if role is not None: self._values["role"] = role
        if stopping_condition is not None: self._values["stopping_condition"] = stopping_condition
        if tags is not None: self._values["tags"] = tags
        if vpc_config is not None: self._values["vpc_config"] = vpc_config

    @property
    def algorithm_specification(self) -> "AlgorithmSpecification":
        """Identifies the training algorithm to use.

        stability
        :stability: experimental
        """
        return self._values.get('algorithm_specification')

    @property
    def input_data_config(self) -> typing.List["Channel"]:
        """Describes the various datasets (e.g. train, validation, test) and the Amazon S3 location where stored.

        stability
        :stability: experimental
        """
        return self._values.get('input_data_config')

    @property
    def output_data_config(self) -> "OutputDataConfig":
        """Identifies the Amazon S3 location where you want Amazon SageMaker to save the results of model training.

        stability
        :stability: experimental
        """
        return self._values.get('output_data_config')

    @property
    def training_job_name(self) -> str:
        """Training Job Name.

        stability
        :stability: experimental
        """
        return self._values.get('training_job_name')

    @property
    def hyperparameters(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """Hyperparameters to be used for the train job.

        stability
        :stability: experimental
        """
        return self._values.get('hyperparameters')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call SageMaker APIs.

        The valid value is either FIRE_AND_FORGET or SYNC.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def resource_config(self) -> typing.Optional["ResourceConfig"]:
        """Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training.

        stability
        :stability: experimental
        """
        return self._values.get('resource_config')

    @property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """Role for the Training Job.

        The role must be granted all necessary permissions for the SageMaker training job to
        be able to operate.

        See https://docs.aws.amazon.com/fr_fr/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-createtrainingjob-perms

        default
        :default: - a role with appropriate permissions will be created.

        stability
        :stability: experimental
        """
        return self._values.get('role')

    @property
    def stopping_condition(self) -> typing.Optional["StoppingCondition"]:
        """Sets a time limit for training.

        stability
        :stability: experimental
        """
        return self._values.get('stopping_condition')

    @property
    def tags(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Tags to be applied to the train job.

        stability
        :stability: experimental
        """
        return self._values.get('tags')

    @property
    def vpc_config(self) -> typing.Optional["VpcConfig"]:
        """Specifies the VPC that you want your training job to connect to.

        stability
        :stability: experimental
        """
        return self._values.get('vpc_config')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SagemakerTrainTaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.SagemakerTransformProps", jsii_struct_bases=[], name_mapping={'model_name': 'modelName', 'transform_input': 'transformInput', 'transform_job_name': 'transformJobName', 'transform_output': 'transformOutput', 'batch_strategy': 'batchStrategy', 'environment': 'environment', 'integration_pattern': 'integrationPattern', 'max_concurrent_transforms': 'maxConcurrentTransforms', 'max_payload_in_mb': 'maxPayloadInMB', 'role': 'role', 'tags': 'tags', 'transform_resources': 'transformResources'})
class SagemakerTransformProps():
    def __init__(self, *, model_name: str, transform_input: "TransformInput", transform_job_name: str, transform_output: "TransformOutput", batch_strategy: typing.Optional["BatchStrategy"]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, max_concurrent_transforms: typing.Optional[jsii.Number]=None, max_payload_in_mb: typing.Optional[jsii.Number]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, transform_resources: typing.Optional["TransformResources"]=None):
        """
        :param model_name: Name of the model that you want to use for the transform job.
        :param transform_input: Dataset to be transformed and the Amazon S3 location where it is stored.
        :param transform_job_name: Training Job Name.
        :param transform_output: S3 location where you want Amazon SageMaker to save the results from the transform job.
        :param batch_strategy: Number of records to include in a mini-batch for an HTTP inference request.
        :param environment: Environment variables to set in the Docker container.
        :param integration_pattern: The service integration pattern indicates different ways to call SageMaker APIs. The valid value is either FIRE_AND_FORGET or SYNC. Default: FIRE_AND_FORGET
        :param max_concurrent_transforms: Maximum number of parallel requests that can be sent to each instance in a transform job.
        :param max_payload_in_mb: Maximum allowed size of the payload, in MB.
        :param role: Role for thte Training Job.
        :param tags: Tags to be applied to the train job.
        :param transform_resources: ML compute instances for the transform job.

        stability
        :stability: experimental
        """
        self._values = {
            'model_name': model_name,
            'transform_input': transform_input,
            'transform_job_name': transform_job_name,
            'transform_output': transform_output,
        }
        if batch_strategy is not None: self._values["batch_strategy"] = batch_strategy
        if environment is not None: self._values["environment"] = environment
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if max_concurrent_transforms is not None: self._values["max_concurrent_transforms"] = max_concurrent_transforms
        if max_payload_in_mb is not None: self._values["max_payload_in_mb"] = max_payload_in_mb
        if role is not None: self._values["role"] = role
        if tags is not None: self._values["tags"] = tags
        if transform_resources is not None: self._values["transform_resources"] = transform_resources

    @property
    def model_name(self) -> str:
        """Name of the model that you want to use for the transform job.

        stability
        :stability: experimental
        """
        return self._values.get('model_name')

    @property
    def transform_input(self) -> "TransformInput":
        """Dataset to be transformed and the Amazon S3 location where it is stored.

        stability
        :stability: experimental
        """
        return self._values.get('transform_input')

    @property
    def transform_job_name(self) -> str:
        """Training Job Name.

        stability
        :stability: experimental
        """
        return self._values.get('transform_job_name')

    @property
    def transform_output(self) -> "TransformOutput":
        """S3 location where you want Amazon SageMaker to save the results from the transform job.

        stability
        :stability: experimental
        """
        return self._values.get('transform_output')

    @property
    def batch_strategy(self) -> typing.Optional["BatchStrategy"]:
        """Number of records to include in a mini-batch for an HTTP inference request.

        stability
        :stability: experimental
        """
        return self._values.get('batch_strategy')

    @property
    def environment(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Environment variables to set in the Docker container.

        stability
        :stability: experimental
        """
        return self._values.get('environment')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call SageMaker APIs.

        The valid value is either FIRE_AND_FORGET or SYNC.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def max_concurrent_transforms(self) -> typing.Optional[jsii.Number]:
        """Maximum number of parallel requests that can be sent to each instance in a transform job.

        stability
        :stability: experimental
        """
        return self._values.get('max_concurrent_transforms')

    @property
    def max_payload_in_mb(self) -> typing.Optional[jsii.Number]:
        """Maximum allowed size of the payload, in MB.

        stability
        :stability: experimental
        """
        return self._values.get('max_payload_in_mb')

    @property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """Role for thte Training Job.

        stability
        :stability: experimental
        """
        return self._values.get('role')

    @property
    def tags(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Tags to be applied to the train job.

        stability
        :stability: experimental
        """
        return self._values.get('tags')

    @property
    def transform_resources(self) -> typing.Optional["TransformResources"]:
        """ML compute instances for the transform job.

        stability
        :stability: experimental
        """
        return self._values.get('transform_resources')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SagemakerTransformProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class SagemakerTransformTask(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.SagemakerTransformTask"):
    """Class representing the SageMaker Create Training Job task.

    stability
    :stability: experimental
    """
    def __init__(self, *, model_name: str, transform_input: "TransformInput", transform_job_name: str, transform_output: "TransformOutput", batch_strategy: typing.Optional["BatchStrategy"]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, max_concurrent_transforms: typing.Optional[jsii.Number]=None, max_payload_in_mb: typing.Optional[jsii.Number]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, transform_resources: typing.Optional["TransformResources"]=None) -> None:
        """
        :param props: -
        :param model_name: Name of the model that you want to use for the transform job.
        :param transform_input: Dataset to be transformed and the Amazon S3 location where it is stored.
        :param transform_job_name: Training Job Name.
        :param transform_output: S3 location where you want Amazon SageMaker to save the results from the transform job.
        :param batch_strategy: Number of records to include in a mini-batch for an HTTP inference request.
        :param environment: Environment variables to set in the Docker container.
        :param integration_pattern: The service integration pattern indicates different ways to call SageMaker APIs. The valid value is either FIRE_AND_FORGET or SYNC. Default: FIRE_AND_FORGET
        :param max_concurrent_transforms: Maximum number of parallel requests that can be sent to each instance in a transform job.
        :param max_payload_in_mb: Maximum allowed size of the payload, in MB.
        :param role: Role for thte Training Job.
        :param tags: Tags to be applied to the train job.
        :param transform_resources: ML compute instances for the transform job.

        stability
        :stability: experimental
        """
        props = SagemakerTransformProps(model_name=model_name, transform_input=transform_input, transform_job_name=transform_job_name, transform_output=transform_output, batch_strategy=batch_strategy, environment=environment, integration_pattern=integration_pattern, max_concurrent_transforms=max_concurrent_transforms, max_payload_in_mb=max_payload_in_mb, role=role, tags=tags, transform_resources=transform_resources)

        jsii.create(SagemakerTransformTask, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [task])

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """The execution role for the Sagemaker training job.

        Only available after task has been added to a state machine.

        stability
        :stability: experimental
        """
        return jsii.get(self, "role")


@jsii.implements(aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class SendToQueue(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.SendToQueue"):
    """A StepFunctions Task to send messages to SQS queue.

    A Function can be used directly as a Resource, but this class mirrors
    integration with other AWS services via a specific class instance.

    stability
    :stability: experimental
    """
    def __init__(self, queue: aws_cdk.aws_sqs.IQueue, *, message_body: aws_cdk.aws_stepfunctions.TaskInput, delay: typing.Optional[aws_cdk.core.Duration]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, message_deduplication_id: typing.Optional[str]=None, message_group_id: typing.Optional[str]=None) -> None:
        """
        :param queue: -
        :param props: -
        :param message_body: The text message to send to the queue.
        :param delay: The length of time, in seconds, for which to delay a specific message. Valid values are 0-900 seconds. Default: Default value of the queue is used
        :param integration_pattern: The service integration pattern indicates different ways to call SendMessage to SQS. The valid value is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET
        :param message_deduplication_id: The token used for deduplication of sent messages. Default: Use content-based deduplication
        :param message_group_id: The tag that specifies that a message belongs to a specific message group. Required for FIFO queues. FIFO ordering applies to messages in the same message group. Default: No group ID

        stability
        :stability: experimental
        """
        props = SendToQueueProps(message_body=message_body, delay=delay, integration_pattern=integration_pattern, message_deduplication_id=message_deduplication_id, message_group_id=message_group_id)

        jsii.create(SendToQueue, self, [queue, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param _task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [_task])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.SendToQueueProps", jsii_struct_bases=[], name_mapping={'message_body': 'messageBody', 'delay': 'delay', 'integration_pattern': 'integrationPattern', 'message_deduplication_id': 'messageDeduplicationId', 'message_group_id': 'messageGroupId'})
class SendToQueueProps():
    def __init__(self, *, message_body: aws_cdk.aws_stepfunctions.TaskInput, delay: typing.Optional[aws_cdk.core.Duration]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, message_deduplication_id: typing.Optional[str]=None, message_group_id: typing.Optional[str]=None):
        """Properties for SendMessageTask.

        :param message_body: The text message to send to the queue.
        :param delay: The length of time, in seconds, for which to delay a specific message. Valid values are 0-900 seconds. Default: Default value of the queue is used
        :param integration_pattern: The service integration pattern indicates different ways to call SendMessage to SQS. The valid value is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN. Default: FIRE_AND_FORGET
        :param message_deduplication_id: The token used for deduplication of sent messages. Default: Use content-based deduplication
        :param message_group_id: The tag that specifies that a message belongs to a specific message group. Required for FIFO queues. FIFO ordering applies to messages in the same message group. Default: No group ID

        stability
        :stability: experimental
        """
        self._values = {
            'message_body': message_body,
        }
        if delay is not None: self._values["delay"] = delay
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if message_deduplication_id is not None: self._values["message_deduplication_id"] = message_deduplication_id
        if message_group_id is not None: self._values["message_group_id"] = message_group_id

    @property
    def message_body(self) -> aws_cdk.aws_stepfunctions.TaskInput:
        """The text message to send to the queue.

        stability
        :stability: experimental
        """
        return self._values.get('message_body')

    @property
    def delay(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The length of time, in seconds, for which to delay a specific message.

        Valid values are 0-900 seconds.

        default
        :default: Default value of the queue is used

        stability
        :stability: experimental
        """
        return self._values.get('delay')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call SendMessage to SQS.

        The valid value is either FIRE_AND_FORGET or WAIT_FOR_TASK_TOKEN.

        default
        :default: FIRE_AND_FORGET

        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def message_deduplication_id(self) -> typing.Optional[str]:
        """The token used for deduplication of sent messages.

        default
        :default: Use content-based deduplication

        stability
        :stability: experimental
        """
        return self._values.get('message_deduplication_id')

    @property
    def message_group_id(self) -> typing.Optional[str]:
        """The tag that specifies that a message belongs to a specific message group.

        Required for FIFO queues. FIFO ordering applies to messages in the same message
        group.

        default
        :default: No group ID

        stability
        :stability: experimental
        """
        return self._values.get('message_group_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SendToQueueProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.ShuffleConfig", jsii_struct_bases=[], name_mapping={'seed': 'seed'})
class ShuffleConfig():
    def __init__(self, *, seed: jsii.Number):
        """Configuration for a shuffle option for input data in a channel.

        :param seed: Determines the shuffling order.

        stability
        :stability: experimental
        """
        self._values = {
            'seed': seed,
        }

    @property
    def seed(self) -> jsii.Number:
        """Determines the shuffling order.

        stability
        :stability: experimental
        """
        return self._values.get('seed')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ShuffleConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-stepfunctions-tasks.SplitType")
class SplitType(enum.Enum):
    """Method to use to split the transform job's data files into smaller batches.

    stability
    :stability: experimental
    """
    NONE = "NONE"
    """Input data files are not split,.

    stability
    :stability: experimental
    """
    LINE = "LINE"
    """Split records on a newline character boundary.

    stability
    :stability: experimental
    """
    RECORD_IO = "RECORD_IO"
    """Split using MXNet RecordIO format.

    stability
    :stability: experimental
    """
    TF_RECORD = "TF_RECORD"
    """Split using TensorFlow TFRecord format.

    stability
    :stability: experimental
    """

@jsii.implements(aws_cdk.aws_stepfunctions.IStepFunctionsTask)
class StartExecution(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-stepfunctions-tasks.StartExecution"):
    """A Step Functions Task to call StartExecution on another state machine.

    It supports three service integration patterns: FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN.

    stability
    :stability: experimental
    """
    def __init__(self, state_machine: aws_cdk.aws_stepfunctions.IStateMachine, *, input: typing.Optional[typing.Mapping[str,typing.Any]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, name: typing.Optional[str]=None) -> None:
        """
        :param state_machine: -
        :param props: -
        :param input: The JSON input for the execution, same as that of StartExecution.
        :param integration_pattern: The service integration pattern indicates different ways to call StartExecution to Step Functions. Default: FIRE_AND_FORGET
        :param name: The name of the execution, same as that of StartExecution.

        stability
        :stability: experimental
        """
        props = StartExecutionProps(input=input, integration_pattern=integration_pattern, name=name)

        jsii.create(StartExecution, self, [state_machine, props])

    @jsii.member(jsii_name="bind")
    def bind(self, task: aws_cdk.aws_stepfunctions.Task) -> aws_cdk.aws_stepfunctions.StepFunctionsTaskConfig:
        """Called when the task object is used in a workflow.

        :param task: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "bind", [task])


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.StartExecutionProps", jsii_struct_bases=[], name_mapping={'input': 'input', 'integration_pattern': 'integrationPattern', 'name': 'name'})
class StartExecutionProps():
    def __init__(self, *, input: typing.Optional[typing.Mapping[str,typing.Any]]=None, integration_pattern: typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]=None, name: typing.Optional[str]=None):
        """Properties for StartExecution.

        :param input: The JSON input for the execution, same as that of StartExecution.
        :param integration_pattern: The service integration pattern indicates different ways to call StartExecution to Step Functions. Default: FIRE_AND_FORGET
        :param name: The name of the execution, same as that of StartExecution.

        stability
        :stability: experimental
        """
        self._values = {
        }
        if input is not None: self._values["input"] = input
        if integration_pattern is not None: self._values["integration_pattern"] = integration_pattern
        if name is not None: self._values["name"] = name

    @property
    def input(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """The JSON input for the execution, same as that of StartExecution.

        see
        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        stability
        :stability: experimental
        """
        return self._values.get('input')

    @property
    def integration_pattern(self) -> typing.Optional[aws_cdk.aws_stepfunctions.ServiceIntegrationPattern]:
        """The service integration pattern indicates different ways to call StartExecution to Step Functions.

        default
        :default: FIRE_AND_FORGET

        see
        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html
        stability
        :stability: experimental
        """
        return self._values.get('integration_pattern')

    @property
    def name(self) -> typing.Optional[str]:
        """The name of the execution, same as that of StartExecution.

        see
        :see: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html
        stability
        :stability: experimental
        """
        return self._values.get('name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StartExecutionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.StoppingCondition", jsii_struct_bases=[], name_mapping={'max_runtime': 'maxRuntime'})
class StoppingCondition():
    def __init__(self, *, max_runtime: typing.Optional[aws_cdk.core.Duration]=None):
        """
        :param max_runtime: The maximum length of time, in seconds, that the training or compilation job can run.

        stability
        :stability: experimental
        """
        self._values = {
        }
        if max_runtime is not None: self._values["max_runtime"] = max_runtime

    @property
    def max_runtime(self) -> typing.Optional[aws_cdk.core.Duration]:
        """The maximum length of time, in seconds, that the training or compilation job can run.

        stability
        :stability: experimental
        """
        return self._values.get('max_runtime')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StoppingCondition(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.TaskEnvironmentVariable", jsii_struct_bases=[], name_mapping={'name': 'name', 'value': 'value'})
class TaskEnvironmentVariable():
    def __init__(self, *, name: str, value: str):
        """An environment variable to be set in the container run as a task.

        :param name: Name for the environment variable. Exactly one of ``name`` and ``namePath`` must be specified.
        :param value: Value of the environment variable. Exactly one of ``value`` and ``valuePath`` must be specified.

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
            'value': value,
        }

    @property
    def name(self) -> str:
        """Name for the environment variable.

        Exactly one of ``name`` and ``namePath`` must be specified.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @property
    def value(self) -> str:
        """Value of the environment variable.

        Exactly one of ``value`` and ``valuePath`` must be specified.

        stability
        :stability: experimental
        """
        return self._values.get('value')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TaskEnvironmentVariable(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.TransformDataSource", jsii_struct_bases=[], name_mapping={'s3_data_source': 's3DataSource'})
class TransformDataSource():
    def __init__(self, *, s3_data_source: "TransformS3DataSource"):
        """S3 location of the input data that the model can consume.

        :param s3_data_source: S3 location of the input data.

        stability
        :stability: experimental
        """
        self._values = {
            's3_data_source': s3_data_source,
        }

    @property
    def s3_data_source(self) -> "TransformS3DataSource":
        """S3 location of the input data.

        stability
        :stability: experimental
        """
        return self._values.get('s3_data_source')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TransformDataSource(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.TransformInput", jsii_struct_bases=[], name_mapping={'transform_data_source': 'transformDataSource', 'compression_type': 'compressionType', 'content_type': 'contentType', 'split_type': 'splitType'})
class TransformInput():
    def __init__(self, *, transform_data_source: "TransformDataSource", compression_type: typing.Optional["CompressionType"]=None, content_type: typing.Optional[str]=None, split_type: typing.Optional["SplitType"]=None):
        """Dataset to be transformed and the Amazon S3 location where it is stored.

        :param transform_data_source: S3 location of the channel data.
        :param compression_type: The compression type of the transform data.
        :param content_type: Multipurpose internet mail extension (MIME) type of the data.
        :param split_type: Method to use to split the transform job's data files into smaller batches.

        stability
        :stability: experimental
        """
        self._values = {
            'transform_data_source': transform_data_source,
        }
        if compression_type is not None: self._values["compression_type"] = compression_type
        if content_type is not None: self._values["content_type"] = content_type
        if split_type is not None: self._values["split_type"] = split_type

    @property
    def transform_data_source(self) -> "TransformDataSource":
        """S3 location of the channel data.

        stability
        :stability: experimental
        """
        return self._values.get('transform_data_source')

    @property
    def compression_type(self) -> typing.Optional["CompressionType"]:
        """The compression type of the transform data.

        stability
        :stability: experimental
        """
        return self._values.get('compression_type')

    @property
    def content_type(self) -> typing.Optional[str]:
        """Multipurpose internet mail extension (MIME) type of the data.

        stability
        :stability: experimental
        """
        return self._values.get('content_type')

    @property
    def split_type(self) -> typing.Optional["SplitType"]:
        """Method to use to split the transform job's data files into smaller batches.

        stability
        :stability: experimental
        """
        return self._values.get('split_type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TransformInput(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.TransformOutput", jsii_struct_bases=[], name_mapping={'s3_output_path': 's3OutputPath', 'accept': 'accept', 'assemble_with': 'assembleWith', 'encryption_key': 'encryptionKey'})
class TransformOutput():
    def __init__(self, *, s3_output_path: str, accept: typing.Optional[str]=None, assemble_with: typing.Optional["AssembleWith"]=None, encryption_key: typing.Optional[aws_cdk.aws_kms.Key]=None):
        """S3 location where you want Amazon SageMaker to save the results from the transform job.

        :param s3_output_path: S3 path where you want Amazon SageMaker to store the results of the transform job.
        :param accept: MIME type used to specify the output data.
        :param assemble_with: Defines how to assemble the results of the transform job as a single S3 object.
        :param encryption_key: AWS KMS key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

        stability
        :stability: experimental
        """
        self._values = {
            's3_output_path': s3_output_path,
        }
        if accept is not None: self._values["accept"] = accept
        if assemble_with is not None: self._values["assemble_with"] = assemble_with
        if encryption_key is not None: self._values["encryption_key"] = encryption_key

    @property
    def s3_output_path(self) -> str:
        """S3 path where you want Amazon SageMaker to store the results of the transform job.

        stability
        :stability: experimental
        """
        return self._values.get('s3_output_path')

    @property
    def accept(self) -> typing.Optional[str]:
        """MIME type used to specify the output data.

        stability
        :stability: experimental
        """
        return self._values.get('accept')

    @property
    def assemble_with(self) -> typing.Optional["AssembleWith"]:
        """Defines how to assemble the results of the transform job as a single S3 object.

        stability
        :stability: experimental
        """
        return self._values.get('assemble_with')

    @property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.Key]:
        """AWS KMS key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

        stability
        :stability: experimental
        """
        return self._values.get('encryption_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TransformOutput(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.TransformResources", jsii_struct_bases=[], name_mapping={'instance_count': 'instanceCount', 'instance_type': 'instanceType', 'volume_kms_key_id': 'volumeKmsKeyId'})
class TransformResources():
    def __init__(self, *, instance_count: jsii.Number, instance_type: aws_cdk.aws_ec2.InstanceType, volume_kms_key_id: typing.Optional[aws_cdk.aws_kms.Key]=None):
        """ML compute instances for the transform job.

        :param instance_count: Nmber of ML compute instances to use in the transform job.
        :param instance_type: ML compute instance type for the transform job.
        :param volume_kms_key_id: AWS KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s).

        stability
        :stability: experimental
        """
        self._values = {
            'instance_count': instance_count,
            'instance_type': instance_type,
        }
        if volume_kms_key_id is not None: self._values["volume_kms_key_id"] = volume_kms_key_id

    @property
    def instance_count(self) -> jsii.Number:
        """Nmber of ML compute instances to use in the transform job.

        stability
        :stability: experimental
        """
        return self._values.get('instance_count')

    @property
    def instance_type(self) -> aws_cdk.aws_ec2.InstanceType:
        """ML compute instance type for the transform job.

        stability
        :stability: experimental
        """
        return self._values.get('instance_type')

    @property
    def volume_kms_key_id(self) -> typing.Optional[aws_cdk.aws_kms.Key]:
        """AWS KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s).

        stability
        :stability: experimental
        """
        return self._values.get('volume_kms_key_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TransformResources(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.TransformS3DataSource", jsii_struct_bases=[], name_mapping={'s3_uri': 's3Uri', 's3_data_type': 's3DataType'})
class TransformS3DataSource():
    def __init__(self, *, s3_uri: str, s3_data_type: typing.Optional["S3DataType"]=None):
        """Location of the channel data.

        :param s3_uri: Identifies either a key name prefix or a manifest.
        :param s3_data_type: S3 Data Type. Default: 'S3Prefix'

        stability
        :stability: experimental
        """
        self._values = {
            's3_uri': s3_uri,
        }
        if s3_data_type is not None: self._values["s3_data_type"] = s3_data_type

    @property
    def s3_uri(self) -> str:
        """Identifies either a key name prefix or a manifest.

        stability
        :stability: experimental
        """
        return self._values.get('s3_uri')

    @property
    def s3_data_type(self) -> typing.Optional["S3DataType"]:
        """S3 Data Type.

        default
        :default: 'S3Prefix'

        stability
        :stability: experimental
        """
        return self._values.get('s3_data_type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'TransformS3DataSource(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-stepfunctions-tasks.VpcConfig", jsii_struct_bases=[], name_mapping={'vpc': 'vpc', 'subnets': 'subnets'})
class VpcConfig():
    def __init__(self, *, vpc: aws_cdk.aws_ec2.IVpc, subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None):
        """
        :param vpc: VPC id.
        :param subnets: VPC subnets.

        stability
        :stability: experimental
        """
        self._values = {
            'vpc': vpc,
        }
        if subnets is not None: self._values["subnets"] = subnets

    @property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        """VPC id.

        stability
        :stability: experimental
        """
        return self._values.get('vpc')

    @property
    def subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        """VPC subnets.

        stability
        :stability: experimental
        """
        return self._values.get('subnets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["AlgorithmSpecification", "AssembleWith", "BatchStrategy", "Channel", "CommonEcsRunTaskProps", "CompressionType", "ContainerOverride", "DataSource", "DockerImage", "DockerImageConfig", "EcsRunTaskBase", "EcsRunTaskBaseProps", "ISageMakerTask", "InputMode", "InvocationType", "InvokeActivity", "InvokeActivityProps", "InvokeFunction", "InvokeFunctionProps", "MetricDefinition", "OutputDataConfig", "PublishToTopic", "PublishToTopicProps", "RecordWrapperType", "ResourceConfig", "RunEcsEc2Task", "RunEcsEc2TaskProps", "RunEcsFargateTask", "RunEcsFargateTaskProps", "RunLambdaTask", "RunLambdaTaskProps", "S3DataDistributionType", "S3DataSource", "S3DataType", "S3Location", "S3LocationBindOptions", "S3LocationConfig", "SagemakerTrainTask", "SagemakerTrainTaskProps", "SagemakerTransformProps", "SagemakerTransformTask", "SendToQueue", "SendToQueueProps", "ShuffleConfig", "SplitType", "StartExecution", "StartExecutionProps", "StoppingCondition", "TaskEnvironmentVariable", "TransformDataSource", "TransformInput", "TransformOutput", "TransformResources", "TransformS3DataSource", "VpcConfig", "__jsii_assembly__"]

publication.publish()
