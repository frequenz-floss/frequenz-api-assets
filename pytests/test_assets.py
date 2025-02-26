# License: MIT
# Copyright © 2025 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.assets package."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api import assets

    assert assets is not None


def test_module_import_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.assets.v1 import assets_pb2

    assert assets_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.assets.v1 import assets_pb2_grpc

    assert assets_pb2_grpc is not None
