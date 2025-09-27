# MCP Client Task & Agent Summary

This repository contains a Digital.ai Release integration plugin (container-based) whose purpose is to demonstrate how
to implement tasks and (specifically) an MCP Client task that can connect to a Model Context Protocol (MCP) ticket
server and invoke its tools (e.g. `list_tickets`).

The project started from the official template (see the separate workshop repository `release-integration-sdk-workshop`)
and keeps the standard build and packaging layout:

* `resources/type-definitions.yaml` – Defines the task types exposed in Release.
* `src/` – Python implementation classes (subclassing `digitalai.release.integration.BaseTask`).
* `tests/` – Unit tests (fast feedback loop without installing the plugin into Release).
* `dev-environment/` – Docker Compose resources for running a local Release development server.

## Fast Overview of Digital.ai Release Integration Plugin Lifecycle

1. Define or update task metadata in `resources/type-definitions.yaml` (names map to Python classes with identical
   simple names).
2. Implement or adjust Python task code under `src/`.
3. Add / refine unit tests under `tests/` for quick iteration.
4. Build the plugin + container image: `sh build.sh --upload` (or the Windows script) – publishes the image to the local
   registry and produces a plugin ZIP.
5. Install/refresh in the local Release instance using the wrapper script
   `./xlw plugin release install --file build/<artifact>.zip`.
6. Run/observe tasks in the Release UI (activity log, outputs, failures, etc.).

