import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.assets
import aws_cdk.aws_cloudformation
import aws_cdk.aws_ecr
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.core
import aws_cdk.cx_api
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-ecr-assets", "1.7.0", __name__, "aws-ecr-assets@1.7.0.jsii.tgz")
@jsii.implements(aws_cdk.assets.IAsset)
class DockerImageAsset(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecr-assets.DockerImageAsset"):
    """An asset that represents a Docker image.

    The image will be created in build time and uploaded to an ECR repository.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, directory: str, build_args: typing.Optional[typing.Mapping[str,str]]=None, repository_name: typing.Optional[str]=None, exclude: typing.Optional[typing.List[str]]=None, follow: typing.Optional[aws_cdk.assets.FollowMode]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param directory: The directory where the Dockerfile is stored.
        :param build_args: Build args to pass to the ``docker build`` command. Default: no build args are passed
        :param repository_name: ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: automatically derived from the asset's ID.
        :param exclude: Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: Never

        stability
        :stability: experimental
        """
        props = DockerImageAssetProps(directory=directory, build_args=build_args, repository_name=repository_name, exclude=exclude, follow=follow)

        jsii.create(DockerImageAsset, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="artifactHash")
    def artifact_hash(self) -> str:
        """A hash of the bundle for of this asset, which is only available at deployment time.

        As this is
        a late-bound token, it may not be used in construct IDs, but can be passed as a resource
        property in order to force a change on a resource when an asset is effectively updated. This is
        more reliable than ``sourceHash`` in particular for assets which bundling phase involve external
        resources that can change over time (such as Docker image builds).

        stability
        :stability: experimental
        """
        return jsii.get(self, "artifactHash")

    @property
    @jsii.member(jsii_name="sourceHash")
    def source_hash(self) -> str:
        """A hash of the source of this asset, which is available at construction time.

        As this is a plain
        string, it can be used in construct IDs in order to enforce creation of a new resource when
        the content hash has changed.

        stability
        :stability: experimental
        """
        return jsii.get(self, "sourceHash")

    @property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> str:
        """The full URI of the image (including a tag).

        Use this reference to pull
        the asset.

        stability
        :stability: experimental
        """
        return jsii.get(self, "imageUri")

    @image_uri.setter
    def image_uri(self, value: str):
        return jsii.set(self, "imageUri", value)

    @property
    @jsii.member(jsii_name="repository")
    def repository(self) -> aws_cdk.aws_ecr.IRepository:
        """Repository where the image is stored.

        stability
        :stability: experimental
        """
        return jsii.get(self, "repository")

    @repository.setter
    def repository(self, value: aws_cdk.aws_ecr.IRepository):
        return jsii.set(self, "repository", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ecr-assets.DockerImageAssetProps", jsii_struct_bases=[aws_cdk.assets.CopyOptions], name_mapping={'exclude': 'exclude', 'follow': 'follow', 'directory': 'directory', 'build_args': 'buildArgs', 'repository_name': 'repositoryName'})
class DockerImageAssetProps(aws_cdk.assets.CopyOptions):
    def __init__(self, *, exclude: typing.Optional[typing.List[str]]=None, follow: typing.Optional[aws_cdk.assets.FollowMode]=None, directory: str, build_args: typing.Optional[typing.Mapping[str,str]]=None, repository_name: typing.Optional[str]=None):
        """
        :param exclude: Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: Never
        :param directory: The directory where the Dockerfile is stored.
        :param build_args: Build args to pass to the ``docker build`` command. Default: no build args are passed
        :param repository_name: ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: automatically derived from the asset's ID.

        stability
        :stability: experimental
        """
        self._values = {
            'directory': directory,
        }
        if exclude is not None: self._values["exclude"] = exclude
        if follow is not None: self._values["follow"] = follow
        if build_args is not None: self._values["build_args"] = build_args
        if repository_name is not None: self._values["repository_name"] = repository_name

    @property
    def exclude(self) -> typing.Optional[typing.List[str]]:
        """Glob patterns to exclude from the copy.

        default
        :default: nothing is excluded

        stability
        :stability: experimental
        """
        return self._values.get('exclude')

    @property
    def follow(self) -> typing.Optional[aws_cdk.assets.FollowMode]:
        """A strategy for how to handle symlinks.

        default
        :default: Never

        stability
        :stability: experimental
        """
        return self._values.get('follow')

    @property
    def directory(self) -> str:
        """The directory where the Dockerfile is stored.

        stability
        :stability: experimental
        """
        return self._values.get('directory')

    @property
    def build_args(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Build args to pass to the ``docker build`` command.

        default
        :default: no build args are passed

        stability
        :stability: experimental
        """
        return self._values.get('build_args')

    @property
    def repository_name(self) -> typing.Optional[str]:
        """ECR repository name.

        Specify this property if you need to statically address the image, e.g.
        from a Kubernetes Pod. Note, this is only the repository name, without the
        registry and the tag parts.

        default
        :default: automatically derived from the asset's ID.

        stability
        :stability: experimental
        """
        return self._values.get('repository_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DockerImageAssetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["DockerImageAsset", "DockerImageAssetProps", "__jsii_assembly__"]

publication.publish()
