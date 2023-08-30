# ADEM Proofs

This repository contains formal proofs of the ADEM design, encoded for the [Tamarin model checker](https://tamarin-prover.github.io/).

You can batch run the proof for a lemma, e.g., `AuthenticEmblem`, using the command (multiple `--prove=...` possible):

```sh
tamarin-prover --prove=AuthenticEmblem adem.spthy
```

The directory `/proofs` also contains proofs for all `all-traces` lemmas, i.e., our model's security properties.
Proofs can checked by running:

```sh
tamarin-prover ./proofs/all-traces.spthy
```

Unfortunately, a Tamarin bug prevents us from providing you with proven `exists-trace` lemmas.
To verify that these are valid, you must prove them yourselves each time anew.
This works straight-forward for all `exists-trace` lemmas, but not `CanReceiveEmblem`, which must be proven manually.
The methodology here is easy, though, as it is guided by the manual oracle.
Follow these steps to prove the lemma:

* `simplify`
* Solve first goal
* Solve first goal
* Skip to case `ReceiveEmblem_case_1` and solve first goal
* Skip to case `ReceiveEmblem` and press `autoprove` (scroll down or press keyboard button `a`)

The `*-run.spthy` scripts provided within this repository are targeted towards a particular development environment, yet, you still may find them useful.
If a script does not work for you, you may need to replace `tamarin-prover-release` with `tamarin-prover` in the scripts.

## Acknowledgements

Work on this project was funded by the Werner Siemens-Stiftung (WSS).
We thank the WSS for their generous support.
