# MCP Client tasks for Digital.ai Release

AI demo tasks for Release

* MCP: List tools
* MCP: Call tools
* Gemini prompt

## Prerequisites

You need to have the following installed in order to develop Python-based container tasks for Release using this
project:

* Python 3
* Docker

## Quickstart

### 1. Configure your `hosts` file

Add the following to `/etc/hosts` or `C:\Windows\System32\drivers\etc\hosts` (sudo / administrator permissions
required):

    127.0.0.1 container-registry

### 2. Start the Release environment:

```commandline
cd dev-environment
docker compose up -d --build
```

### 3. Build & publish the plugin

Run the build script

**Unix / macOS**

```commandline
sh build.sh --upload
```

**Windows**

```commandline
build.bat --upload
```

### 4. Upload demo templates

Run the following command to upload the demo templates to the local Release instance:

```commandline
./xlw apply -f setup/mcp-demo.yaml
```

### Browse the templates

1. Log in to http://localhost:5516 with admin/admin
2. Go to the **MCP Demo** folder
3. Go the **Templates** section and look at the examples

Now add your favorite MCP Server under Connections and build your own template using the MCP plugin!


