# MCP Client tasks for Digital.ai Release

AI demo tasks for Release

* **MCP**: Connect to any MCP server and invoke its tools
* **AI prompt**: Connect to an AI server and invoke a prompt. Support Gemini and OpenAI-compatible providers
* **Agent prompt**. Combines the MCP and AI prompt tasks to create an agent that can use tools

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

### 3. Set up credentials

Put your API keys into [setup/secrets.xlvals](setup/secrets.xlvals).

Use the example file as a base:

```commandline
cp setup/secrets.xlvals.example setup/secrets.xlvals
```

Then edit the file and add your keys.

### 4. Upload demo templates

Run the following command to upload the demo templates to the local Release instance:

```commandline
./xlw apply -f setup/mcp-demo.yaml
```

### Demo time!

1. Log in to http://localhost:5516 with admin/admin
2. Go to the **AI Demo** folder
3. Go the **Templates** section and run the examples

👉Add your favorite MCP Server or LLM provider under Connections and build your own example!

