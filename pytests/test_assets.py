# License: MIT
# Copyright © 2025 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.platformassets package."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api import platformassets

    assert platformassets is not None


def test_platformassets_generated_modules_import() -> None:
    """Test that the platformassets runtime modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.platformassets.v1alpha1 import platformassets_pb2

    assert (
        platformassets_pb2.DESCRIPTOR.package == "frequenz.api.platformassets.v1alpha1"
    )

    # pylint: disable=import-outside-toplevel
    from frequenz.api.platformassets.v1alpha1 import platformassets_pb2_grpc

    assert platformassets_pb2_grpc is not None
