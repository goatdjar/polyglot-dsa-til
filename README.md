# dsa

A minimalist, multi-language data structures and algorithms workspace. Powered by Nix, Cargo, and uv.

## 📂 Project Structure

```text
dsa/
├── flake.nix             # Nix development environment (Rust + uv)
├── pyrightconfig.json    # Pyright LSP configuration for editor integration
├── python/               # 🐍 Python Workspace
│   ├── dsa_utils/        # Clean library source code (importable modules)
│   ├── examples/         # Scratchpad run scripts and execution sandboxes
│   ├── pyproject.toml    # Python project package metadata (Hatchling/uv)
│   └── tests/            # 🧪 NEW: Dedicated testing directory
├── rust/                 # 🦀 Rust Cargo Workspace
│   ├── Cargo.toml        # Workspace root manifest
│   └── dsa-core/         # Core Rust library crate
│       ├── src/          # Pure library code (lib.rs)
│       └── examples/     # Scratchpad execution scripts (run_sorting.rs)
└── til/                  # 📝 Today I Learned markdown files

```

## 🚀 Quick Start

### 1. Enter the Environment
Run this command in the project root to load all required system tools, runtimes, and paths automatically via Nix:

``` bash
direnv allow
```

Or

```bash
nix develop
```

### 2. Python Workspace (uv)
Navigate to the python/ directory to manage dependencies and execute scratchpad scripts. The local dsa_utils library is linked dynamically by uv:
```bash
cd python

# Run tests
uv run python -m unittest discover -s tests -v

# Run examples
uv run examples/run_sorting.py
```

### 3. Rust Workspace (Cargo)
Navigate to the rust/ directory to build your crates, run tests, or execute standalone example scripts:
```bash
cd rust

# Run unit tests inside the library
cargo test

# Run a localized scratchpad example script
# cargo run --example <filename_without_the_extension>
cargo run --example run_sorting 

# Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.01s
# Running `target/debug/examples/run_sorting`
Original array: [74, 23, 5, 89, 32, 12]
Sorted array: [5, 12, 23, 32, 74, 89]
```

## 📝 Rules of the Repo
* **No standalone execution scripts in the source:** All algorithms must be built as pure, importable library functions inside python/dsa_utils/ or rust/dsa-core/src/.
* **Language-Specific Sandbox Isolation:** Keep all trial codes, benchmarks, and ad-hoc executions strictly inside the respective language's localized examples/ directory.
* **Keep it atomic:** Use the til/ folder to write brief, concept-specific notes tracking structural observations, time complexity, and space complexity ($O$ notation).
