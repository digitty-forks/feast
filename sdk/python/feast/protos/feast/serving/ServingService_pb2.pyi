"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Copyright 2018 The Feast Authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import feast.types.Value_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FieldStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FieldStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FieldStatus.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INVALID: _FieldStatus.ValueType  # 0
    """Status is unset for this field."""
    PRESENT: _FieldStatus.ValueType  # 1
    """Field value is present for this field and age is within max age."""
    NULL_VALUE: _FieldStatus.ValueType  # 2
    """Values could be found for entity key and age is within max age, but
    this field value is not assigned a value on ingestion into feast.
    """
    NOT_FOUND: _FieldStatus.ValueType  # 3
    """Entity key did not return any values as they do not exist in Feast.
    This could suggest that the feature values have not yet been ingested
    into feast or the ingestion failed.
    """
    OUTSIDE_MAX_AGE: _FieldStatus.ValueType  # 4
    """Values could be found for entity key, but field values are outside the maximum
    allowable range.
    """

class FieldStatus(_FieldStatus, metaclass=_FieldStatusEnumTypeWrapper): ...

INVALID: FieldStatus.ValueType  # 0
"""Status is unset for this field."""
PRESENT: FieldStatus.ValueType  # 1
"""Field value is present for this field and age is within max age."""
NULL_VALUE: FieldStatus.ValueType  # 2
"""Values could be found for entity key and age is within max age, but
this field value is not assigned a value on ingestion into feast.
"""
NOT_FOUND: FieldStatus.ValueType  # 3
"""Entity key did not return any values as they do not exist in Feast.
This could suggest that the feature values have not yet been ingested
into feast or the ingestion failed.
"""
OUTSIDE_MAX_AGE: FieldStatus.ValueType  # 4
"""Values could be found for entity key, but field values are outside the maximum
allowable range.
"""
global___FieldStatus = FieldStatus

class GetFeastServingInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetFeastServingInfoRequest = GetFeastServingInfoRequest

class GetFeastServingInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    version: builtins.str
    """Feast version of this serving deployment."""
    def __init__(
        self,
        *,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["version", b"version"]) -> None: ...

global___GetFeastServingInfoResponse = GetFeastServingInfoResponse

class FeatureReferenceV2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURE_VIEW_NAME_FIELD_NUMBER: builtins.int
    FEATURE_NAME_FIELD_NUMBER: builtins.int
    feature_view_name: builtins.str
    """Name of the Feature View to retrieve the feature from."""
    feature_name: builtins.str
    """Name of the Feature to retrieve the feature from."""
    def __init__(
        self,
        *,
        feature_view_name: builtins.str = ...,
        feature_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["feature_name", b"feature_name", "feature_view_name", b"feature_view_name"]) -> None: ...

global___FeatureReferenceV2 = FeatureReferenceV2

class GetOnlineFeaturesRequestV2(google.protobuf.message.Message):
    """ToDo (oleksii): remove this message (since it's not used) and move EntityRow on package level"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class EntityRow(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class FieldsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            @property
            def value(self) -> feast.types.Value_pb2.Value: ...
            def __init__(
                self,
                *,
                key: builtins.str = ...,
                value: feast.types.Value_pb2.Value | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

        TIMESTAMP_FIELD_NUMBER: builtins.int
        FIELDS_FIELD_NUMBER: builtins.int
        @property
        def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """Request timestamp of this row. This value will be used,
            together with maxAge, to determine feature staleness.
            """
        @property
        def fields(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, feast.types.Value_pb2.Value]:
            """Map containing mapping of entity name to entity value."""
        def __init__(
            self,
            *,
            timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
            fields: collections.abc.Mapping[builtins.str, feast.types.Value_pb2.Value] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields", "timestamp", b"timestamp"]) -> None: ...

    FEATURES_FIELD_NUMBER: builtins.int
    ENTITY_ROWS_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    @property
    def features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureReferenceV2]:
        """List of features that are being retrieved"""
    @property
    def entity_rows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetOnlineFeaturesRequestV2.EntityRow]:
        """List of entity rows, containing entity id and timestamp data.
        Used during retrieval of feature rows and for joining feature
        rows into a final dataset
        """
    project: builtins.str
    """Optional field to specify project name override. If specified, uses the
    given project for retrieval. Overrides the projects specified in
    Feature References if both are specified.
    """
    def __init__(
        self,
        *,
        features: collections.abc.Iterable[global___FeatureReferenceV2] | None = ...,
        entity_rows: collections.abc.Iterable[global___GetOnlineFeaturesRequestV2.EntityRow] | None = ...,
        project: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_rows", b"entity_rows", "features", b"features", "project", b"project"]) -> None: ...

global___GetOnlineFeaturesRequestV2 = GetOnlineFeaturesRequestV2

class FeatureList(google.protobuf.message.Message):
    """In JSON "val" field can be omitted"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VAL_FIELD_NUMBER: builtins.int
    @property
    def val(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        val: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["val", b"val"]) -> None: ...

global___FeatureList = FeatureList

class GetOnlineFeaturesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class EntitiesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> feast.types.Value_pb2.RepeatedValue: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: feast.types.Value_pb2.RepeatedValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    class RequestContextEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> feast.types.Value_pb2.RepeatedValue: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: feast.types.Value_pb2.RepeatedValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    FEATURE_SERVICE_FIELD_NUMBER: builtins.int
    FEATURES_FIELD_NUMBER: builtins.int
    ENTITIES_FIELD_NUMBER: builtins.int
    FULL_FEATURE_NAMES_FIELD_NUMBER: builtins.int
    REQUEST_CONTEXT_FIELD_NUMBER: builtins.int
    feature_service: builtins.str
    @property
    def features(self) -> global___FeatureList: ...
    @property
    def entities(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, feast.types.Value_pb2.RepeatedValue]:
        """The entity data is specified in a columnar format
        A map of entity name -> list of values
        """
    full_feature_names: builtins.bool
    @property
    def request_context(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, feast.types.Value_pb2.RepeatedValue]:
        """Context for OnDemand Feature Transformation
        (was moved to dedicated parameter to avoid unnecessary separation logic on serving side)
        A map of variable name -> list of values
        """
    def __init__(
        self,
        *,
        feature_service: builtins.str = ...,
        features: global___FeatureList | None = ...,
        entities: collections.abc.Mapping[builtins.str, feast.types.Value_pb2.RepeatedValue] | None = ...,
        full_feature_names: builtins.bool = ...,
        request_context: collections.abc.Mapping[builtins.str, feast.types.Value_pb2.RepeatedValue] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["feature_service", b"feature_service", "features", b"features", "kind", b"kind"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entities", b"entities", "feature_service", b"feature_service", "features", b"features", "full_feature_names", b"full_feature_names", "kind", b"kind", "request_context", b"request_context"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["kind", b"kind"]) -> typing_extensions.Literal["feature_service", "features"] | None: ...

global___GetOnlineFeaturesRequest = GetOnlineFeaturesRequest

class GetOnlineFeaturesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class FeatureVector(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUES_FIELD_NUMBER: builtins.int
        STATUSES_FIELD_NUMBER: builtins.int
        EVENT_TIMESTAMPS_FIELD_NUMBER: builtins.int
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[feast.types.Value_pb2.Value]: ...
        @property
        def statuses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___FieldStatus.ValueType]: ...
        @property
        def event_timestamps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.timestamp_pb2.Timestamp]: ...
        def __init__(
            self,
            *,
            values: collections.abc.Iterable[feast.types.Value_pb2.Value] | None = ...,
            statuses: collections.abc.Iterable[global___FieldStatus.ValueType] | None = ...,
            event_timestamps: collections.abc.Iterable[google.protobuf.timestamp_pb2.Timestamp] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["event_timestamps", b"event_timestamps", "statuses", b"statuses", "values", b"values"]) -> None: ...

    METADATA_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> global___GetOnlineFeaturesResponseMetadata: ...
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetOnlineFeaturesResponse.FeatureVector]:
        """Length of "results" array should match length of requested features.
        We also preserve the same order of features here as in metadata.feature_names
        """
    status: builtins.bool
    def __init__(
        self,
        *,
        metadata: global___GetOnlineFeaturesResponseMetadata | None = ...,
        results: collections.abc.Iterable[global___GetOnlineFeaturesResponse.FeatureVector] | None = ...,
        status: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metadata", b"metadata", "results", b"results", "status", b"status"]) -> None: ...

global___GetOnlineFeaturesResponse = GetOnlineFeaturesResponse

class GetOnlineFeaturesResponseMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURE_NAMES_FIELD_NUMBER: builtins.int
    @property
    def feature_names(self) -> global___FeatureList: ...
    def __init__(
        self,
        *,
        feature_names: global___FeatureList | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["feature_names", b"feature_names"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["feature_names", b"feature_names"]) -> None: ...

global___GetOnlineFeaturesResponseMetadata = GetOnlineFeaturesResponseMetadata
