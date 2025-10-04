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

## Adding a new task

These are the instructions for adding a new task.

The basic steps are:

1. Add a new entry in `resources/type-definitions.yaml` (copy an existing one and adjust the name, input/output
   properties, etc.).
2. Create a new Python class in `src/` with the same name as the task type (e.g. `MyTask` for a task type
   `MyTask`).
3. Implement the `execute()` method of the class (access input properties via `self.input_properties` and set output
   properties via `self.set_output_property()`).
4. Add unit tests in `tests/` (copy an existing test case and adjust it).

You need to know the following and you may ask the user if you don't have this information:

1. Task name and prefix. For example `release.TaskName` where `release` is the prefix.
2. One input property and its type. For example `name` of type `string`.
3. One output property and its type. For example `result` of type `string

## Adding an exisiting server to a task

If you want to add an existing server to a task, you need to do the following

1. Find the server definition in `resources/type-definitions.yaml` (e.g. `MCPServer`).
2. Add a `server` property to the task definition in `resources/type-definitions.yaml` that references the server
   definition. This must be an input property
3. In the Python class, access the server configuration via `
