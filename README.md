# ADEM Proofs

This repository contains formal proofs of the ADEM design, encoded for the [Tamarin model checker](https://tamarin-prover.github.io/).
We were using Tamarin version 1.8.0 to find and check proofs.

## Prerequisites

To use our formal model and proofs, you need to install:

- The [Tamarin prover v1.8.0](https://tamarin-prover.github.io/manual/master/book/002_installation.html).
Probably, later versions will work as well, but v1.8.0 was used during creation of the model and proofs.
- [Python3](https://www.python.org/downloads/) to run the custom proof heuristics provided in `oracle.py`.

It might happen that Tamarin runs into file encoding issues on your system, e.g., this has been reported for Ubuntu 20.04 and results into errors like `invalid argument (invalid byte sequence)`.
In this case, please make sure that your shell is using UTF-8 encoding.
On Ubuntu, you can configure this by executing:

```sh
export LANG=en_US.UTF-8
```

## Repository Contents

| File | Description |
|------|-------------|
| `proofs/proof.spthy` | Proofs of our formal model. |
| `adem.spthy` | The formal model of ADEM. |
| `batch-run-all.sh` | A script to prove all lemmas but `Executability`. This lemma must be proven manually (see note below). |
| `oracle.py` | Custom proof heuristics to guide proof search. |

## Verifying and Finding Proofs

We provide proofs for all lemmas (i.e., our model's security properties) in the directory `/proofs`.
Proofs can checked by running:

```sh
tamarin-prover ./proofs/proofs.spthy
```

You can also find proofs, either automated or manually.
To find a proof for all lemmas (except `CanReceiveEmblem`) automatically, run the script:

```sh
./batch-run-all.sh
```

The lemma `CanReceiveEmblem` must be proven manually.
See the comment below.

Should you see a warning regarding wellformedness checks, please see our note below.

### Note on Executability Lemma

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

### Note on Wellformedness Checks

It might happen that Tamarin outputs the following warning when verifying or generating proofs:

```
WARNING:  1 wellformedness check failed!
          The analysis results might be wrong!
```

This is most likely due to a wellformedness check timing out.
You can verify this by scrolling up in the terminal output a bit.
There you should see:

```
/*
WARNING: the following wellformedness checks failed!

Derivation Checks
=================

  Derivation checks timed out. Use --derivcheck-timeout=INT to configure timeout, 0 to deactivate.
*/
```

To fix this warning, we suggest increasing that timeout by passing the argument `--derivcheck-timeout=300` to Tamarin.
Should they still time out, you may need to increase that timeout further, but 300 seconds should suffice.

## Acknowledgements

Work on this project was funded by the Werner Siemens-Stiftung (WSS).
We thank the WSS for their generous support.
