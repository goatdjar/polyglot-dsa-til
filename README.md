# dsa

A minimalist, multi-language data structures and algorithms workspace. Powered by Nix, Cargo, and uv.

## 📂 Project Structure

```text
dsa/
├── flake.nix             # Nix development environment (Rust + uv)
├── python/               # Python DSA library package
│   ├── dsa_utils/        # Library source code
│   └── pyproject.toml    # Python project configuration
├── rust/                 # Rust Cargo workspace
│   ├── Cargo.toml        # Workspace root manifest
│   └── dsa-core/         # Rust library crate
├── examples/             # Language-agnostic scratchpad run scripts
└── til/                  # Today I Learned markdown files
```

## 🚀 Quick Start

### 1. Enter the Environment
Run this in the project root to load all required system tools automatically:
```bash
nix develop
```

### 2. Python Workspace (uv)
Execute example scripts instantly. The local `dsa_utils` library is linked automatically:
```bash
uv run examples/run_sorting.py
```

### 3. Rust Workspace (Cargo)
Run the built-in module validation tests:
```bash
cd rust
cargo test
```

## 📝 Rules of the Repo
* **No standalone execution scripts in the source:** All algorithms must be built as importable library functions inside `python/` or `rust/`.
* **Scratchpad separation:** Keep all trial codes, benchmarks, and ad-hoc executions inside the `examples/` directory.
* **Keep it atomic:** Use the `til/` folder to write brief, concept-specific notes on time and space complexities.
