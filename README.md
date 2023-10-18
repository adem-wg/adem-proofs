# ADEM Proofs

This repository contains formal proofs of the ADEM design, encoded for the [Tamarin model checker](https://tamarin-prover.github.io/).
We were using Tamarin version 1.8.0 to find and check proofs.

We provide proofs for all lemmas (i.e., our model's security properties) in the directory `/proofs`.
Proofs can checked by running:

```sh
tamarin-prover ./proofs/proofs.spthy
```

You can also find proofs, either automated or manually.
To find a proof for a lemma automated, e.g., `AuthenticEmblem`, use the command (multiple `--prove=...` possible):

```sh
tamarin-prover --prove=AuthenticEmblem adem.spthy
```

You can prove all lemmas but `CanReceiveEmblem` yourself by executing the `batch-run-all.sh` script.
The lemma `CanReceiveEmblem` must be proven manually.
See the comment below.

## Note on Executability Lemma

If you want to find proofs for lemmas yourself, note that the lemma `CanReceiveEmblem` must be proven manually.
The methodology here is easy, as it is guided by the manual oracle.
First, launch Tamarin in interactive mode:

```sh
tamarin-prover interactive .
```

Second, follow these steps to prove the lemma:

* `simplify`
* Solve first goal
* Skip to case `ReceiveEmblem_case_1` and solve first goal
* Solve first goal
* Skip to case `ReceiveEmblem` and use `autoprove` (scroll down or press keyboard button `a`)

## Acknowledgements

Work on this project was funded by the Werner Siemens-Stiftung (WSS).
We thank the WSS for their generous support.
