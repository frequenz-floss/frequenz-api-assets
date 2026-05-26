# Frequenz Assets API Release Notes

## Summary

This release adds `ListMicrogrids` and `GetGridpool` to
`frequenz.api.platformassets.v1alpha1`.

## Upgrading

- `frequenz.api.platformassets.v1alpha1.PlatformAssetsService` now includes
  `ListMicrogrids`.
- `frequenz.api.platformassets.v1alpha1` includes the `GetGridpool`
  request/response messages and RPC.
- `frequenz.api.platformassets.v1alpha1` remains a separate versioned package
  with the renamed `PlatformAssetsService`.

## New Features

- Add the `ListMicrogrids` RPC to the `PlatformAssetsService` service.
- Add the `GetGridpool` RPC to the `PlatformAssetsService` service.
