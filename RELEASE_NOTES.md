# Frequenz Assets API Release Notes

## Summary

This release evolves the Assets API into the `PlatformAssetsService`, providing read-only access to platform asset metadata such as Gridpools, microgrids, electrical component inventories, and electrical component connections.

The release introduces Gridpool metadata retrieval and microgrid discovery within the current enterprise scope. It also aligns list request filtering with the structure used in other Frequenz APIs by moving filter fields into dedicated filter messages.

## Upgrading

- The service has been renamed to `PlatformAssetsService`.
- `GetGridpool` now returns only Gridpool metadata. Clients that need microgrids assigned to a Gridpool should use `ListMicrogrids` with the `gridpool_ids` filter.
- The `ListMicrogridElectricalComponentsRequest` and 
- `ListMicrogridElectricalComponentConnectionsRequest` messages now use 
  nested filter messages instead of placing all filter fields directly on the request message.
- Changed ordering of RPCs

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->
- New ListMicrogrids RPC has been added

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
