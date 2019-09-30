import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.assets
import aws_cdk.aws_iam
import aws_cdk.aws_s3
import aws_cdk.core
import aws_cdk.cx_api
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-s3-assets", "1.8.0", __name__, "aws-s3-assets@1.8.0.jsii.tgz")
@jsii.implements(aws_cdk.assets.IAsset)
class Asset(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-s3-assets.Asset"):
    """An asset represents a local file or directory, which is automatically uploaded to S3 and then can be referenced within a CDK application.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, path: str, readers: typing.Optional[typing.List[aws_cdk.aws_iam.IGrantable]]=None, exclude: typing.Optional[typing.List[str]]=None, follow: typing.Optional[aws_cdk.assets.FollowMode]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param path: The disk location of the asset. The path should refer to one of the following: - A regular file or a .zip file, in which case the file will be uploaded as-is to S3. - A directory, in which case it will be archived into a .zip file and uploaded to S3.
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param exclude: Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: Never

        stability
        :stability: experimental
        """
        props = AssetProps(path=path, readers=readers, exclude=exclude, follow=follow)

        jsii.create(Asset, self, [scope, id, props])

    @jsii.member(jsii_name="addResourceMetadata")
    def add_resource_metadata(self, resource: aws_cdk.core.CfnResource, resource_property: str) -> None:
        """Adds CloudFormation template metadata to the specified resource with information that indicates which resource property is mapped to this local asset.

        This can be used by tools such as SAM CLI to provide local
        experience such as local invocation and debugging of Lambda functions.

        Asset metadata will only be included if the stack is synthesized with the
        "aws:cdk:enable-asset-metadata" context key defined, which is the default
        behavior when synthesizing via the CDK Toolkit.

        :param resource: The CloudFormation resource which is using this asset [disable-awslint:ref-via-interface].
        :param resource_property: The property name where this asset is referenced (e.g. "Code" for AWS::Lambda::Function).

        see
        :see: https://github.com/aws/aws-cdk/issues/1432
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addResourceMetadata", [resource, resource_property])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> None:
        """Grants read permissions to the principal on the asset's S3 object.

        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @property
    @jsii.member(jsii_name="assetPath")
    def asset_path(self) -> str:
        """The path to the asset (stringinfied token).

        If asset staging is disabled, this will just be the original path.
        If asset staging is enabled it will be the staged path.

        stability
        :stability: experimental
        """
        return jsii.get(self, "assetPath")

    @property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> aws_cdk.aws_s3.IBucket:
        """The S3 bucket in which this asset resides.

        stability
        :stability: experimental
        """
        return jsii.get(self, "bucket")

    @property
    @jsii.member(jsii_name="isZipArchive")
    def is_zip_archive(self) -> bool:
        """Indicates if this asset is a zip archive.

        Allows constructs to ensure that the
        correct file type was used.

        stability
        :stability: experimental
        """
        return jsii.get(self, "isZipArchive")

    @property
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> str:
        """Attribute that represents the name of the bucket this asset exists in.

        stability
        :stability: experimental
        """
        return jsii.get(self, "s3BucketName")

    @property
    @jsii.member(jsii_name="s3ObjectKey")
    def s3_object_key(self) -> str:
        """Attribute which represents the S3 object key of this asset.

        stability
        :stability: experimental
        """
        return jsii.get(self, "s3ObjectKey")

    @property
    @jsii.member(jsii_name="s3Url")
    def s3_url(self) -> str:
        """Attribute which represents the S3 URL of this asset.

        stability
        :stability: experimental

        Example::
            https://s3.us-west-1.amazonaws.com/bucket/key
        """
        return jsii.get(self, "s3Url")

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


@jsii.data_type(jsii_type="@aws-cdk/aws-s3-assets.AssetProps", jsii_struct_bases=[aws_cdk.assets.CopyOptions], name_mapping={'exclude': 'exclude', 'follow': 'follow', 'path': 'path', 'readers': 'readers'})
class AssetProps(aws_cdk.assets.CopyOptions):
    def __init__(self, *, exclude: typing.Optional[typing.List[str]]=None, follow: typing.Optional[aws_cdk.assets.FollowMode]=None, path: str, readers: typing.Optional[typing.List[aws_cdk.aws_iam.IGrantable]]=None):
        """
        :param exclude: Glob patterns to exclude from the copy. Default: nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: Never
        :param path: The disk location of the asset. The path should refer to one of the following: - A regular file or a .zip file, in which case the file will be uploaded as-is to S3. - A directory, in which case it will be archived into a .zip file and uploaded to S3.
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.

        stability
        :stability: experimental
        """
        self._values = {
            'path': path,
        }
        if exclude is not None: self._values["exclude"] = exclude
        if follow is not None: self._values["follow"] = follow
        if readers is not None: self._values["readers"] = readers

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
    def path(self) -> str:
        """The disk location of the asset.

        The path should refer to one of the following:

        - A regular file or a .zip file, in which case the file will be uploaded as-is to S3.
        - A directory, in which case it will be archived into a .zip file and uploaded to S3.

        stability
        :stability: experimental
        """
        return self._values.get('path')

    @property
    def readers(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.IGrantable]]:
        """A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later.

        default
        :default: - No principals that can read file asset.

        stability
        :stability: experimental
        """
        return self._values.get('readers')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AssetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["Asset", "AssetProps", "__jsii_assembly__"]

publication.publish()
