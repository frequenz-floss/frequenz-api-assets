# Frequenz Assets API Release Notes

## Summary

This release renames `MarketLocationSelector` to `MarketLocation` and fixes
packaging for the generated Platform Assets API modules.

## Upgrading

- Rename `MarketLocationSelector` to `MarketLocation`.
- The legacy `frequenz.api.assets.v1` package was removed.
- Use `frequenz.api.platformassets.v1alpha1` for the generated API package.

## New Features


## Bug Fixes

- Include the generated runtime modules for
  `frequenz.api.platformassets.v1alpha1` in wheels.
