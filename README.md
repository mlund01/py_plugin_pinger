# py_plugin_pinger

Minimal Python [Squadron](https://github.com/mlund01/squadron) plugin —
the Python sibling of [plugin_pinger](https://github.com/mlund01/plugin_pinger).
Built with [squadron-sdk-py](https://github.com/mlund01/squadron-sdk-py).

Tools:

| Name   | Args                              | Returns                  | Notes                                  |
|--------|-----------------------------------|--------------------------|----------------------------------------|
| `ping` | none                              | `"pong"`                 | string passthrough                     |
| `pong` | none                              | `"ping"`                 | string passthrough                     |
| `echo` | `message: str, all_caps: bool`    | `"<greeting><message>"`  | uses the configured `greeting` setting |
| `add`  | `a: int, b: int`                  | `{sum: int, even: bool}` | structured (BaseModel) return          |

## Install

In your Squadron config:

```hcl
plugin "pinger" {
  source  = "github.com/mlund01/py_plugin_pinger"
  version = "v0.0.1"

  settings = {
    greeting = "hello "
  }
}
```

Squadron auto-downloads the wheel on first use, verifies its sha256 against
`checksums.txt`, and pip-installs it into a venv at
`.squadron/plugins/<platform>/pinger/v0.0.1/venv/`.

## Local development

```bash
squadron plugin build pinger /path/to/py_plugin_pinger
```

That creates a venv and installs the source. Set `version = "local"` in HCL.

## Release

Push a tag matching `v*`:

```bash
git tag v0.0.1
git push origin v0.0.1
```

The release workflow builds `py_plugin_pinger-<ver>-py3-none-any.whl`,
generates `checksums.txt`, and attaches both to a new GitHub release.

## License

MIT.
