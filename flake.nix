{
  description = "DSA Scratchpad Environment for X";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.11";
    utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      utils,
    }:
    utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Rust Toolchain
            cargo
            rustc
            rust-analyzer
            clippy

            # Python Toolchain
            uv
            python312

            # System libraries often needed by Python wheels (C extensions)
            stdenv.cc.cc.lib
            zlib
          ];

          shellHook = ''
            # 1. Force uv to use the Nix-provided Python interpreter
            export UV_PYTHON="${pkgs.python3}/bin/python"

            # 2. Prevent uv from downloading its own unpatched Python binaries
            export UV_PYTHON_DOWNLOADS="never"

            # 3. Fix "missing shared library" errors for pre-compiled pip packages
            export LD_LIBRARY_PATH="${
              pkgs.lib.makeLibraryPath [
                pkgs.stdenv.cc.cc.lib
                pkgs.zlib
              ]
            }:$LD_LIBRARY_PATH"

            echo "⚡ DSA Flake Environment Loaded! ⚡"
            echo "Rust:   $(rustc --version)"
            echo "Python: $(python --version)"
            echo "uv:     $(uv --version)"
          '';
        };
      }
    );
}
