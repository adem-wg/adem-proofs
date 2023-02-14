# ADEM Proofs

This repository contains formal proofs of the ADEM design, encoded for the [Tamarin model checker](https://tamarin-prover.github.io/).

You can batch run the proof for a lemma, e.g., `AuthenticEmblem`, using the command (multiple `--prove=...` possible):

```sh
tamarin-prover --prove=AuthenticEmblem adem.spthy
```

The directory `/proofs` also contains proofs.
As the file names suggest, `Ex.spthy` contains proofs for existentially quantified lemmas, and `AllButEx.spthy` for universally quantified lemmas.
Proofs can be inspected visually by running the following command inside the `/proofs` directory:

```sh
tamarin-prover interactive .
```

After having started Tamarin in interactive mode, you can navigate to `localhost:3001` to inspect loaded files.

The `*-run.spthy` scripts provided within this repository are targeted towards a particular development environment, yet, you still may find them useful.
If a script does not work for you, you may need to replace `tamarin-prover-release` with `tamarin-prover` in the scripts.

## Acknowledgements

Work on this project was funded by the Werner Siemens-Stiftung (WSS).
We thank the WSS for their generous support.
