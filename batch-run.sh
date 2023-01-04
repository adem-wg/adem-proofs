tamarin-prover-release +RTS -N10 -RTS --output=$1.spthy "${@:2}" adem.spthy > $1.log 2>&1 &
